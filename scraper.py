import requests
from bs4 import BeautifulSoup

def scrape_competitor_content(competitor_url):
    """Scrapes competitor's blog titles as keywords"""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(competitor_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('h2')  # Assuming blog titles are inside <h2> tags
        keywords = [article.text.strip() for article in articles]
        return keywords
    else:
        return []

# Testing
if __name__ == "__main__":
    competitor_url = "https://example.com/blog"
    print(scrape_competitor_content(competitor_url))
