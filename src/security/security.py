from ..alert import Alert


class Security:
    def __init__(self):
        self.alert = Alert()

    def startDetectingBreakIn(self):
        pass

    def stopDetectingBreakIn(self):
        pass

    def sendGPSLocationToOwnerViaSMS(self):
        pass

    def sendBreakInNotificationToOwnerViaSMS(self):
        pass

    def sendBreakInNotificationToOwnerViaEmail(self):
        pass

    def streamRecordingToCloud(self):
        pass
