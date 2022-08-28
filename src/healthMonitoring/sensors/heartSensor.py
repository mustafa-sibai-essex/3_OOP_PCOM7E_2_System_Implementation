import random
from healthMonitoring.sensors.healthSensor import HealthSensor
from loggingSystem import LoggingSystem


class HeartSensor(HealthSensor):
    def __init__(self):
        self.__bmp = 0

    def measure(self):
        self.__bmp = random.randint(60, 170)
        LoggingSystem.logInfo("""Heart rate: {0}""".format(self.__bmp))
        return self.__bmp

    def inRange(self):
        if self.__bmp >= 60 and self.__bmp <= 170
            return True
        
        return False
