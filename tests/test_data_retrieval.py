from src.agents.data_retrieval import GoogleSearchAgent, WikipediaAgent

def test_google_data_retrieval():
    agent = GoogleSearchAgent()
    result = agent.get_google_data("OpenAI")
    assert "google_results" in result
    assert len(result["google_results"]) > 0

def test_wikipedia_data_retrieval():
    agent = WikipediaAgent()
    result = agent.get_wikipedia_data("OpenAI")
    assert "extract" in result
    assert result["extract"] != ""
