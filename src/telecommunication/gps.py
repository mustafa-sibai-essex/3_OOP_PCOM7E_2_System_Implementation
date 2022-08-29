import random
from loggingSystem import LoggingSystem
from telecommunication.connectionState import ConnectionState
from telecommunication.satellite import Satellite


class GPS:
    """GPS class is responsible connecting, disconnecting and getting cruical information like position, speed and altitude"""

    def __init__(self, satellite: Satellite):
        """Creates the GPS class object"""
        self.__satellite = satellite
        self.__connection_state = ConnectionState.NOT_CONNECTED
        self.__latitude = 0
        self.__longitude = 0
        self.__altitude = 0
        self.__speed = 0

    def connect(self):
        """Connects to GPS as long as we are connected to the satellite"""
        if self.__satellite.getState() != ConnectionState.CONNECTED:
            return LoggingSystem.logError(
                "Cannot connect to GPS before connecting to satellite"
            )

        if self.__connection_state == ConnectionState.CONNECTED:
            return LoggingSystem.logWarrning("Already connected to GPS")

        self.__connection_state = ConnectionState.CONNECTING
        LoggingSystem.logInfo("Connecting to GPS")

        if random.randint(0, 100) > 10:
            self.__connection_state = ConnectionState.CONNECTED
            LoggingSystem.logInfo("Connected to GPS")
        else:
            LoggingSystem.logError("Failed to connect to GPS")

    def disconnect(self):
        """Disconnects from the GPS as long as we were connected to the satellite previously"""

        if self.__satellite.getState() != ConnectionState.CONNECTED:
            return LoggingSystem.logError(
                "Cannot disconnect from GPS before connecting to satellite"
            )

        if self.__connection_state != ConnectionState.CONNECTED:
            return LoggingSystem.logWarrning(
                "Cannot disconnect from GPS before connecting to it"
            )

        if self.__connection_state == ConnectionState.DISCONNECTED:
            return LoggingSystem.logWarrning("Already disconnected from GPS")

        self.__connection_state = ConnectionState.DISCONNECTING
        LoggingSystem.logInfo("Disconnecting from GPS")

        if random.randint(0, 100) > 10:
            self.__connection_state = ConnectionState.DISCONNECTED
            LoggingSystem.logInfo("Disconnected to GPS")
        else:
            LoggingSystem.logError("Failed to disconnect from GPS")

    def getState(self):
        """Returns the current state of GPS"""

        LoggingSystem.logInfo(
            "GPS state is: {0}".format(self.__connection_state)
        )
        return self.__connection_state

    def getSpeed(self):
        """Returns the vehicle current speed as long as we are connected to the satellite"""
        if self.__connection_state != ConnectionState.CONNECTED:
            self.__speed = 0
            LoggingSystem.logWarrning("Cannot get speed if not connected to GPS")

        LoggingSystem.logInfo("GPS speed is: {0}".format(self.__speed))
        return self.__speed

    def getLattitude(self):
        """Returns the vehicle current lattitude as long as we are connected to the satellite"""
        if self.__connection_state != ConnectionState.CONNECTED:
            self.__latitude = 0
            LoggingSystem.logWarrning("Cannot get latitude if not connected to GPS")

        LoggingSystem.logInfo("GPS latitude is: {0}".format(self.__latitude))
        return self.__latitude

    def getLongitude(self):
        """Returns the vehicle current longitude as long as we are connected to the satellite"""
        if self.__connection_state != ConnectionState.CONNECTED:
            self.__longitude = 0
            LoggingSystem.logWarrning("Cannot get longitude if not connected to GPS")

        LoggingSystem.logInfo("GPS longitude is: {0}".format(self.__longitude))
        return self.__longitude

    def getAltitude(self):
        """Returns the vehicle current altitude as long as we are connected to the satellite"""
        if self.__connection_state != ConnectionState.CONNECTED:
            self.__altitude = 0
            LoggingSystem.logWarrning("Cannot get altitude if not connected to GPS")

        LoggingSystem.logInfo("GPS altitude is: {0}".format(self.__altitude))
        return self.__altitude
