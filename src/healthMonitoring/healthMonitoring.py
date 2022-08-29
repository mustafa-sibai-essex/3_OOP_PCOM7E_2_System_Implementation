from security.alert import Alert
from infotainment.infotainment import Infotainment


class HealthMonitoring:
    def __init__(self, infotainment: Infotainment):
        self.__health_sensors = []
        self.__infotainment = infotainment
        self.__alert = Alert()

    def isDriverAlert(self):
        pass
    