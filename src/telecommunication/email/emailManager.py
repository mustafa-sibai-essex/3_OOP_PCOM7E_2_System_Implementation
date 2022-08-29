from loggingSystem import LoggingSystem
from telecommunication.connectionState import ConnectionState
from telecommunication.email.email import Email
from telecommunication.satellite import Satellite


class EmailManager:
    """EmailManager class is responsible for managing, deleting and sending emails"""

    def __init__(self, satellite: Satellite):
        """Creates the EmailManager object and setups a list of emails"""
        self.__satellite = satellite
        self.__emails = list[Email]

    def sendEmail(self, email: Email):
        """Sends an email as long as we are connected to the satellite"""
        if self.__satellite.getState() == ConnectionState.CONNECTED:
            self.__emails.append(email)
            LoggingSystem.logInfo(
                """Email: {0}
sent to {1}
from {2} with body of
{3}""".format(
                    email.getSubject(),
                    email.getReceiverEmail(),
                    email.getSenderEmail(),
                    email.getBody(),
                )
            )
        else:
            LoggingSystem.logError("Cannot send an email if not connected to satellite")

    def deleteEmail(self, index: int):
        """Deletes an email according to the index number"""
        del self._emails[index]

    def syncEmails(self):
        """Sync emails as long as connected to satellite"""
        if self.__satellite.getState() == ConnectionState.CONNECTED:
            LoggingSystem.logInfo("Emails are synced")
        else:
            LoggingSystem.logError("Cannot sync emails if not connected to satellite")
