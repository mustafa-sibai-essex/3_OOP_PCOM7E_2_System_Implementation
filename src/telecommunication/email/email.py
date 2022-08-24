class Email:
    def __init__(self, sender_email: str, receiver_email: str, subject: str, body: str):
        self._sender_email = sender_email
        self._receiver_email = receiver_email
        self._subject = subject
        self._body = body

    def getSenderEmail(self):
        return self._sender_email

    def getReceiverEmail(self):
        return self._receiver_email

    def getSubject(self):
        return self._subject

    def getBody(self):
        return self._body
