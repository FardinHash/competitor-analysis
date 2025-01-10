import requests
from bs4 import BeautifulSoup

class GoogleSearchAgent:
    def get_google_data(self, query):
        url = f"https://www.google.com/search?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            results = [a.text for a in soup.select("a")]
            return {"google_results": results[:5]}  
        except requests.exceptions.RequestException as e:
            return {"error": f"Google Search error: {e}"}

class WikipediaAgent:
    def get_wikipedia_data(self, query):
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()  
        except requests.exceptions.RequestException as e:
            return {"error": f"Wikipedia API error: {e}"}
