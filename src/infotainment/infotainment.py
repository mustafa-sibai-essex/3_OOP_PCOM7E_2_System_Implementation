from .phone import Phone


class Infotainment:
    def __init__(self):
        self.__phone = Phone()

    def getPhone(self):
        """Returns the phone object"""
        return self.__phone
