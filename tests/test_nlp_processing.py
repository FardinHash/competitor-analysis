from src.agents.nlp_processing import NLPProcessingAgent

def test_nlp_processing_with_llama2():
    agent = NLPProcessingAgent()
    raw_data = {
        "google_summary": "OpenAI is transforming AI research with innovative models.",
        "wikipedia_summary": "OpenAI is a research lab that focuses on the ethical use of AI.",
        "linkedin_summary": "Known for advancing machine learning technologies."
    }
    processed_data = agent.process_data(raw_data)

    assert "google_summary" in processed_data
    assert "wikipedia_summary" in processed_data
    assert "linkedin_summary" in processed_data
    assert processed_data["google_summary"] == "OpenAI is transforming AI research with innovative models."
    assert processed_data["wikipedia_summary"] == "OpenAI is a research lab that focuses on the ethical use of AI."
    assert processed_data["linkedin_summary"] == "Known for advancing machine learning technologies."
