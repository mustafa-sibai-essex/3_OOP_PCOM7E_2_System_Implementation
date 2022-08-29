class SMS:
    """SMS class contains data about the sms such as phone number and message"""

    def __init__(self, phone_number: str, message: str):
        """Creates an sms object with phone number and message"""
        self.__phone_number = phone_number
        self.__message = message

    def getPhoneNumber(self):
        """Returns the phone number assigned to the sms"""
        return self.__phone_number

    def getMessage(self):
        """Returns the message assigned to the sms"""
        return self.__message
