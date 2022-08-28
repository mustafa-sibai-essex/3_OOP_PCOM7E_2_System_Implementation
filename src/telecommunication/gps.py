from loggingSystem import LoggingSystem


class GPS:
    def __init__(self):
        self.__latitude = 0
        self.__longitude = 0
        self.__altitude = 0
        self.__speed = 0

    def connect(self):
        # assert random.randint(0, 9) > 1, "Failed to connect to GPS Satellite"
        LoggingSystem.logInfo("Connected to GPS")
        pass

    def disconnect(self):
        LoggingSystem.logInfo("Disconnected from GPS")

    def getSpeed(self):
        return self.__speed

    def getLattitude(self):
        return self.__latitude

    def getLongitude(self):
        return self.__longitude

    def getAltitude(self):
        return self.__altitude
