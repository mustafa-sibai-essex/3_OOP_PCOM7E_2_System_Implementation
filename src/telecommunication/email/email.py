class Email:
    def __init__(self, sender_email: str, receiver_email: str, subject: str, body: str):
        self.__sender_email = sender_email
        self.__receiver_email = receiver_email
        self.__subject = subject
        self.__body = body

    def getSenderEmail(self):
        return self.__sender_email

    def getReceiverEmail(self):
        return self.__receiver_email

    def getSubject(self):
        return self.__subject

    def getBody(self):
        return self.__body
