from src.agents.nlp_processing import NLPProcessingAgent

def test_nlp_processing():
    raw_data = {
        "google_results": ["OpenAI develops cutting-edge AI models."],
        "wikipedia_summary": "OpenAI is an AI research lab."
    }
    agent = NLPProcessingAgent()
    processed_data = agent.normalize_data(raw_data)
    assert "google_summary" in processed_data
    assert "wikipedia_summary" in processed_data
    assert processed_data["google_summary"] != ""
    assert processed_data["wikipedia_summary"] != ""
