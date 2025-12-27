import requests
from bs4 import BeautifulSoup
import json
import re


def fetch_wikipedia_page(url):
    """
    Fetch the HTML content of the given Wikipedia page.

    Args:
        url (str): The URL of the Wikipedia page to fetch.

    Returns:
        str: The HTML content of the page as a string.

    Raises:
        HTTPError: If the HTTP request returned an unsuccessful status code.
    """
    response = requests.get(url)

    result = response.content
    response.raise_for_status()
    
    return result


def extract_title(soup):
    """
    Extract the title of the Wikipedia page.

    Args:
        soup (BeautifulSoup): A BeautifulSoup object representing the parsed HTML.

    Returns:
        str: The title of the page.
    """
    title = soup.find("h1", {"id": "firstHeading"})
    if title:
        result = title.get_text()
    else:
        result = ""
        
    return result


def extract_first_sentence(soup):
    """
    Extract the first sentence of the first paragraph on the Wikipedia page.

    Args:
        soup (BeautifulSoup): A BeautifulSoup object representing the parsed HTML.

    Returns:
        str: The first sentence of the first paragraph.
    """
    result = ""
    p = soup.find("p")

    if p:
        p_text = p.get_text()
        match = re.search(r"^.+?[.!?]", p_text)
        if match:
            result = match.group()

    return result


def save_to_json(data, filename):
    """
    Save the extracted data to a JSON file.

    Args:
        data (dict): The data to be saved to the JSON file.
        filename (str): The name of the JSON file to save the data in.
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    
    return None


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Web_scraping"
    page_content = fetch_wikipedia_page(url)
    soup = BeautifulSoup(page_content, 'html.parser')

    # Extract the title of the page
    title = extract_title(soup)

    # Extract the first sentence of the first paragraph
    first_sentence = extract_first_sentence(soup)

    # Combine the extracted data
    extracted_data = {
        "title": title,
        "first_sentence": first_sentence
    }

    # Print the extracted data
    print("Extracted Data:", extracted_data)

    # Save the data to a JSON file
    save_to_json(extracted_data, 'extracted_wikipedia_data.json')

    print("Data successfully saved to extracted_wikipedia_data.json")