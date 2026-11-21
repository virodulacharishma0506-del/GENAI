"""Gemini API Monitoring System
Logs tokens, latency, estimated cost, status and retry attempt of every
Gemini API call to MongoDB Atlas."""
import os
import time
from datetime import datetime, timezone

import certifi
from dotenv import load_dotenv
from google import genai
from google.genai import errors
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MONGODB_URI = os.getenv("MONGODB_URI")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

# Pricing in USD per 1 million tokens (update to match your model's price list)
INPUT_PRICE_PER_M = 0.30
OUTPUT_PRICE_PER_M = 2.50

MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds
RETRYABLE_CODES = {429, 500, 503, 504}

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing in .env file")
if not MONGODB_URI:
    raise ValueError("MONGODB_URI is missing in .env file")

gemini = genai.Client(api_key=GEMINI_API_KEY)
mongo = MongoClient(
    MONGODB_URI,
    server_api=ServerApi("1"),
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=15000,
)
mongo.admin.command("ping")
collection = mongo["GenAI_Monitoring"]["api_usage_logs"]
print("MongoDB connected successfully!")
print("Database: GenAI_Monitoring")
print("Collection: api_usage_logs")


def estimate_cost(input_tokens, output_tokens):
    return (input_tokens * INPUT_PRICE_PER_M + output_tokens * OUTPUT_PRICE_PER_M) / 1_000_000


def log_call(prompt, attempt, status, latency, in_tok=0, out_tok=0,
             think_tok=0, total_tok=0, error=None):
    # Thinking tokens are billed as output tokens
    cost = estimate_cost(in_tok, out_tok + think_tok)
    collection.insert_one({
        "timestamp": datetime.now(timezone.utc),
        "prompt": prompt,
        "model": MODEL_NAME,
        "input_tokens": in_tok,
        "output_tokens": out_tok,
        "thinking_tokens": think_tok,
        "total_tokens": total_tok,
        "latency_seconds": round(latency, 3),
        "estimated_cost_usd": round(cost, 7),
        "status": status,
        "retry_attempt": attempt,
        "error": error,
    })
    print(f"Attempt {attempt}: Log saved to MongoDB.")
    return cost


def ask_gemini(prompt):
    for attempt in range(1, MAX_RETRIES + 1):
        start = time.time()
        try:
            response = gemini.models.generate_content(model=MODEL_NAME, contents=prompt)
            latency = time.time() - start
            u = response.usage_metadata
            in_tok = u.prompt_token_count or 0
            out_tok = u.candidates_token_count or 0
            think_tok = getattr(u, "thoughts_token_count", 0) or 0
            total_tok = u.total_token_count or (in_tok + out_tok + think_tok)
            cost = log_call(prompt, attempt, "success", latency,
                            in_tok, out_tok, think_tok, total_tok)

            print("\nGemini Response:")
            print(response.text)
            print("\nUsage Details")
            print("-" * 30)
            print(f"Input tokens: {in_tok}")
            print(f"Output tokens: {out_tok}")
            print(f"Thinking tokens: {think_tok}")
            print(f"Total tokens: {total_tok}")
            print(f"Latency: {latency:.3f} seconds")
            print(f"Estimated cost: $ {cost:.7f}")
            return
        except errors.APIError as e:
            latency = time.time() - start
            print(f"Gemini API error: {e.code} {e.status}. {e.message}")
            log_call(prompt, attempt, f"error_{e.code}", latency, error=str(e))
            if e.code in RETRYABLE_CODES and attempt < MAX_RETRIES:
                print(f"Retrying after {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            else:
                print("Request failed. Not retrying.")
                return


def main():
    print("\nGEMINI API MONITORING SYSTEM")
    print("=" * 40)
    try:
        while True:
            prompt = input("\nEnter your prompt (or type exit): ").strip()
            if prompt.lower() == "exit":
                break
            if prompt:
                ask_gemini(prompt)
    except KeyboardInterrupt:
        pass
    finally:
        mongo.close()
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
