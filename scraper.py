import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def validate_url(url):
    """Ensure the URL includes a scheme; if not, prepend 'https://'."""
    parsed = urlparse(url)
    if not parsed.scheme:
        url = "https://" + url
    return url

def scrape_competitor_content(competitor_url):
    """Scrapes competitor's blog titles as keywords"""
    competitor_url = validate_url(competitor_url)  # Validate URL first
    headers = {"User-Agent": "Mozilla/5.0"}
    # Added verify=False to bypass SSL certificate verification
    response = requests.get(competitor_url, headers=headers, verify=False)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('h2')  # Assuming blog titles are inside <h2> tags
        keywords = [article.text.strip() for article in articles]
        return keywords
    else:
        return []

# Testing the function
if __name__ == "__main__":
    competitor_url = "www.intelegencia.com"
    print(scrape_competitor_content(competitor_url))
