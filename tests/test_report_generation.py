import asyncio
from src.orchestrator import Orchestrator
from src.agents.report_generator import ReportGenerator

def test_pdf_generation():
    swot_results = (
        "Strengths:\n- Innovation\n- Leadership\n\n"
        "Weaknesses:\n- High costs\n\n"
        "Opportunities:\n- Market expansion\n\n"
        "Threats:\n- Competition"
    )
    generator = ReportGenerator()
    report_path = generator.generate(swot_results, "SpaceX")
    assert report_path.endswith("SpaceX_analysis_report.pdf")
    with open(report_path, "rb") as f:
        assert len(f.read()) > 0
