from threading import Thread
import gps


class GpsReport:
    def __init__(self, lat, lon, speed, time):
        self.lat = lat
        self.lon = lon
        self.speed = speed
        self.time = time


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
        if self.poller.current_report:
            return GpsReport(
                lat=self.poller.current_report.lat,
                lon=self.poller.current_report.lon,
                speed=self.poller.current_report.speed,
                time=self.poller.current_report.time
            )
        else:
            return GpsReport(None, None, None, None)
