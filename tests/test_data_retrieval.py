from src.agents.data_retrieval import GoogleSearchAgent, WikipediaAgent, LinkedInSearchAgent

def test_llama2_google_data_retrieval():
    agent = GoogleSearchAgent()
    result = agent.get_google_data("OpenAI")
    assert "google_summary" in result
    assert len(result["google_summary"]) > 0

def test_llama2_wikipedia_data_retrieval():
    agent = WikipediaAgent()
    result = agent.get_wikipedia_data("OpenAI")
    assert "wikipedia_summary" in result
    assert len(result["wikipedia_summary"]) > 0

def test_llama2_linkedin_data_retrieval():
    agent = LinkedInSearchAgent()
    result = agent.get_linkedin_data("OpenAI")
    assert "linkedin_summary" in result
    assert len(result["linkedin_summary"]) > 0