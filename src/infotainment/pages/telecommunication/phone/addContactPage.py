from infotainment.pages.page import Page
from loggingSystem import LoggingSystem
from telecommunication.phone.contact import Contact
from telecommunication.phone.contactType import ContactType
from telecommunication.telecommunication import Telecommunication


class AddContactPage(Page):
    def __init__(self, stack, telecommunication: Telecommunication):
        super().__init__()
        self.__stack = stack
        self.__telecommunication = telecommunication

    def start(self):
        name = input(
            """Add new contact
Enter name:
"""
        )

        phone_number = input(
            """
Enter phone number:
"""
        )

        email = input(
            """
Enter Email:
"""
        )

        contact = (
            self.__telecommunication.getPhone()
            .getPhoneBook()
            .addContact(Contact(name, phone_number, ContactType.NORMAL, email))
        )

        LoggingSystem.logInfo(
            """
Contact added with the following information:
{0}""".format(
                contact
            )
        )

        self.__stack.pop()
        self.__stack[len(self.__stack) - 1].start()
