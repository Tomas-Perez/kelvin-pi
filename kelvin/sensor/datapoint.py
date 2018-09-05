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


class DictEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


if __name__ == '__main__':
    climate_report = ClimateReport(23, 23)
    report = DataPoint.from_reports(GpsReport(23, 43, 324, 453), climate_report, LightReport(True))
    print(json.dumps(report, cls=DictEncoder))
