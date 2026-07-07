import os
from openai import OpenAI
import requests

key = "a56863eaa4814b9cacff78f0753ad742.ESNP3NAsYC71j87_75xCK0Qc"

# Test 1: Native API
print("Testing Native API...")
try:
    response = requests.post(
        "https://ollama.com/api/generate",
        headers={"Authorization": f"Bearer {key}"},
        json={"model": "gpt-oss:120b", "prompt": "Say hi", "stream": False},
        timeout=10
    )
    print(f"Native API Status: {response.status_code}")
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.text)
except Exception as e:
    print(e)

# Test 2: OpenAI Compatible API
print("\nTesting OpenAI Compatible API...")
try:
    client = OpenAI(base_url="https://ollama.com/v1", api_key=key)
    res = client.chat.completions.create(
        model="gpt-oss:120b",
        messages=[{"role": "user", "content": "Say hi"}],
        max_tokens=10
    )
    print("OpenAI Compatible API works!")
    print(res.choices[0].message.content)
except Exception as e:
    print(f"OpenAI Compatible Error: {e}")

