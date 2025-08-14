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

MEETING_HINTS = re.compile(
    r"(meeting|conference|symposium|workshop|seminar|colloquium|poster|aps|aas|agu|taccster)",
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

def scholar_items(user_id="", name=""):
    if not HAVE_SCHOLAR: return []
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
    for p in a.get("publications", [])[:150]:
        try:
            p_full = scholarly.fill(p, sections=["bib", "citation_link"])
            bib = p_full.get("bib", {})
            title = bib.get("title") or ""
            venue = (bib.get("venue") or bib.get("journal") or bib.get("publisher") or "")
            # only keep items that look like talks/posters/meetings
            blob = f"{title} {venue}"
            if not MEETING_HINTS.search(blob):
                continue
            year = None
            y = (bib.get("pub_year") or bib.get("year") or "").strip()
            if y:
                try: year = int(y)
                except: pass

            url = p_full.get("pub_url") or p_full.get("eprint_url") or ""
            item = {
                "title": title,
                "type": "Talk",
                "event": venue,
                "location": "",
                "date": f"{year}-01-01" if year else "",
                "url": url,
                "slides": "",
                "poster": "",
                "video": "",
                "coauthors": "",
                "notes": "",
                "_source": ["scholar"]
            }
            talks.append(item)
            time.sleep(0.35)
        except Exception:
            continue
    return talks

def merge_dedupe(items):
    out = []
    seen = set()
    for it in items:
        key = (norm_title(it.get("title")), (it.get("date") or "")[:4], (it.get("url") or "").lower())
        if key in seen: 
            continue
        seen.add(key)
        # normalize minimal fields
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

    # Manual first (source of truth), then auto
    merged = merge_dedupe(manual + auto)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps({
        "updated": datetime.utcnow().isoformat() + "Z",
        "items": merged
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK: wrote {len(merged)} talks to {OUT_PATH}")

if __name__ == "__main__":
    main()
