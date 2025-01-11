from dotenv import load_dotenv
import os

def authenticate_hf():
    load_dotenv()

    token = os.getenv("HUGGINGFACE_HUB_TOKEN")
    if not token:
        raise ValueError("Hugging Face token not found in environment variables.")
    return token
