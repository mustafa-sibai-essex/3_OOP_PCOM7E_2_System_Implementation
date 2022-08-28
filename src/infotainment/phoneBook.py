from infotainment.contactType import ContactType
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

        for contact in self.__contacts:
            phone_book_string += contact.__str__()

        return phone_book_string

    def __getContactIndex(self, contact_name: str):
        """Returns an index number of the contact that matches contact_name from the phone book"""
        contact_len = len(self.__contacts)

        for i in range(0, contact_len):
            if self.__contacts[i].getName() == contact_name:
                return i

    def addContact(self, contact: Contact):
        """Add a new contact to your phone book"""
        self.__contacts.append(contact)

    def removeContact(self, contact_name: str):
        """Removes a contact from the phone book based on contact_name"""
        contact_index = self.__getContactIndex(self, contact_name)
        self.__contacts.pop(contact_index)

    def updateContact(self, contact_name: str, updated_contact: Contact):
        """Updates a contact in the phone book based on contact_name"""
        contact_index = self.__getContactIndex(self, contact_name)
        self.__contacts[contact_index] = updated_contact

    def updateOwnerContact(self, updated_contact: Contact):
        """Updates owner contact in the phone book"""
        self.__contacts[1] = updated_contact

    def getEmergencyContact(self):
        """Returns emergency contact from the phone book"""
        return self.__contacts[0]

    def getContact(self, contact_name: str):
        """Returns a contact from the phone book based on contact_name"""
        contact_index = self.__getContactIndex(self, contact_name)
        return self.__contacts[contact_index]
