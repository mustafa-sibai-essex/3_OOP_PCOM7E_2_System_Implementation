from util.terminalColors import TerminalColors


class LoggingSystem:
    __buffer = []

    def logInfo(message: str):
        LoggingSystem.__buffer.append(message)
        print(TerminalColors.HEADER + message + TerminalColors.ENDC)

    def logWarrning(warning: str):
        LoggingSystem.__buffer.append(warning)
        print(TerminalColors.WARNING + warning + TerminalColors.ENDC)

    def logError(error: str):
        LoggingSystem.__buffer.append(error)
        print(TerminalColors.FAIL + error + TerminalColors.ENDC)

    def writeLogToDisk():
        print("Writing log to disk")

    def readLogFromDisk():
        print("Reading log from disk")
