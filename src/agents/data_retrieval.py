import requests
from bs4 import BeautifulSoup

class GoogleSearchAgent:
    def get_google_data(self, query):
        """
        Retrieve summarized data from Google search results.
        """
        url = f"https://www.google.com/search?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            results = [a.text for a in soup.select("a") if a.text.strip()]
            return {"google_summary": " ".join(results[:5])}  
        except requests.exceptions.RequestException as e:
            return {"error": f"Google Search error: {e}"}

class WikipediaAgent:
    def get_wikipedia_data(self, query):
        """
        Retrieve summarized data from Wikipedia.
        """
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return {"wikipedia_summary": data.get("extract", "No summary available")}
        except requests.exceptions.RequestException as e:
            return {"error": f"Wikipedia API error: {e}"}

class LinkedInSearchAgent:
    def get_linkedin_data(self, query):
        """
        Retrieve company-related information from LinkedIn.
        """
        url = f"https://www.linkedin.com/search/results/companies/?keywords={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            results = [
                item.text.strip()
                for item in soup.select("div.entity-result__primary-subtitle")
            ]
            if results:
                return {"linkedin_summary": " ".join(results[:3])}
            else:
                return {"linkedin_summary": "No data available"}
        except requests.exceptions.RequestException as e:
            return {"error": f"LinkedIn Search error: {e}"}
