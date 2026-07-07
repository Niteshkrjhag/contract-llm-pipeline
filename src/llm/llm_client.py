import os
from google import genai
from google.genai import types
from openai import OpenAI
from src.utils.logger import get_logger
from dotenv import load_dotenv

load_dotenv()
logger = get_logger(__name__)

# Load configuration
fallback_order_str = os.getenv("LLM_FALLBACK_ORDER", "Gemini,Ollama,OpenRouter,OpenAI")
LLM_FALLBACK_ORDER = [p.strip() for p in fallback_order_str.split(',')]

openai_api_key = os.getenv("OPENAI_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434/v1")
ollama_api_key = os.getenv("OLLAMA_API_KEY", "ollama")

# Initialize clients
clients = {}

if gemini_api_key:
    clients["Gemini"] = genai.Client(api_key=gemini_api_key)

if openai_api_key:
    clients["OpenAI"] = OpenAI(api_key=openai_api_key)

if openrouter_api_key:
    clients["OpenRouter"] = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=openrouter_api_key)

# Configure Ollama (Cloud or Local)
if ollama_url and not ollama_url.startswith("http://localhost") or ollama_api_key != "ollama":
    clients["Ollama"] = OpenAI(base_url=ollama_url, api_key=ollama_api_key)
elif ollama_url:
    clients["Ollama"] = OpenAI(base_url=ollama_url, api_key="ollama")

def _generate_gemini(client, prompt: str, temperature: float) -> str:
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(temperature=temperature)
    )
    return response.text.strip()

def _generate_openai_compatible(client: OpenAI, prompt: str, model: str, temperature: float) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response.choices[0].message.content.strip()

def generate(prompt: str, model: str = "gpt-3.5-turbo", temperature: float = 0.0) -> str:
    """
    Generates a response using the configured LLMs with fallback mechanism.
    """
    for provider in LLM_FALLBACK_ORDER:
        if provider not in clients:
            logger.warning(f"Provider {provider} is not configured. Skipping.")
            continue
            
        try:
            logger.info(f"Attempting to generate using {provider}...")
            if provider == "Gemini":
                return _generate_gemini(clients["Gemini"], prompt, temperature)
            elif provider == "OpenAI":
                # We can use the passed 'model' or a default like gpt-3.5-turbo
                return _generate_openai_compatible(clients["OpenAI"], prompt, model, temperature)
            elif provider == "OpenRouter":
                # OpenRouter requires explicit provider model strings
                return _generate_openai_compatible(clients["OpenRouter"], prompt, "google/gemma-4-26b-a4b-it:free", temperature)
            elif provider == "Ollama":
                # Ollama Cloud model
                return _generate_openai_compatible(clients["Ollama"], prompt, "gpt-oss:120b", temperature)
                
        except Exception as e:
            logger.error(f"Error calling {provider} API: {e}")
            logger.info(f"Falling back to next provider...")
            
    logger.error("All LLM providers failed.")
    return "Error: All LLM providers failed to generate a response."
