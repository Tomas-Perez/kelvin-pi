from getmac import get_mac_address
from backup import get_collection
from constants import \
    MONGO_PORT, QUEUE_URL, SEND_TIMEOUT
from transmit import SQSTransmit
import time


def publish_data():
    mac = get_mac_address(interface="eth0")
    collection = get_collection(MONGO_PORT)
    queue = SQSTransmit(QUEUE_URL)
    while True:
        counter = 0

        for report in collection.find({'sent': False}):
            point = report['point']
            report_id = report['_id']
            response = queue.send_dict_as_json({'point': point, 'mac': mac})
            if response:
                print('message sent')
                counter += 1
                collection.update_one({'_id': report_id}, {'$set': {'sent': True}})
            else:
                print('no connection, retrying in {} seconds'.format(SEND_TIMEOUT))
                break

        if counter > 0:
            print('sent {} messages'.format(counter))

        time.sleep(SEND_TIMEOUT)


if __name__ == '__main__':
    publish_data()
