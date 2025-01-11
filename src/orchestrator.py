from agents.data_retrieval import GoogleSearchAgent, WikipediaAgent, LinkedInSearchAgent
from utils.normalization import normalize_data
from agents.nlp_processing import NLPProcessingAgent
from agents.swot_analysis import SWOTAnalysisAgent
from agents.report_generator import ReportGenerator

class Orchestrator:
    def __init__(self):
        self.google_agent = GoogleSearchAgent()
        self.wikipedia_agent = WikipediaAgent()
        self.linkedin_agent = LinkedInSearchAgent()
        self.nlp_agent = NLPProcessingAgent()
        self.swot_agent = SWOTAnalysisAgent()
        self.report_agent = ReportGenerator()

    async def run(self, query):
        # Step 1: Retrieve data from alternative sources
        google_data = self.google_agent.get_google_data(query)
        wikipedia_data = self.wikipedia_agent.get_wikipedia_data(query)
        linkedin_data = self.linkedin_agent.get_linkedin_data(query)

        # Step 2: Normalize data
        raw_data = {"google": google_data, "wikipedia": wikipedia_data, "linkedin": linkedin_data,}
        normalized_data = normalize_data(raw_data)

        # Step 3: Process data
        processed_data = self.nlp_agent.process_data(normalized_data)

        # Step 4: Perform SWOT Analysis
        swot_results = self.swot_agent.analyze(processed_data, query)

        # Step 5: Generate Report
        report_path = self.report_agent.generate(swot_results, query)

        return report_path
