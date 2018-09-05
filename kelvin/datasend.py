from getmac import get_mac_address
from backup import get_collection
from constants import MONGO_PORT
from transmit import SQSTransmit
import time

QUEUE_URL = 'https://sqs.us-east-2.amazonaws.com/011354114873/kelvin'
SEND_TIMEOUT = 10


def publish_data():
    mac = get_mac_address(interface="eth0")
    collection = get_collection(MONGO_PORT)
    queue = SQSTransmit(QUEUE_URL)
    while True:
        for report in collection.find({'sent': False}):
            point = report['point']
            report_id = report['_id']
            queue.send_message({'point': point, 'mac': mac})
            collection.update_one({'_id': report_id}, {'$set': {'sent': True}})
        time.sleep(SEND_TIMEOUT)


if __name__ == '__main__':
    publish_data()
