import RPi.GPIO as GPIO
from collections import namedtuple

LightReport = namedtuple('LightReport', ['is_lighted'])


class LightSensor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN)

    def next_report(self):
        return LightReport(not bool(GPIO.input(self.pin)))
