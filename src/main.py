import asyncio
from orchestrator import Orchestrator

if __name__ == "__main__":
    query = input("Enter a company name or product query: ")
    orchestrator = Orchestrator()
    report_path = asyncio.run(orchestrator.run(query))
    print(f"Report generated at: {report_path}")
