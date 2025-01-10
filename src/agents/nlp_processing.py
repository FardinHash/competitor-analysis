import pandas as pd

class NLPProcessingAgent:
    def normalize_data(self, raw_data):
        normalized_data = {
            "google_summary": " ".join(raw_data.get("google_results", [])),
            "wikipedia_summary": raw_data.get("wikipedia_summary", ""),
        }
        return normalized_data

    def process_data(self, raw_data):
        normalized_data = {}
        for source, content in raw_data.items():
            if isinstance(content, dict):
                normalized_data[source] = pd.json_normalize(content)
            else:
                normalized_data[source] = content
        return normalized_data
