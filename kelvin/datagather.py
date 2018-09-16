from sensor import \
    GpsSensor, ClimateSensor, LightSensor, DataPoint
from backup import get_collection
from config import \
    GPSD_PORT, DHT_PIN, LDR_PIN, MONGO_PORT, GATHER_TIMEOUT, LOG_FORMAT, GATHER_FILE, LOG_LEVEL
import time
import logging


def poll_and_save_reports():
    logging.basicConfig(format=LOG_FORMAT, filename=GATHER_FILE, level=LOG_LEVEL)

    gps = GpsSensor(port=GPSD_PORT)
    logging.info('reading gpsd on port {}'.format(GPSD_PORT))
    climate = ClimateSensor(pin=DHT_PIN)
    logging.info('reading climate sensor on pin {}'.format(DHT_PIN))
    lighting = LightSensor(pin=LDR_PIN)
    logging.info('reading light sensor on pin {}'.format(LDR_PIN))
    collection = get_collection()
    logging.info('connected to mongodb on port {}'.format_map(MONGO_PORT))

    while True:
        gps_report = gps.next_report()
        climate_report = climate.next_report()
        light_report = lighting.next_report()
        data_point = DataPoint.from_reports(
            gps=gps_report,
            climate=climate_report,
            light=light_report
        )

        if not data_point.is_empty():
            collection.insert_one({'point': data_point.__dict__, 'sent': False})
            logging.info('report stored')
        else:
            logging.warning('no data')

        time.sleep(GATHER_TIMEOUT)


if __name__ == '__main__':
    poll_and_save_reports()
