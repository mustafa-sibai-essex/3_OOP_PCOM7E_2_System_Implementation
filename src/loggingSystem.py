from util.terminalColors import TerminalColors


class LoggingSystem:
    """LoggingSystem class is responsible for handling all logging in the vehicle"""

    __buffer = []
    """This buffer contains all of the vehicle logging messages since last started"""

    def logInfo(message: str):
        """Logs information messages and saves it into the bugger"""
        LoggingSystem.__buffer.append(message)
        print(TerminalColors.HEADER + message + TerminalColors.ENDC)

    def logWarrning(warning: str):
        """Logs warrning messages and saves it into the bugger"""
        LoggingSystem.__buffer.append(warning)
        print(TerminalColors.WARNING + warning + TerminalColors.ENDC)

    def logError(error: str):
        """Logs error messages and saves it into the bugger"""
        LoggingSystem.__buffer.append(error)
        print(TerminalColors.FAIL + error + TerminalColors.ENDC)

    def writeLogToDisk():
        """Writes the logs to disk"""
        print("Writing log to disk")

    def readLogFromDisk():
        """Reads the logs to disk"""
        print("Reading log from disk")
