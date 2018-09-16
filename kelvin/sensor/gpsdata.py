from threading import Thread
import gps

REPORT_KEYS = ['lat', 'lon', 'speed', 'time']


class GpsReport:
    def __init__(self, lat, lon, speed, time):
        self.lat = lat
        self.lon = lon
        self.speed = speed
        self.time = time

    def __str__(self):
        return 'GpsReport(lat={}, lon={}, speed={}Km/h, time={})'.format(
            self.lat, self.lon, self.speed, self.time
        )

    def __repr__(self):
        return self.__str__()


class GpsPoller(Thread):
    def __init__(self, port):
        Thread.__init__(self)
        self.session = gps.gps('localhost', port)
        self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
        self.current_report = None

    def run(self):
        try:
            while True:
                report = self.session.next()
                if report['class'] == 'TPV':
                    self.current_report = report
        except StopIteration:
            self.session = None
            print('GPSD has terminated')


class GpsSensor:
    def __init__(self, port):
        self.poller = GpsPoller(port)
        self.poller.start()

    def next_report(self):
        temp_dict = dict.fromkeys(REPORT_KEYS)
        current_report = self.poller.current_report
        if current_report:
            for key in REPORT_KEYS:
                try:
                    temp_dict[key] = current_report[key]
                except KeyError:
                    pass
            return GpsReport(
                lat=temp_dict['lat'],
                lon=temp_dict['lon'],
                speed=temp_dict['speed'],
                time=temp_dict['time']
            )
        else:
            return GpsReport(None, None, None, None)
