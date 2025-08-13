import os, re, json, time, sys
from pathlib import Path
from datetime import datetime
from unidecode import unidecode
from urllib.parse import urlencode, quote_plus

import requests
import feedparser
from dateutil import parser as dtparser
import difflib
import itertools
import re

ARXIV_RE = re.compile(r'arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})(?:v\d+)?', re.I)

# Scholar can be flaky on CI; import guarded
try:
    from scholarly import scholarly
    HAVE_SCHOLAR = True
except Exception:
    HAVE_SCHOLAR = False

OUT_PATH = Path("_data/scholar.json")

# --- Helpers ---------------------------------------------------------------
def extract_arxiv_id(s: str) -> str:
    if not s:
        return ""
    m = ARXIV_RE.search(s)
    return (m.group(1).lower() if m else "")

def keys_for_item(it):
    keys = []
    doi = (it.get("doi") or "").strip().lower()
    if doi:
        keys.append(("doi", doi))
    # try url/pdf_url for arxiv id
    arx = extract_arxiv_id(it.get("url") or "") or extract_arxiv_id(it.get("pdf_url") or "")
    if arx:
        keys.append(("arxiv", arx))
    nt = norm_title(it.get("title", ""))
    if nt:
        keys.append(("title", nt))
    return keys

def fuzzy_same_title(a: str, b: str, thresh: float = 0.9) -> bool:
    if not a or not b:
        return False
    ra = norm_title(a)
    rb = norm_title(b)
    if not ra or not rb:
        return False
    # quick exact-or-substring checks
    if ra == rb or ra in rb or rb in ra:
        return True
    # fall back to ratio
    return difflib.SequenceMatcher(None, ra, rb).ratio() >= thresh

def norm_title(t: str) -> str:
    t = (t or "").strip().lower()
    t = unidecode(t)
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"[^a-z0-9 ]", "", t)
    return t

def safe_int(x):
    try:
        return int(x)
    except Exception:
        return ""

def http_get_json(url, params=None, headers=None):
    if params:
        url = url + ("&" if "?" in url else "?") + urlencode(params)
    r = requests.get(url, headers=headers or {}, timeout=20)
    r.raise_for_status()
    return r.json()

def keep_previous_if_any():
    if OUT_PATH.exists():
        try:
            return json.loads(OUT_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"updated": "", "publications": []}

# --- Sources ---------------------------------------------------------------

def fetch_arxiv(author: str, max_results=50):
    """Fetch by author exact match."""
    if not author:
        return []
    q = f'au:"{author}"'
    url = ("https://export.arxiv.org/api/query?"
           f"search_query={quote_plus(q)}&start=0&max_results={max_results}")
    feed = feedparser.parse(url)
    pubs = []
    for e in feed.entries:
        title = e.title.strip()
        url = e.link
        pdf = ""
        for l in e.links:
            if l.get("type") == "application/pdf":
                pdf = l.get("href")
                break
        year = ""
        if e.get("published"):
            try:
                year = dtparser.parse(e.published).year
            except Exception:
                pass
        authors = ", ".join(a.name for a in e.get("authors", [])) if e.get("authors") else ""
        primary = ""
        try:
            primary = e["arxiv_primary_category"]["term"]
        except Exception:
            pass
        doi = ""
        for l in e.get("links", []):
            if "dx.doi.org" in l.get("href", ""):
                doi = l["href"].split("dx.doi.org/")[-1]
        pubs.append({
            "title": title, "authors": authors, "year": year,
            "venue": f"arXiv ({primary})" if primary else "arXiv",
            "url": url, "pdf_url": pdf, "doi": doi, "citations": 0, "source": ["arxiv"]
        })
        time.sleep(0.15)
    return pubs

