import os, json, time
from datetime import datetime
from pathlib import Path
import requests

USER = os.environ.get("GITHUB_USERNAME", "").strip()
TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()
OUT = Path("_data/repos.json")

if not USER:
    raise SystemExit("GITHUB_USERNAME not set")

headers = {"Accept": "application/vnd.github+json"}
if TOKEN:
    headers["Authorization"] = f"Bearer {TOKEN}"

def fetch_all_repos(user):
    # owner repos, public, exclude forks/archived
    url = f"https://api.github.com/users/{user}/repos"
    params = {"per_page": 100, "type": "owner", "sort": "updated", "direction": "desc"}
    r = requests.get(url, headers=headers, params=params, timeout=20)
    r.raise_for_status()
    data = r.json()
    repos = []
    for repo in data:
        if repo.get("fork") or repo.get("archived"):
            continue
        repos.append({
            "name": repo["name"],
            "html_url": repo["html_url"],
            "description": repo.get("description") or "",
            "language": repo.get("language") or "",
            "topics": repo.get("topics") or [],
            "stargazers_count": repo.get("stargazers_count", 0),
            "updated_at": repo.get("pushed_at") or repo.get("updated_at"),
            "fork": False
        })
        time.sleep(0.1)
    return repos

def main():
    repos = fetch_all_repos(USER)
    data = {"updated": datetime.utcnow().isoformat() + "Z", "repos": repos}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(repos)} repos to {OUT}")

if __name__ == "__main__":
    main()
