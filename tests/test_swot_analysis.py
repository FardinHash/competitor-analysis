from src.agents.swot_analysis import SWOTAnalysisAgent

def test_llama2_swot_analysis():
    agent = SWOTAnalysisAgent()
    input_data = {
        "google_summary": "OpenAI is revolutionizing AI with advanced models.",
        "wikipedia_summary": "OpenAI is an AI research lab founded to ensure artificial general intelligence benefits humanity.",
        "linkedin_summary": "Known for cutting-edge research in AI and machine learning."
    }
    company_name = "OpenAI"

    result = agent.analyze(input_data, company_name)

    assert "Strengths:" in result
    assert "Weaknesses:" in result
    assert "Opportunities:" in result
    assert "Threats:" in result
    assert len(result) > 100  
