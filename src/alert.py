class Alert:
    def __init__(self):
        self._alertVolumeLevel = 50
        self.armed = False

    def arm(self):
        self.armed = True
        print("Alert system armed!")

    def disarm(self):
        self.armed = False
        print("Alert system disarm!")

    def alertFromSpeakers(self):
        print("Alerting from speaker")

    def alertFromHorn(self):
        print("Alerting from horn")

    def setAlertVolumeLevel(self, level: int):
        self._alertVolumeLevel = level

        if self._alertVolumeLevel > 100:
            self._alertVolumeLevel = min(self._alertVolumeLevel, 100)
            print(
                "Alert volume level cannot be more than 100%. Volume level was set to 100%"
            )
        elif self._alertVolumeLevel < 0:
            self._alertVolumeLevel = max(self._alertVolumeLevel, 0)
            print(
                "Alert volume level cannot be less than 0%. Volume level was set to 0%"
            )

        print(self._alertVolumeLevel)

    def getAlertVolumeLevel(self):
        return self._alertVolumeLevel
