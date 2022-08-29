from security.alert import Alert
from loggingSystem import LoggingSystem
from security.entrances.entranceManager import EntranceManager
from telecommunication.connectionState import ConnectionState
from telecommunication.email.email import Email
from telecommunication.sms.sms import SMS
from telecommunication.telecommunication import Telecommunication


class Security:
    """Security class is responsible for all security systems in the vehicle such as locking and unlocking entrances and detecting any breakins"""

    def __init__(self, telecommunication: Telecommunication):
        self.__telecommunication = telecommunication
        self.__entrance_manager = EntranceManager()
        self.__alert = Alert()

    def getEntranceManager(self):
        """Returns entrance manager object"""
        return self.__entrance_manager

    def getAlert(self):
        """Returns alert object"""
        return self.__alert

    def startDetectingBreakIn(self):
        """Starts detecting break in"""
        LoggingSystem.logInfo("Breakin detection is on")

    def stopDetectingBreakIn(self):
        """Stops detecting break in"""
        LoggingSystem.logInfo("Breakin detection is off")

    def sendGPSLocationToOwnerViaSMS(self):
        """Sends the vehicle owner the vehicle current GPS location"""
        if self.__telecommunication.getGPS().getState() != ConnectionState.CONNECTED:
            return LoggingSystem.logError(
                "Cannot send GPS location when not connected to GPS"
            )

        self.__telecommunication.getSMSManager().sendSMS(
            SMS(
                self.__telecommunication.getPhone().getPhoneBook().getOwnerContact(),
                "Vehicle GPS location is {0},{1},{2}".format(
                    self.__telecommunication.getGPS().getLongitude(),
                    self.__telecommunication.getGPS().getLattitude(),
                    self.__telecommunication.getGPS().getAltitude(),
                ),
            )
        )

    def sendBreakInNotificationToOwnerViaSMS(self):
        """Sends a breakin alert to vehicle owner by SMS"""
        self.__telecommunication.getSMSManager().sendSMS(
            SMS(
                self.__telecommunication.getPhone()
                .getPhoneBook()
                .getOwnerContact()
                .getPhoneNumber(),
                "Breakin Detected!",
            )
        )

    def sendBreakInNotificationToOwnerViaEmail(self):
        """Sends a breakin alert to vehicle owner by Email"""
        self.__telecommunication.getEmailManager().sendEmail(
            Email(
                "vehicle.email@gmail.com",
                self.__telecommunication.getPhone()
                .getPhoneBook()
                .getOwnerContact()
                .getEmail(),
                "Breakin Detected!",
                "A breakin to your vehicle has been detected!",
            )
        )

    def streamRecordingToCloud(self):
        pass
