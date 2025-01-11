from src.agents.swot_analysis import SWOTAnalysisAgent

def test_swot_analysis():
    data = {
        "google_summary": "OpenAI develops cutting-edge AI models.",
        "wikipedia_summary": "OpenAI is an AI research lab."
    }
    agent = SWOTAnalysisAgent()
    result = agent.analyze(data, "OpenAI")
    assert "Strengths:" in result
    assert "Weaknesses:" in result
    assert "Opportunities:" in result
    assert "Threats:" in result
