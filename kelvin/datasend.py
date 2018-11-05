from getmac import get_mac_address
from backup import get_collection
from config import \
    MONGO_PORT, QUEUE_URL, SEND_TIMEOUT, SEND_FILE, LOG_LEVEL, LOG_FORMAT
from transmit import SQSTransmit
import time
import logging


def publish_data():
    """
    Send new report to the kelvin SQS Queue
    """
    logging.basicConfig(format=LOG_FORMAT, filename=SEND_FILE, level=LOG_LEVEL)
    mac = get_mac_address(interface="eth0")
    collection = get_collection()
    logging.info('connected to mongodb on port {}'.format(MONGO_PORT))
    queue = SQSTransmit(QUEUE_URL)
    logging.info('sending to queue on {}'.format(QUEUE_URL))

    while True:
        counter = 0

        for report in collection.find({'sent': False}):
            point = report['point']
            report_id = report['_id']
            response = queue.send_dict_as_json({'point': point, 'mac': mac})
            if response:
                counter += 1
                collection.update_one({'_id': report_id}, {'$set': {'sent': True}})
            else:
                logging.warning('no connection, retrying in {} seconds'.format(SEND_TIMEOUT))
                break

        if counter > 0:
            logging.info('sent {} messages'.format(counter))

        time.sleep(SEND_TIMEOUT)


if __name__ == '__main__':
    publish_data()
