# from getmac import get_mac_address
# eth_mac = get_mac_address(interface="eth0")

from gpsdata import GpsSensor
from climate import ClimateSensor
from lighting import LightSensor
import time

GPSD_PORT = '2947'
DTH_PIN = 4
LDR_PIN = 17


if __name__ == '__main__':
    gps = GpsSensor(port=GPSD_PORT)
    climate = ClimateSensor(pin=DTH_PIN)
    lighting = LightSensor(pin=LDR_PIN)

    while True:
        gps_report = gps.next_report()
        print(gps_report)
        climate_report = climate.next_report()
        print(climate_report)
        lighting_report = lighting.next_report()
        print(lighting_report)
        time.sleep(2)
