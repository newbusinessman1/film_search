from pymongo.errors import ConnectionFailure
from datetime import datetime as dt, timedelta

from pymongo import MongoClient
import os
from dotenv import load_dotenv
from pymongo import MongoClient, errors
import sys

load_dotenv()


MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
GROUP = os.getenv("GROUP")
FULL_NAME = os.getenv("FULL_NAME")

_collection_name = f"final_project_{GROUP}_{FULL_NAME}"

try:
    _col = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)[MONGO_DB][_collection_name]
except errors.InvalidURI:
    print("❌ [MongoDB] Not valid URI — check MONGO_URI in .env")
    sys.exit(1)
except errors.ConfigurationError as e:
    print(f"❌ [MongoDB] Config error: {e}")
    sys.exit(1)

def log_query(qtype: str, params: dict):
    try:
        # delete everything older than 30 days
        _col.delete_many({"ts": {"$lt": dt.utcnow() - timedelta(days=30)}})

        # insert new log
        _col.insert_one({
            "ts": dt.utcnow(),
            "type": qtype,     # 'keyword' | 'genre_year'
            "params": params
        })
    except ConnectionFailure:
        print("[MongoDB] ❌ Error connecting — log not saved")