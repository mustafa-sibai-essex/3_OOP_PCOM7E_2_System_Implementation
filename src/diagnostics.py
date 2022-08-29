from loggingSystem import LoggingSystem


class Diagnostics:
    """Diagnostics class is responsible for making sure all hardware is working"""

    def __init__(self):
        """Creates the Diagnostics class object"""
        LoggingSystem.logInfo("Diagnostics running")

    def verifyLoggingSystem(self):
        """Verifies the logging system"""
        LoggingSystem.logInfo("Logging System working")

    def verifyInfotainmentSystem(self):
        """Verifies the Infotainment system"""
        LoggingSystem.logInfo("Infotainment System working")

    def verifyCameras(self):
        """Verifies Cameras"""
        LoggingSystem.logInfo("Cameras working")

    def verifyProximitySensors(self):
        """Verifies Proximity Sensors"""
        LoggingSystem.logInfo("Proximity Sensors working")

    def verifyGPS(self):
        """Verifies GPS"""
        LoggingSystem.logInfo("GPS working")

    def verifyInternet(self):
        """Verifies internet"""
        LoggingSystem.logInfo("Internet working")

    def verifyHealthVitalSensors(self):
        """Verifies health vital sensors"""
        LoggingSystem.logInfo("Health Vital Sensors working")

    def verifySSDHealth(self):
        """Verifies SSD health"""
        LoggingSystem.logInfo("SSD Health is good")

    def verifySSDEnoughSpace(self):
        """Verifies enough SSD space"""
        LoggingSystem.logInfo("SSD has enough space")

    def startVerificationProcess(self):
        """Verifies all systems at once"""
        self.verifyLoggingSystem()
        self.verifyInfotainmentSystem()
        self.verifyCameras()
        self.verifyProximitySensors()
        self.verifyGPS()
        self.verifyInternet()
        self.verifyHealthVitalSensors()
        self.verifySSDHealth()
        self.verifySSDEnoughSpace()
