from infotainment.contactType import ContactType
from .phoneBook import PhoneBook


class Phone:
    def __init__(self):
        self.phone_book = PhoneBook()

    def call(self, contact: ContactType):
        pass

    def callEmergancyServices(self):
        pass

    def getPhoneBook(self):
        return self.phone_book
