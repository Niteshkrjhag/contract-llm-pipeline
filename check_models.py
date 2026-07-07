import os
import requests
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Check Gemini
print("--- Gemini Models ---")
gemini_key = os.getenv("GEMINI_API_KEY")
if gemini_key:
    client = genai.Client(api_key=gemini_key)
    try:
        models = [m.name for m in client.models.list()]
        print("Available Gemini Models:", models)
    except Exception as e:
        print("Error listing Gemini models:", e)
else:
    print("No GEMINI_API_KEY")

# Check OpenRouter
print("--- OpenRouter Models ---")
openrouter_key = os.getenv("OPENROUTER_API_KEY")
if openrouter_key:
    try:
        response = requests.get(
            "https://openrouter.ai/api/v1/models",
            headers={"Authorization": f"Bearer {openrouter_key}"}
        )
        if response.status_code == 200:
            models = response.json().get('data', [])
            free_models = [m['id'] for m in models if m.get('pricing', {}).get('prompt', '1') == '0']
            print("Free OpenRouter Models:", free_models[:10]) # print first 10
        else:
            print("Failed to fetch OpenRouter models:", response.text)
    except Exception as e:
        print("Error listing OpenRouter models:", e)
else:
    print("No OPENROUTER_API_KEY")
