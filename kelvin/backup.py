from pymongo import MongoClient
from config import DB, COLLECTION, MONGO_PORT


def get_collection():
    """
    Helper function to get mongo point collection
    """
    client = MongoClient('localhost', MONGO_PORT)
    db = client[DB]
    return db[COLLECTION]
