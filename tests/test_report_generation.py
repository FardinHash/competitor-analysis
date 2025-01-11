import os
from src.agents.report_generator import ReportGenerator

def test_report_generation_with_gemma2():
    agent = ReportGenerator()
    swot_results = (
        "Strengths:\n- Innovative AI models.\n- Strong research team.\n\n"
        "Weaknesses:\n- Dependency on external funding.\n\n"
        "Opportunities:\n- Growing AI adoption in various industries.\n\n"
        "Threats:\n- Competition from major tech players."
    )
    query = "OpenAI"

    report_path = agent.generate(swot_results, query)

    assert report_path.endswith(f"{query}_analysis_report.pdf")
    assert os.path.exists(report_path)

    with open(report_path, "rb") as f:
        assert len(f.read()) > 0
