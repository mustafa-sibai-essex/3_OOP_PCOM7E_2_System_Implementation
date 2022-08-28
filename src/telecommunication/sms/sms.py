class SMS:
    def __init__(self, phone_number: str, message: str):
        self.__phone_number = phone_number
        self.__message = message

    def getPhoneNumber(self):
        return self.__phone_number

    def getMessage(self):
        return self.__message
