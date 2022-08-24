from loggingSystem import LoggingSystem


class CloudServer:
    def __init__(self):
        self.cloudServerIpAddress = "82.35.12.3"
        self.cloudServerPort = 3243

    def connect(self):
        # assert random.randint(0, 9) > 1, "Failed to connect to GPS Satellite"
        LoggingSystem.logInfo("Connected to Cloud Server")

    def disconnect(self):
        LoggingSystem.logInfo("Disconnected from Cloud Server")

    def uploadStatstics(self):
        LoggingSystem.logInfo("Statstics uploaded to Cloud Server")

    def uploadData(self, data: list[int]):
        LoggingSystem.logInfo("Data uploaded to Cloud Server")

    def streamData(self, buffer: list[int]):
        LoggingSystem.logInfo(
            "Data is being streamed in the background to Cloud Server"
        )
