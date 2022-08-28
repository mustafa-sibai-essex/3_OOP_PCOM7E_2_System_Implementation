from loggingSystem import LoggingSystem
from telecommunication.sms.sms import SMS


class SMSManager:
    def __init__(self):
        self.__smses = list[SMS]

    def sendSMS(self, sms: SMS):
        self.__smses.append(sms)
        LoggingSystem.logInfo(
            """sms send to: {0}
with message of {1}""".format(
                sms.getPhoneNumber(), sms.getMessage()
            )
        )

    def deleteSMS(self, index: int):
        del self.__smses[index]
