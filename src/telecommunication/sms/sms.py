class SMS:
    def __init__(self, phone_number: str, message: str):
        self._phone_number = phone_number
        self._message = message

    def getPhoneNumber(self):
        return self._phone_number

    def getMessage(self):
        return self._message
