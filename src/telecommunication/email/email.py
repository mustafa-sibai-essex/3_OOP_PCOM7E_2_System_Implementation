class Email:
    """The email class contains data about the email like sender address, receiver address, subject and body"""

    def __init__(
        self,
        sender_email_address: str,
        receiver_email_address: str,
        subject: str,
        body: str,
    ):
        """Creates the email object with sender_email_address, receiver_email_address, subject and body"""
        self.__sender_email_address = sender_email_address
        self.__receiver_email_address = receiver_email_address
        self.__subject = subject
        self.__body = body

    def getSenderEmail(self):
        """Returns the sender email address of the email"""
        return self.__sender_email_address

    def getReceiverEmail(self):
        """Returns the receiver email address of the email"""
        return self.__receiver_email_address

    def getSubject(self):
        """Returns the subject of the email"""
        return self.__subject

    def getBody(self):
        """Returns the body of the email"""
        return self.__body
