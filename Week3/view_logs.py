"""Reads logs from MongoDB, prints a summary and saves a latency/cost chart."""
import os
import certifi
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGODB_URI"), tlsCAFile=certifi.where())
docs = list(client["GenAI_Monitoring"]["api_usage_logs"].find({}, {"_id": 0}))
client.close()

if not docs:
    raise SystemExit("No logs found.")

df = pd.DataFrame(docs)
cols = [c for c in ["timestamp", "model", "status", "retry_attempt", "input_tokens",
                    "output_tokens", "total_tokens", "latency_seconds",
                    "estimated_cost_usd"] if c in df.columns]
print(df[cols].to_string(index=False))
print("\nTotal calls:", len(df))
if "estimated_cost_usd" in df:
    print("Total estimated cost: $", round(df["estimated_cost_usd"].sum(), 7))

ok = df[df["status"] == "success"].reset_index(drop=True)
if not ok.empty:
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    ax[0].bar(ok.index + 1, ok["latency_seconds"]); ax[0].set_title("Latency (s) per successful call")
    ax[1].bar(ok.index + 1, ok["estimated_cost_usd"]); ax[1].set_title("Estimated cost (USD)")
    plt.tight_layout(); plt.savefig("usage_chart.png")
    print("Chart saved as usage_chart.png")
