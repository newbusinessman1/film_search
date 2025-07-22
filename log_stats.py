from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB, GROUP, FULL_NAME

_col = MongoClient(MONGO_URI)[MONGO_DB][f"final_project_{GROUP}_{FULL_NAME}"]

def top_queries(limit=5):
    pipe = [
        {"$group": {"_id": "$params", "cnt": {"$sum": 1}}},
        {"$sort": {"cnt": -1}},
        {"$limit": limit}
    ]
    return list(_col.aggregate(pipe))

def recent_unique(limit=5):
    pipe = [
        {"$sort": {"ts": -1}},
        {"$group": {"_id": "$params", "ts": {"$first": "$ts"}}},
        {"$limit": limit}
    ]
    return list(_col.aggregate(pipe))