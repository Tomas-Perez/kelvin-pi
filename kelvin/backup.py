from pymongo import MongoClient


def get_collection(port):
    client = MongoClient('localhost', port)
    db = client.kelvin
    return db.points
