import requests
from bs4 import BeautifulSoup
import json
import re


def fetch_wikipedia_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def extract_title(soup):
    title_tag = soup.find("h1", {"id": "firstHeading"})
    return title_tag.get_text() if title_tag else ""


def extract_first_sentence(soup):
    p = soup.find("p")
    if p:
        p_text = p.get_text().strip()
        match = re.search(r"^.+?[.!?]", p_text)
        if match:
            return match.group()
    return ""


def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Web_scraping"
    html = fetch_wikipedia_page(url)
    soup = BeautifulSoup(html, "html.parser")
    extracted_data = {
        "title": extract_title(soup),
        "first_sentence": extract_first_sentence(soup)
    }
    print("Extracted Data:", extracted_data)
    save_to_json(extracted_data, "extracted_wikipedia_data.json")
