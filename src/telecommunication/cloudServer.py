import random
from loggingSystem import LoggingSystem
from telecommunication.connectionState import ConnectionState
from telecommunication.satellite import Satellite


class CloudServer:
    """CloudServer class is responsible for connecting, disconnecting, and upload data to the cloud server"""

    def __init__(self, satellite: Satellite):
        """Creates the CloudServer class object and sets up the connection state"""
        self.__satellite = satellite
        self.__connection_state = ConnectionState.DISCONNECTED
        self.__cloudServerIpAddress = "82.35.12.3"
        self.__cloudServerPort = 3243

    def connect(self):
        """Connects to the cloud server as long as we are connected to the Satellite"""
        if self.__satellite.getState() != ConnectionState.CONNECTED:
            return LoggingSystem.logError(
                "Cannot connect to cloud server before connecting to satellite"
            )

        if self.__connection_state == ConnectionState.CONNECTED:
            return LoggingSystem.logWarrning("Already connected to cloud server")

        self.__connection_state = ConnectionState.CONNECTING
        LoggingSystem.logInfo("Connecting to cloud server")

        if random.randint(0, 100) > 10:
            self.__connection_state = ConnectionState.CONNECTED
            LoggingSystem.logInfo("Connected to cloud server!")
        else:
            self.__connection_state = ConnectionState.FAILED_TO_CONNECT
            LoggingSystem.logError("Failed to connect to cloud server!")

    def disconnect(self):
        """Disconnect from the cloud server as long as we were connected previously"""
        if self.__connection_state == ConnectionState.CONNECTED:

            self.__connection_state = ConnectionState.DISCONNECTING
            LoggingSystem.logInfo("Disconnecting from cloud server")

            if random.randint(0, 100) > 10:
                self.__connection_state = ConnectionState.DISCONNECTED
                LoggingSystem.logInfo("Disconnected from cloud server!")
            else:
                self.__connection_state = ConnectionState.FAILED_TO_DISCONNECT
                LoggingSystem.logError("Failed to disconnect from cloud server!")
        else:
            LoggingSystem.logWarrning(
                "Cannot disconnect from cloud server before connecting to it"
            )

    def uploadStatstics(self):
        """Uploads vehicle statstics as long we are connected to the cloud server"""
        if self.__connection_state == ConnectionState.CONNECTED:
            if random.randint(0, 100) > 10:
                LoggingSystem.logInfo("Statstics uploaded to Cloud Server")
            else:
                LoggingSystem.logError("Failed to uploaded statstics to cloud server!")
        else:
            LoggingSystem.logWarrning(
                "Cannot upload statstics to cloud server if not connected to it"
            )

    def uploadData(self, data: list[int]):
        """Uploads data to cloud server as long as we are connected to it"""
        if self.__connection_state == ConnectionState.CONNECTED:
            if random.randint(0, 100) > 10:
                LoggingSystem.logInfo("Data uploaded to cloud server")
            else:
                LoggingSystem.logError("Failed to uploaded data to cloud server!")
        else:
            LoggingSystem.logWarrning(
                "Cannot upload data to cloud server if not connected to it"
            )

    def streamData(self, buffer: list[int]):
        """Streams data continually to cloud server as long as we are connected to it"""
        if self.__connection_state == ConnectionState.CONNECTED:
            if random.randint(0, 100) > 10:
                LoggingSystem.logInfo(
                    "Data is being streamed in the background to cloud server"
                )
            else:
                LoggingSystem.logError("Failed to stream data to cloud server!")
        else:
            LoggingSystem.logWarrning(
                "Cannot stream data to cloud server if not connected to it"
            )
