import json, os, sys, time
from datetime import datetime

# pip install scholarly
from scholarly import scholarly

USER_ID = os.environ.get("SCHOLAR_USER_ID", "").strip()
if not USER_ID:
    print("ERROR: SCHOLAR_USER_ID not set. Add it as a repository secret.", file=sys.stderr)
    sys.exit(1)

OUT_PATH = "_data/scholar.json"

def fetch_author(user_id: str):
    # Load by explicit author id (faster and more reliable than search by name)
    # https://scholar.google.com/citations?user=<USER_ID>
    author = scholarly.search_author_id(user_id)
    author = scholarly.fill(author, sections=["publications"])
    return author

def fetch_pubs(author, limit=120):
    pubs = []
    pubs_list = author.get("publications", [])[:limit]
    for idx, p in enumerate(pubs_list, start=1):
        try:
            # fill the publication to get bib (title, authors, venue, year...) and links
            p_full = scholarly.fill(p, sections=["bib", "citation_link"])
            bib = p_full.get("bib", {})
            title = bib.get("title") or p_full.get("bib", {}).get("title") or "Untitled"
            authors = ", ".join(bib.get("author", [])) if isinstance(bib.get("author"), list) else bib.get("author", "")
            year = bib.get("pub_year") or bib.get("year") or ""
            try:
                year = int(year)
            except Exception:
                year = ""

            venue = bib.get("venue") or bib.get("journal") or bib.get("publisher") or ""
            url = p_full.get("pub_url") or p_full.get("eprint_url") or ""
            pdf_url = p_full.get("eprint_url") or ""

            pubs.append({
                "title": title,
                "authors": authors,
                "year": year,
                "venue": venue,
                "url": url,
                "pdf_url": pdf_url,
                "citations": p_full.get("num_citations", 0)
            })

            # polite delay to avoid rate-limit
            time.sleep(0.5)
        except Exception as e:
            print(f"WARN: failed to fetch pub {idx}: {e}", file=sys.stderr)
            continue
    return pubs

def main():
    author = fetch_author(USER_ID)
    pubs = fetch_pubs(author)
    data = {
        "updated": datetime.utcnow().isoformat() + "Z",
        "publications": pubs
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(pubs)} publications to {OUT_PATH}")

if __name__ == "__main__":
    main()
