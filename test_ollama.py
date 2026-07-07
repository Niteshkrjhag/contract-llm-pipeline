import os
import requests
from dotenv import load_dotenv

load_dotenv()

key = "a56863eaa4814b9cacff78f0753ad742.ESNP3NAsYC71j87_75xCK0Qc"

# URLs to test
urls = [
    "https://api.ollama.com/v1/models",
    "https://api.ollama.ai/v1/models",
    "https://api.ollama.cloud/v1/models",
    "https://api.ollama.com/api/tags"
]

for url in urls:
    try:
        response = requests.get(url, headers={"Authorization": f"Bearer {key}"}, timeout=5)
        if response.status_code == 200:
            models = response.json().get('data', [])
            names = [m.get('id', m.get('name', '')) for m in models]
            print(f"Models on {url}:")
            print(names[:20]) # Print first 20
    except Exception as e:
        pass
