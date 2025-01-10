import pandas as pd

class NLPProcessingAgent:
    def process_data(self, raw_data):
        normalized_data = {}
        for source, content in raw_data.items():
            if isinstance(content, dict):
                normalized_data[source] = pd.json_normalize(content)
            else:
                normalized_data[source] = content
        return normalized_data
