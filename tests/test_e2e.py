from src.orchestrator import Orchestrator
import asyncio

def test_llama2_end_to_end():
    orchestrator = Orchestrator()
    query = "OpenAI"
    report_path = asyncio.run(orchestrator.run(query))
    assert report_path.endswith(f"{query}_analysis_report.pdf")
    with open(report_path, "rb") as f:
        assert len(f.read()) > 0
