import requests

api_key = "a0ad5e7a32eb6acd9f46d36030a4f214"
url = "https://api.crunchbase.com/v3.1/organizations"
headers = {"Authorization": f"Bearer {api_key}"}
params = {"name": "OpenAI"}

try:
    response = requests.get(url, headers=headers, params=params, timeout=10)
    response.raise_for_status()
    print("API Response:", response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    if e.response:
        print(f"Response Text: {e.response.text}")
