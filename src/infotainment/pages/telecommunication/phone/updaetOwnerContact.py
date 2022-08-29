from infotainment.pages.page import Page
from loggingSystem import LoggingSystem
from telecommunication.phone.contact import Contact
from telecommunication.phone.contactType import ContactType
from telecommunication.telecommunication import Telecommunication


class UpdateOwnerContactPage(Page):
    def __init__(self, stack, telecommunication: Telecommunication):
        super().__init__()
        self.__stack = stack
        self.__telecommunication = telecommunication

    def start(self):

        LoggingSystem.logInfo(
            """Current owner contact is:
{0}""".format(
                self.__telecommunication.getPhone().getPhoneBook().getOwnerContact()
            )
        )

        name = input(
            """Enter new owner contcts information
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
            .updateOwnerContact(Contact(name, phone_number, ContactType.OWNER, email))
        )

        LoggingSystem.logInfo(
            """
Owner contact has been updated:
{0}""".format(
                contact
            )
        )

        self.__stack.pop()
        self.__stack[len(self.__stack) - 1].start()
