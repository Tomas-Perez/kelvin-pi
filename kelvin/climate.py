import Adafruit_DHT
from threading import Thread
from collections import namedtuple

DTH_MODEL = 11
ClimateReport = namedtuple('ClimateReport', ['humidity', 'temperature'])


class ClimatePoller(Thread):
    def __init__(self, pin):
        Thread.__init__(self)
        self.pin = pin
        self.current_report = None

    def run(self):
        while True:
            self.current_report = Adafruit_DHT.read_retry(DTH_MODEL, self.pin)


class ClimateSensor:
    def __init__(self, pin=4):
        self.poller = ClimatePoller(pin)
        self.poller.start()

    def next_report(self):
        if self.poller.current_report:
            humidity, temperature = self.poller.current_report
            return ClimateReport(
                temperature=temperature,
                humidity=humidity
            )
        else:
            return ClimateReport(None, None)
