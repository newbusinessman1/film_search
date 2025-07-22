from datetime import datetime as dt
from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB, GROUP, FULL_NAME

_col = MongoClient(MONGO_URI)[MONGO_DB][f"final_project_{GROUP}_{FULL_NAME}"]

def log_query(qtype: str, params: dict):
    _col.insert_one({
        "ts": dt.utcnow(),
        "type": qtype,     # 'keyword' | 'genre_year'
        "params": params
    })