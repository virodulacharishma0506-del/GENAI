
import os
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Load environment variables
load_dotenv()

# Read MongoDB connection string
MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI is missing in .env file")

print("Connecting to MongoDB Atlas...")

# Create MongoDB connection
client = MongoClient(
    MONGODB_URI,
    server_api=ServerApi("1"),
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=15000
)

try:
    # Test connection
    client.admin.command("ping")
    print("MongoDB Connected Successfully!")

    # Create database
    db = client["GenAI_Monitoring"]

    # Create collection
    collection = db["api_usage_logs"]

    # Insert sample document
    result = collection.insert_one({
        "message": "MongoDB connection successful",
        "status": "success"
    })

    print("Database:", db.name)
    print("Collection:", collection.name)
    print("Inserted ID:", result.inserted_id)

except Exception as error:
    print("MongoDB Connection Failed!")
    print("Error:", error)

finally:
    client.close()
