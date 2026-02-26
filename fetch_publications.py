import requests
import yaml

AUTHOR_ID = "29891652"  # Find at semanticscholar.org
BASE_URL = "https://api.semanticscholar.org/graph/v1"

fields = "title,year,authors,abstract,venue,externalIds,openAccessPdf"
url = f"{BASE_URL}/author/{AUTHOR_ID}/papers?fields={fields}&limit=80"

response = requests.get(url)
papers = response.json()["data"]

papers_sorted = sorted(
    papers,
    key=lambda x: x.get("year") or 0,
    reverse=True  # Most recent first; change to False for oldest first
)

pub_list = []
for paper in papers_sorted:
    entry = {
        "title": paper.get("title", ""),
        "date": paper.get("year", ""),
        "abstract": paper.get("abstract", ""),
        "venue": paper.get("venue", ""),
        "type": "conference",
    }

    paper_authors = ", ".join(a["name"] for a in paper.get("authors", []))
    if len(paper_authors.split(',')) > 9:
        paper_authors = paper_authors.split(',')[0] + ' et al.'
    entry["authors"] = paper_authors

    # Try to get the best available link
    external_ids = paper.get("externalIds", {})
    open_access_url = (paper.get("openAccessPdf") or {}).get("url", "")

    if open_access_url:  # Only use if URL is non-empty
        entry["pdf"] = open_access_url
    elif external_ids.get("ArXiv"):
        entry["pdf"] = f"https://arxiv.org/abs/{external_ids['ArXiv']}"
    elif external_ids.get("DOI"):
        entry["pdf"] = f"https://doi.org/{external_ids['DOI']}"
    elif paper.get("paperId"):
        entry["pdf"] = f"https://www.semanticscholar.org/paper/{paper['paperId']}"
    pub_list.append(entry)

with open("_data/publications.yml", "w", encoding="utf-8") as f:
    yaml.dump(pub_list, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

print("Done!")