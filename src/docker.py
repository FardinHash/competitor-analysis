import sys
import asyncio
from orchestrator import Orchestrator

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: docker run --env-file .env competitor-analysis <company_name>")
        sys.exit(1)
    
    query = sys.argv[1]
    orchestrator = Orchestrator()
    report_path = asyncio.run(orchestrator.run(query))
    print(f"Report generated at: {report_path}")
