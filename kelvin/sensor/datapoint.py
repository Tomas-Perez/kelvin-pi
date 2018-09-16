import json

from sensor.climate import ClimateReport
from sensor.gpsdata import GpsReport
from sensor.lighting import LightReport


class DataPoint:
    def __init__(self, coordinates, time, speed, temperature, humidity, is_lighted):
        self.coordinates = coordinates
        self.time = time
        self.speed = speed
        self.temperature = temperature
        self.humidity = humidity
        self.is_lighted = is_lighted

    @staticmethod
    def from_reports(gps, climate, light):
        return DataPoint(
            coordinates={
                'lat': gps.lat,
                'lon': gps.lon
            },
            time=gps.time,
            speed=gps.speed,
            humidity=climate.humidity,
            temperature=climate.temperature,
            is_lighted=light.is_lighted
        )

    def is_empty(self):
        return self.coordinates['lat'] is None and \
               self.coordinates['lon'] is None and \
               self.time is None and \
               self.speed is None and \
               self.humidity is None and \
               self.temperature is None

    def __str__(self):
        return 'DataPoint(coordinates={}, time={}, speed={}Km/h, humidity={}%, temperature={}C, is_lighted={})'.format(
            self.coordinates, self.time, self.speed, self.humidity, self.temperature, self.is_lighted
        )

    def __repr__(self):
        return self.__str__()
