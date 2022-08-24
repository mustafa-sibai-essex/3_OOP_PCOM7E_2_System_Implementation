from loggingSystem import LoggingSystem
from telecommunication.email.email import Email


class EmailManager:
    def __init__(self):
        self._emails = list[Email]

    def sendEmail(self, email: Email):
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

    def deleteEmail(self, index: int):
        del self._emails[index]

    def syncEmails(self):
        LoggingSystem.logInfo("Emails are syncing")
