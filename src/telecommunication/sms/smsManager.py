from loggingSystem import LoggingSystem
from telecommunication.connectionState import ConnectionState
from telecommunication.satellite import Satellite
from telecommunication.sms.sms import SMS


class SMSManager:
    """SMSManager class is responsible for managing, deleting and sending SMSes"""

    def __init__(self, satellite: Satellite):
        """Creates the SMSManager object and setups a list of SMSes"""
        self.__satellite = satellite
        self.__smses = list[SMS]

    def sendSMS(self, sms: SMS):
        """Sends an SMS message as long as we are connected to the satellite"""
        if self.__satellite.getState() == ConnectionState.CONNECTED:
            self.__smses.append(sms)
            LoggingSystem.logInfo(
                """SMS sent to: {0}
with message of {1}""".format(
                    sms.getPhoneNumber(), sms.getMessage()
                )
            )
        else:
            LoggingSystem.logError("Cannot send SMS if not connected to satellite")

    def deleteSMS(self, index: int):
        """Deletes an SMS message according to the index number"""
        del self.__smses[index]
