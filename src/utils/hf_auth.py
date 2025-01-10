import os
from huggingface_hub import login

def authenticate_hf():
    token = os.getenv("HUGGINGFACE_HUB_TOKEN")
    if token:
        login(token)
    else:
        raise ValueError("Hugging Face token not found in environment variables.")
