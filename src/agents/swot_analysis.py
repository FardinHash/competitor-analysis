import openai
import os
from dotenv import load_dotenv

class SWOTAnalysisAgent:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in .env file")
    
    def analyze(self, data, company_name):
        openai.api_key = self.api_key

        google_summary = data.get("google_summary", "No data available")
        wikipedia_summary = data.get("wikipedia_summary", "No data available")
        linkedin_summary = data.get("linkedin_summary", "No data available")
        
        prompt = (
            f"Perform a detailed SWOT analysis for the company '{company_name}' using the following data:\n\n"
            f"Google Summary:\n{google_summary}\n\n"
            f"Wikipedia Summary:\n{wikipedia_summary}\n\n"
            f"LinkedIn Summary:\n{linkedin_summary}\n\n"
            "Provide the analysis in the format:\n"
            "Strengths:\n- Point 1\n- Point 2\n\n"
            "Weaknesses:\n- Point 1\n- Point 2\n\n"
            "Opportunities:\n- Point 1\n- Point 2\n\n"
            "Threats:\n- Point 1\n- Point 2"
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a business analyst specializing in SWOT analysis."},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=500,
            )
            return response["choices"][0]["message"]["content"].strip()
        except openai.error.OpenAIError as e:
            return f"Error generating SWOT analysis: {e}"
