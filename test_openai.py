import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are an expert SWOT analysis generator."},
            {"role": "user", "content": "Provide a brief SWOT analysis for OpenAI."}
        ],
        max_tokens=100
    )
    print("SWOT Analysis Response:")
except Exception as e:
    print(f"Error: {e}")
