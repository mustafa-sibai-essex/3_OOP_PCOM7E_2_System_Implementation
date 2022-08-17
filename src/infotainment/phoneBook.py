from .contact import Contact


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def __str__(self):
        phone_book_string = ""

        for contact in self.contacts:
            phone_book_string += contact.__str__()

        return phone_book_string

    def addContact(self, contact: Contact):
        self.contacts.append(contact)

    def removeContact(self):
        pass

    def updateContact(self):
        pass
