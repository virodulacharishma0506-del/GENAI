
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv(Path(__file__).resolve().parent / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key missing from .env")

# Connect to Gemini
client = genai.Client(api_key=api_key)

print("\nAVAILABLE GEMINI MODELS")
print("=" * 50)

try:
    for model in client.models.list():
        actions = getattr(model, "supported_actions", None) or []

        if "generateContent" in actions:
            print(model.name)

except Exception as error:
    print("Error while fetching models:", error)

print("=" * 50)
