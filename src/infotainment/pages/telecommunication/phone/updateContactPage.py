from infotainment.pages.page import Page
from loggingSystem import LoggingSystem
from telecommunication.phone.contact import Contact
from telecommunication.phone.contactType import ContactType
from telecommunication.telecommunication import Telecommunication


class UpdateContactPage(Page):
    def __init__(self, stack, telecommunication: Telecommunication):
        super().__init__()
        self.__stack = stack
        self.__telecommunication = telecommunication

    def start(self):

        LoggingSystem.logInfo(
            self.__telecommunication.getPhone().getPhoneBook().__str__()
        )

        choice = input(
            """
Select which contact to update
"""
        )

        name = input(
            """
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
            .updateContactByIndex(
                int(choice), Contact(name, phone_number, ContactType.OWNER, email)
            )
        )

        LoggingSystem.logInfo(
            """
Contact has been updated:
{0}""".format(
                contact
            )
        )

        self.__stack.pop()
        self.__stack[len(self.__stack) - 1].start()
