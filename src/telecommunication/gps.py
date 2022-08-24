from loggingSystem import LoggingSystem


class GPS:
    def __init__(self):
        self._latitude = 0
        self._longitude = 0
        self._altitude = 0
        self._speed = 0

    def connect(self):
        # assert random.randint(0, 9) > 1, "Failed to connect to GPS Satellite"
        LoggingSystem.logInfo("Connected to GPS")
        pass

    def disconnect(self):
        LoggingSystem.logInfo("Disconnected from GPS")

    def getSpeed(self):
        return self._speed

    def getLattitude(self):
        return self._latitude

    def getLongitude(self):
        return self._longitude

    def getAltitude(self):
        return self._altitude
