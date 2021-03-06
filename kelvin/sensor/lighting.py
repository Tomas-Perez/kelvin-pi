import RPi.GPIO as GPIO


class LightReport:
    def __init__(self, is_lighted):
        self.is_lighted = is_lighted

    def __str__(self):
        return 'LightReport(is_lighted={})'.format(self.is_lighted)

    def __repr__(self):
        return self.__str__()


class LightSensor:
    """
    Represents the a light sensor connected to the given pin
    """
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN)

    def next_report(self):
        """
        Get a new light report of the sensor state
        :return: light report
        """
        return LightReport(not bool(GPIO.input(self.pin)))
