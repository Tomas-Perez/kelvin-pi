from pymongo import MongoClient
from constants import MONGO_PORT
import json


def get_collection(port):
    client = MongoClient('localhost', port)
    db = client.kelvin
    return db.points


if __name__ == '__main__':
    collection = get_collection(MONGO_PORT)

    # collection.insert_one({
    #     'hello': 'am i json?',
    #     'point': DataPoint({'lat': 2, 'lon': 3}, 4, 5, 6, 2, True).__dict__
    # })
    #
    # for something in collection.find():
    #     print(something['hello'])