def fetch_orcid(orcid_id: str):
    """Public ORCID works."""
    if not orcid_id:
        return []
    url = f"https://pub.orcid.org/v3.0/{orcid_id}/works"
    headers = {"Accept": "application/json"}
    r = requests.get(url, headers=headers, timeout=20)
    if r.status_code != 200:
        return []
    data = r.json()
    pubs = []
    for g in data.get("group", []):
        work = g.get("work-summary", [{}])[0]
        title = (work.get("title", {}) or {}).get("title", {}) or {}
        title = title.get("value", "")
        year = ""
        if work.get("publication-date"):
            y = work["publication-date"].get("year", {}).get("value")
            year = safe_int(y)
        url = ""
        if work.get("url", {}) and work["url"].get("value"):
            url = work["url"]["value"]
        doi = ""
        for ext in work.get("external-ids", {}).get("external-id", []):
            if (ext.get("external-id-type") or "").lower() == "doi":
                doi = ext.get("external-id-value") or ""
                break
        venue = (work.get("journal-title", {}) or {}).get("value", "") or ""
        # authors not directly in ORCID summary
        pubs.append({
            "title": title, "authors": "", "year": year,
            "venue": venue, "url": url, "pdf_url": "", "doi": doi,
            "citations": 0, "source": ["orcid"]
        })
        time.sleep(0.1)
    return pubs

def fetch_scholar(user_id: str = "", name: str = ""):
    """Best-effort; can be blocked on CI. Never crash."""
    if not HAVE_SCHOLAR:
        return []
    try:
        if user_id:
            author = scholarly.search_author_id(user_id)
        elif name:
            author = scholarly.fill(next(scholarly.search_author(name)))
        else:
            return []
        author = scholarly.fill(author, sections=["publications"])
        pubs = []
        for p in author.get("publications", [])[:150]:
            try:
                p_full = scholarly.fill(p, sections=["bib", "citation_link"])
            except Exception:
                continue
            bib = p_full.get("bib", {})
            title = bib.get("title") or ""
            authors = ", ".join(bib.get("author", [])) if isinstance(bib.get("author"), list) else (bib.get("author") or "")
            year = safe_int(bib.get("pub_year") or bib.get("year") or "")
            venue = bib.get("venue") or bib.get("journal") or bib.get("publisher") or ""
            url = p_full.get("pub_url") or p_full.get("eprint_url") or ""
            pdf_url = p_full.get("eprint_url") or ""
            pubs.append({
                "title": title, "authors": authors, "year": year,
                "venue": venue, "url": url, "pdf_url": pdf_url, "doi": "",
                "citations": p_full.get("num_citations", 0), "source": ["scholar"]
            })
            time.sleep(0.4)
        return pubs
    except Exception:
        return []

# --- Crossref enrichment ---------------------------------------------------

def crossref_enrich(item, mailto=None):
    """Add DOI/venue/year/url if missing, using title search; be polite."""
    title = (item.get("title") or "").strip()
    if not title:
        return item
    params = {"query.bibliographic": title, "rows": 3}
    if mailto:
        params["mailto"] = mailto
    try:
        data = http_get_json("https://api.crossref.org/works", params=params)
    except Exception:
        return item
    def clean(s): return norm_title(s or "")
    nt = clean(title)
    best = None
    for m in data.get("message", {}).get("items", []):
        # simple title match heuristic
        mtitles = m.get("title") or []
        if not mtitles:
            continue
        mt = clean(mtitles[0])
        if nt == mt or nt in mt or mt in nt:
            best = m
            break
    if not best:
        return item
    doi = best.get("DOI") or item.get("doi")
    url = best.get("URL") or item.get("url")
    venue = ""
    if best.get("short-container-title"):
        venue = best["short-container-title"][0]
    elif best.get("container-title"):
        venue = best["container-title"][0]
    year = item.get("year")
    try:
        issued = best.get("issued", {}).get("date-parts", [[None]])[0][0]
        if issued:
            year = safe_int(issued)
    except Exception:
        pass
    return {
        **item,
        "doi": doi or item.get("doi") or "",
        "url": url or item.get("url") or "",
        "venue": venue or item.get("venue") or "",
        "year": year,
        "source": sorted(list(set(item.get("source", []) + ["crossref"])))
    }

# --- Merge/dedupe ----------------------------------------------------------

