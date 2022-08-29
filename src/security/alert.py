from loggingSystem import LoggingSystem


class Alert:
    """Alert class is responsible for alerting the owner with audio feedback"""

    def __init__(self):
        """Construct the alert system"""
        self.__max_alert_volume_level = 100
        self.__min_alert_volume_level = 0
        self.__current_alert_volume_level = 50
        self.__armed = False

    def arm(self):
        """Arms the alert system"""
        self.__armed = True
        LoggingSystem.logInfo("Alert system armed!")

    def disarm(self):
        """Disarms the alert system"""
        self.__armed = False
        LoggingSystem.logInfo("Alert system disarm!")

    def alertFromSpeakers(self):
        """Alert the driver from the inner vehicle speakers"""
        LoggingSystem.logInfo(
            "Alerting from speaker with a volume level of {0}".format(
                self.__current_alert_volume_level
            )
        )

    def alertFromHorn(self):
        """Alert using the vehicle horn"""
        LoggingSystem.logInfo("Alerting from horn")

    def increaseAlertVolumeLevel(self, level: int):
        """Sets the inner vehicle speakers alert volume level. Limited between 0% and 100%"""
        self.__current_alert_volume_level += level

        if self.__current_alert_volume_level > 100:
            self.__current_alert_volume_level = self.__max_alert_volume_level
            return LoggingSystem.logWarrning(
                "Alert volume level cannot be more than {0}%. Volume level was set to {0}%".format(
                    self.__max_alert_volume_level
                )
            )

        LoggingSystem.logInfo(
            """Alert volume level: {0}""".format(self.__current_alert_volume_level)
        )

    def decreaseAlertVolumeLevel(self, level: int):
        """Sets the inner vehicle speakers alert volume level. Limited between 0% and 100%"""
        self.__current_alert_volume_level -= level

        if self.__current_alert_volume_level < 0:
            self.__current_alert_volume_level = self.__min_alert_volume_level
            return LoggingSystem.logWarrning(
                "Alert volume level cannot be less than {0}%. Volume level was set to {0}%".format(
                    self.__min_alert_volume_level
                )
            )

        LoggingSystem.logInfo(
            """Alert volume level: {0}""".format(self.__current_alert_volume_level)
        )

    def getAlertVolumeLevel(self):
        """Gets the inner vehicle speakers alert volume level"""
        LoggingSystem.logInfo(
            "Current alert volume level is {0}%".format(
                self.__current_alert_volume_level
            )
        )
        return self.__current_alert_volume_level
