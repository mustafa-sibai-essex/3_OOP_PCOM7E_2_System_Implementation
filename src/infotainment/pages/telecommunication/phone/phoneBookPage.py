from infotainment.pages.page import Page
from infotainment.pages.telecommunication.phone.addContactPage import AddContactPage
from infotainment.pages.telecommunication.phone.removeContactPage import (
    RemoveContactPage,
)
from infotainment.pages.telecommunication.phone.updaetOwnerContact import (
    UpdateOwnerContactPage,
)
from infotainment.pages.telecommunication.phone.updateContactPage import (
    UpdateContactPage,
)
from loggingSystem import LoggingSystem
from telecommunication.telecommunication import Telecommunication


class PhoneBookPage(Page):
    def __init__(self, stack, telecommunication: Telecommunication):
        super().__init__()
        self.__stack = stack
        self.__telecommunication = telecommunication
        self.__add_contact_page = AddContactPage(stack, telecommunication)
        self.__remove_contact_page = RemoveContactPage(stack, telecommunication)
        self.__update_contact_page = UpdateContactPage(stack, telecommunication)
        self.__update_owner_contactPage = UpdateOwnerContactPage(
            stack, telecommunication
        )

    def start(self):
        while len(self.__stack) > 0:
            choice = input(
                """Select an option:
1) Add Contact
2) Remove Contact
3) Update Contact
4) Update Owner Contact
5) View All Contacts
0) Back
"""
            )

            assert int(choice) <= 5, "Choice is outside the range"

            if choice == "1":
                self.__stack.append(self.__add_contact_page)
                self.__stack[len(self.__stack) - 1].start()
            elif choice == "2":
                self.__stack.append(self.__remove_contact_page)
                self.__stack[len(self.__stack) - 1].start()
            elif choice == "3":
                self.__stack.append(self.__update_contact_page)
                self.__stack[len(self.__stack) - 1].start()
            elif choice == "4":
                self.__stack.append(self.__update_owner_contactPage)
                self.__stack[len(self.__stack) - 1].start()
            elif choice == "5":
                LoggingSystem.logInfo(
                    self.__telecommunication.getPhone().getPhoneBook().__str__()
                )
            elif choice == "0":
                self.__stack.pop()
                self.__stack[len(self.__stack) - 1].start()
