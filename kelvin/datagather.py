from sensor.gpsdata import GpsSensor
from sensor.climate import ClimateSensor
from sensor.lighting import LightSensor
from sensor.datapoint import DataPoint
from backup import get_collection
from constants import MONGO_PORT
import time

GPSD_PORT = '2947'
DTH_PIN = 4
LDR_PIN = 17
GATHER_TIMEOUT = 2


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
        collection.insert_one({'point': data_point, 'sent': False})
        time.sleep(GATHER_TIMEOUT)


if __name__ == '__main__':
    poll_and_save_reports()
