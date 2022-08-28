from infotainment.contactType import ContactType


class BasicContact:
    """BasicContact class contains basic information about contact like name and phone number"""

    def __init__(self, name: str, phone_number: str, contact_type: ContactType):
        """Sets the contact name, phone number and contact type"""
        self.__name = name
        self.__phone_number = phone_number
        self.__contact_type = contact_type

    def __str__(self):
        """Prints contact name and phone number"""
        return """Name: {0}
Phone Number: {1}""".format(
            self.__name, self.__phone_number
        )

    def getName(self):
        """Returns the contact name"""
        return self.__name

    def getPhoneNumber(self):
        """Returns the contact phone number"""
        return self.__phone_number
