class LoggingSystem:
    __buffer = []

    def logInfo(message: str):
        LoggingSystem.__buffer.append(message)
        print(message)

    def logWarrning(warning: str):
        LoggingSystem.__buffer.append(warning)
        print(warning)

    def logError(error: str):
        LoggingSystem.__buffer.append(error)
        print(error)

    def writeLogToDisk():
        print("Writing log to disk")

    def readLogFromDisk():
        print("Reading log from disk")
