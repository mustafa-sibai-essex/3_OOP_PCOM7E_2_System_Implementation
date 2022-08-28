from loggingSystem import LoggingSystem


class Alert:
    def __init__(self):
        """Construct the alert system"""
        self.__alertVolumeLevel = 50
        self.armed = False

    def arm(self):
        """Arms the alert system"""
        self.armed = True
        LoggingSystem.logInfo("Alert system armed!")

    def disarm(self):
        """Disarms the alert system"""
        self.armed = False
        LoggingSystem.logInfo("Alert system disarm!")

    def alertFromSpeakers(self):
        """Alert the driver from the inner vehicle speakers"""
        LoggingSystem.logInfo("Alerting from speaker")

    def alertFromHorn(self):
        """Alert using the vehicle horn"""
        LoggingSystem.logInfo("Alerting from horn")

    def setAlertVolumeLevel(self, level: int):
        """Sets the inner vehicle speakers alert volume level. Limited between 0% and 100%"""
        self.__alertVolumeLevel = level

        if self.__alertVolumeLevel > 100:
            self.__alertVolumeLevel = min(self.__alertVolumeLevel, 100)
            LoggingSystem.logWarrning(
                "Alert volume level cannot be more than 100%. Volume level was set to 100%"
            )
        elif self.__alertVolumeLevel < 0:
            self.__alertVolumeLevel = max(self.__alertVolumeLevel, 0)
            LoggingSystem.logWarrning(
                "Alert volume level cannot be less than 0%. Volume level was set to 0%"
            )

        LoggingSystem.logInfo(
            """Alert volume level: {0}""".format(self.__alertVolumeLevel)
        )

    def getAlertVolumeLevel(self):
        """Gets the inner vehicle speakers alert volume level"""
        return self.__alertVolumeLevel
