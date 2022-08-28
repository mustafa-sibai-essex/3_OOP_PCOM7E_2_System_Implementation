from infotainment.contactType import ContactType
from loggingSystem import LoggingSystem
from .phoneBook import PhoneBook


class Phone:
    """Phone class allows the user to make calls"""

    def __init__(self):
        """Creates phone book object in phone"""
        self.__phone_book = PhoneBook()

    def call(self, contact_name: str):
        """Finds and calls a contact when passing contact_name"""
        contact = self.__phone_book.getContact(contact_name)

        LoggingSystem.logInfo(
            """Calling {0} {1}""".format(contact.getName(), contact.getPhoneNumber())
        )

    def callEmergancyServices(self):
        """Calls emergency services"""
        LoggingSystem.logInfo(
            """Calling emergency services: {0}""".format(
                self.__phone_book.getEmergencyContact().getPhoneNumber()
            )
        )

    def getPhoneBook(self):
        """Returns the phone book object"""
        return self.__phone_book
