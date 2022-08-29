from loggingSystem import LoggingSystem
from telecommunication.phone.contactType import ContactType
from .contact import Contact


class PhoneBook:
    """Phone book class stores all contacts and allows the user to add, remove, and update contacts"""

    def __init__(self):
        """Creates a the phone with a list of contacts"""
        self.__contacts: list[Contact] = []
        self.__contacts.append(
            Contact("Emergency", "999", ContactType.EMERGENCY, "emergency@uk.gov")
        )
        self.__contacts.append(
            Contact("Owner", "0", ContactType.OWNER, "owner@email.com")
        )

    def __str__(self):
        """Prints the entire phone book contacts information"""
        phone_book_string = ""

        for i in range(0, len(self.__contacts)):
            phone_book_string += "{0}) {1}\n".format(i, self.__contacts[i].getName())

        return phone_book_string

    def __getContactIndex(self, contact_name: str):
        """Returns an index number of the contact that matches contact_name from the phone book"""
        contact_len = len(self.__contacts)

        for i in range(0, contact_len):
            if self.__contacts[i].getName() == contact_name:
                return i

    def addContact(self, contact: Contact):
        """Add a new contact to your phone book and returns the newly added contact"""
        self.__contacts.append(contact)
        return contact

    def removeContactByName(self, contact_name: str):
        """Removes a contact from the phone book based on contact_name"""
        contact_index = self.__getContactIndex(self, contact_name)
        self.__contacts.pop(contact_index)

    def removeContactByIndex(self, index: int):
        """Removes a contact from the phone book based on the index"""
        if index >= len(self.__contacts):
            return LoggingSystem.logError("Index is out of range")

        self.__contacts.pop(index)

    def updateContactByName(self, contact_name: str, updated_contact: Contact):
        """Updates a contact in the phone book based on contact_name and returns it"""
        contact_index = self.__getContactIndex(self, contact_name)
        self.__contacts[contact_index] = updated_contact
        return self.__contacts[contact_index]

    def updateContactByIndex(self, index: int, updated_contact: Contact):
        """Updates a contact in the phone book based on index and return it"""
        self.__contacts[index] = updated_contact
        return self.__contacts[index]

    def updateOwnerContact(self, updated_contact: Contact):
        """Updates owner contact in the phone book and returns it"""
        self.__contacts[1] = updated_contact
        return self.__contacts[1]

    def getEmergencyContact(self):
        """Returns emergency contact from the phone book"""
        return self.__contacts[0]

    def getContactByName(self, contact_name: str):
        """Returns a contact from the phone book based on contact_name"""
        contact_index = self.__getContactIndex(self, contact_name)
        return self.__contacts[contact_index]

    def getContactByIndex(self, index: int):
        """Returns a contact from the phone book based on index"""
        if index >= len(self.__contacts):
            return LoggingSystem.logError("Index is out of range")

        return self.__contacts[index]

    def getOwnerContact(self):
        """Returns the owner contact from the phone book"""
        return self.__contacts[1]
