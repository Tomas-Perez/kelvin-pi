from sensor import \
    GpsSensor, ClimateSensor, LightSensor, DataPoint
from backup import get_collection
from constants import \
    GPSD_PORT, DTH_PIN, LDR_PIN, MONGO_PORT, GATHER_TIMEOUT
import time
import json


def poll_and_save_reports():
    gps = GpsSensor(port=GPSD_PORT)
    climate = ClimateSensor(pin=DTH_PIN)
    lighting = LightSensor(pin=LDR_PIN)
    collection = get_collection(port=MONGO_PORT)

    while True:
        gps_report = gps.next_report()
        climate_report = climate.next_report()
        light_report = lighting.next_report()
        data_point = DataPoint.from_reports(
            gps=gps_report,
            climate=climate_report,
            light=light_report
        )
        print('got {}'.format(data_point))
        if not data_point.is_empty():
            collection.insert_one({'point': data_point.__dict__, 'sent': False})
            print('stored')

        time.sleep(GATHER_TIMEOUT)


if __name__ == '__main__':
    poll_and_save_reports()
