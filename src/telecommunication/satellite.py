import random
from telecommunication.connectionState import ConnectionState
from ..loggingSystem import LoggingSystem


class Satellite:
    """Satellite class is responsible for connecting and disconnecting from the satellite"""

    def __init__(self):
        """Creates the satellite class object and sets up the connection state"""
        self.__connection_state = ConnectionState.NOT_CONNECTED

    def connect(self):
        """Connects to the satellite"""

        if self.__connection_state == ConnectionState.CONNECTED:
            return LoggingSystem.logWarrning("Already connected to satellite")

        self.__connection_state = ConnectionState.CONNECTING
        LoggingSystem.logInfo("Connecting to satellite")

        if random.randint(0, 100) > 10:
            self.__connection_state = ConnectionState.CONNECTED
            LoggingSystem.logInfo("Connected to satellite!")
        else:
            self.__connection_state = ConnectionState.FAILED_TO_CONNECT
            LoggingSystem.logError("Failed to connect to satellite!")

    def disconnect(self):
        """Disconnects from the satellite"""
        if self.__connection_state == ConnectionState.DISCONNECTED:
            return LoggingSystem.logWarrning("Already disconnected from satellite")

        self.__connection_state = ConnectionState.DISCONNECTING

        if random.randint(0, 100) > 10:
            self.__connection_state = ConnectionState.DISCONNECTED
            LoggingSystem.logInfo("Disconnected from satellite!")
        else:
            self.__connection_state = ConnectionState.FAILED_TO_DISCONNECT
            LoggingSystem.logError("Failed to disconnect from satellite!")

    def getState(self):
        """Returns the current state of the satellite"""
        return self.__connection_state
