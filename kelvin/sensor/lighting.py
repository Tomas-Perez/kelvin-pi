import RPi.GPIO as GPIO


class LightReport:
    def __init__(self, is_lighted):
        self.is_lighted = is_lighted


class LightSensor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN)

    def next_report(self):
        return LightReport(not bool(GPIO.input(self.pin)))
