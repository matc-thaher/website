# scripts/update_talks.py
import os, json, time, sys, re
from pathlib import Path
from datetime import datetime
from unidecode import unidecode
from dateutil import parser as dtparser
import yaml

# Optional Scholar import (best-effort)
try:
    from scholarly import scholarly
    HAVE_SCHOLAR = True
except Exception:
    HAVE_SCHOLAR = False

MANUAL_PATH = Path("_data/talks_manual.yml")
OUT_PATH    = Path("_data/talks.json")

# --- Heuristics to identify talks/posters/meetings -------------------------

# Strong signals in venue/title
MEETING_HINTS = re.compile(
    r"(meeting|conference|symposium|workshop|seminar|colloquium|colloquia|poster|presentation|"
    r"aps|baps|bulletin|march meeting|april meeting|joint fall|taccster|aas|agu|damop|dpp|dnp|dpf)",
    re.I
)

# Strong signals in links
URL_HINTS = re.compile(
    r"(meetings\.aps\.org|aps\.org/meetings|hdl\.handle\.net|utexas|taccster|indico|eventbrite)",
    re.I
)

def norm_title(s):
    s = (s or "").strip().lower()
    s = unidecode(s)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[^a-z0-9 ]", "", s)
    return s

def load_manual():
    if not MANUAL_PATH.exists():
        return []
    data = yaml.safe_load(MANUAL_PATH.read_text(encoding="utf-8")) or {}
    return data.get("items", [])

def looks_like_talk(title, venue, url, eprint_url):
    blob = " ".join([title or "", venue or ""])
    if MEETING_HINTS.search(blob):
        return True
    for u in (url or "", eprint_url or ""):
        if URL_HINTS.search(u or ""):
            return True
    return False

def scholar_items(user_id="", name=""):
    if not HAVE_SCHOLAR:
        return []
    try:
        if user_id:
            a = scholarly.search_author_id(user_id)
        elif name:
            a = scholarly.fill(next(scholarly.search_author(name)))
        else:
            return []
        a = scholarly.fill(a, sections=["publications"])
    except Exception:
        return []

    talks = []
    for p in a.get("publications", [])[:180]:
        try:
            p_full = scholarly.fill(p, sections=["bib", "citation_link"])
            bib = p_full.get("bib", {}) or {}
            title = bib.get("title") or ""
            venue = bib.get("venue") or bib.get("journal") or bib.get("publisher") or ""
            url = p_full.get("pub_url") or ""
            eurl = p_full.get("eprint_url") or ""

            if not looks_like_talk(title, venue, url, eurl):
                continue

            # Date (year → YYYY-01-01 if day not known)
            year = (bib.get("pub_year") or bib.get("year") or "").strip()
            date = ""
            if year:
                try:
                    date = f"{int(year)}-01-01"
                except Exception:
                    date = ""

            item = {
                "title": title,
                "type": "Talk" if "poster" not in (title.lower() + " " + venue.lower()) else "Poster",
                "event": venue,
                "location": "",
                "date": date,
                "url": url or eurl,
                "slides": "",
                "poster": "",
                "video": "",
                "coauthors": "",
                "notes": "",
                "_source": ["scholar"]
            }
            talks.append(item)
            time.sleep(0.3)  # be polite
        except Exception:
            continue
    return talks

def merge_dedupe(items):
    out = []
    seen = set()
    for it in items:
        # key: normalized title + year (from date) + url host (rough)
        title_key = norm_title(it.get("title"))
        year_key  = (it.get("date") or "")[:4]
        url_key   = (it.get("url") or "").strip().lower()
        key = (title_key, year_key, url_key)
        if key in seen:
            continue
        seen.add(key)

        # Normalize date if we have it
        if it.get("date"):
            try:
                it["date"] = dtparser.parse(it["date"]).date().isoformat()
            except Exception:
                pass

        out.append(it)

    # newest first
    out.sort(key=lambda x: (x.get("date") or "", x.get("title") or ""), reverse=True)
    return out

def main():
    manual = load_manual()

    user_id = os.environ.get("SCHOLAR_USER_ID", "").strip()
    name    = os.environ.get("SCHOLAR_NAME", "").strip()
    auto    = scholar_items(user_id, name)

    # Manual is source of truth -> always included
    merged = merge_dedupe(manual + auto)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps({
        "updated": datetime.utcnow().isoformat() + "Z",
        "items": merged
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"OK: manual={len(manual)}, scholar={len(auto)}, merged={len(merged)} → {_short_list(merged)}")

def _short_list(items, n=6):
    return ", ".join([i.get("title","")[:32] + ("…" if len(i.get("title",""))>32 else "") for i in items[:n]])

if __name__ == "__main__":
    main()