def merge_two(a, b):
    """Merge b into a."""
    for f in ["title", "authors", "venue", "url", "pdf_url", "doi", "year"]:
        if not a.get(f) and b.get(f):
            a[f] = b[f]
    a["citations"] = max(a.get("citations", 0), b.get("citations", 0))
    a["source"] = sorted(list(set((a.get("source") or []) + (b.get("source") or []))))
    return a

def merge_items(lists):
    # Pass 1: merge by DOI / arXiv / normalized title
    merged = []
    index = {}  # key -> idx in merged

    for it in itertools.chain.from_iterable(lists):
        # try to find an existing record by any key
        found_idx = None
        for k in keys_for_item(it):
            if k in index:
                found_idx = index[k]
                break
        if found_idx is None:
            merged.append(it)
            idx = len(merged) - 1
            for k in keys_for_item(it):
                index[k] = idx
        else:
            merge_two(merged[found_idx], it)
            # refresh index with possibly new keys (e.g., DOI just added)
            for k in keys_for_item(merged[found_idx]):
                index[k] = found_idx

    # Pass 2: fuzzy title merge (handles punctuation/casing differences)
    i = 0
    while i < len(merged):
        j = i + 1
        while j < len(merged):
            ai, aj = merged[i], merged[j]
            # same DOI or arXiv id -> definitely same
            same_doi = (ai.get("doi") or "").lower() and (ai.get("doi") or "").lower() == (aj.get("doi") or "").lower()
            same_arx = extract_arxiv_id(ai.get("url") or "") and extract_arxiv_id(ai.get("url") or "") == extract_arxiv_id(aj.get("url") or "")
            # otherwise, fuzzy title + close year
            close_year = (not ai.get("year") or not aj.get("year") or abs(int(ai.get("year") or 0) - int(aj.get("year") or 0)) <= 1)
            if same_doi or same_arx or (fuzzy_same_title(ai.get("title", ""), aj.get("title", "")) and close_year):
                merge_two(ai, aj)
                merged.pop(j)
                continue
            j += 1
        i += 1

    return merged


# --- Main ------------------------------------------------------------------

def main():
    prev = keep_previous_if_any()

    scholar_id = os.environ.get("SCHOLAR_USER_ID", "").strip()
    scholar_name = os.environ.get("SCHOLAR_NAME", "").strip()
    arxiv_author = os.environ.get("ARXIV_AUTHOR", "").strip()
    orcid_id     = os.environ.get("ORCID_ID", "").strip()
    cr_mailto    = os.environ.get("CROSSREF_MAILTO", "").strip()

    all_items = []

    # Fetch from each source (best-effort; don't fail if one breaks)
    try:
        if arxiv_author:
            all_items += fetch_arxiv(arxiv_author)
    except Exception as e:
        print(f"WARN arXiv: {e}", file=sys.stderr)

    try:
        if orcid_id:
            all_items += fetch_orcid(orcid_id)
    except Exception as e:
        print(f"WARN ORCID: {e}", file=sys.stderr)

    try:
        if HAVE_SCHOLAR and (scholar_id or scholar_name):
            all_items += fetch_scholar(scholar_id, scholar_name)
    except Exception as e:
        print(f"WARN Scholar: {e}", file=sys.stderr)

    # If everything failed, keep previous so page doesn't go empty
    if not all_items:
        print("ERROR: all sources returned 0; keeping previous data", file=sys.stderr)
        OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        OUT_PATH.write_text(json.dumps(prev, ensure_ascii=False, indent=2), encoding="utf-8")
        return

    # Deduplicate
    merged = merge_items([all_items])

    # Enrich via Crossref (polite: 200–300ms between calls)
    enriched = []
    for it in merged:
        enriched.append(crossref_enrich(it, mailto=cr_mailto))
        time.sleep(0.25)

    # Deduplicate again (post-enrichment, now that DOIs exist)
    final = merge_items([enriched])

    # Final sort
    final.sort(key=lambda x: (x.get("year") or 0, (x.get("title") or "").lower()), reverse=True)

    data = {"updated": datetime.utcnow().isoformat() + "Z", "publications": final}
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK: wrote {len(enriched)} publications to {OUT_PATH}")

if __name__ == "__main__":
    main()
