from loggingSystem import LoggingSystem
from telecommunication.connectionState import ConnectionState
from telecommunication.satellite import Satellite
from .phoneBook import PhoneBook


class Phone:
    """Phone class allows the user to make calls"""

    def __init__(self, satellite: Satellite):
        """Creates phone book object in phone"""
        self.__phone_book = PhoneBook()
        self.__satellite = satellite

    def callByContactName(self, contact_name: str):
        """Finds and calls a contact when passing contact_name as long as connected to satellite"""

        if self.__satellite.getState() != ConnectionState.CONNECTED:
            return LoggingSystem.logError(
                "Cannot make calls before connecting to satellite"
            )

        contact = self.__phone_book.getContact(contact_name)

        LoggingSystem.logInfo(
            """Calling {0} {1}""".format(contact.getName(), contact.getPhoneNumber())
        )

    def callByContactIndex(self, index: int):
        """Calls a contact when passing an index as long as connected to satellite"""

        if self.__satellite.getState() != ConnectionState.CONNECTED:
            return LoggingSystem.logError(
                "Cannot make calls before connecting to satellite"
            )

        contact = self.__phone_book.getContactByIndex(index)

        LoggingSystem.logInfo(
            """Calling {0} {1}""".format(contact.getName(), contact.getPhoneNumber())
        )

    def callEmergancyServices(self):
        """Calls emergency services"""

        if self.__satellite.getState() != ConnectionState.CONNECTED:
            return LoggingSystem.logError(
                "Cannot make calls before connecting to satellite"
            )

        LoggingSystem.logInfo(
            """Calling emergency services: {0}""".format(
                self.__phone_book.getEmergencyContact().getPhoneNumber()
            )
        )

    def getPhoneBook(self):
        """Returns the phone book object"""
        return self.__phone_book
