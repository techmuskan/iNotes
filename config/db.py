# config/db.py
from pymongo import MongoClient  # ✅ Correct import

# MongoDB connection string
MONGO_URI = "mongodb+srv://techmuskan:qyqEURTR3k3lTtAJ@cluster0.baz5x.mongodb.net/"

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Select database and collection
db = client["notes"]          # Database name
collection = db["notes"]      # Collection name

print("✅ Connected to MongoDB")
