from infotainment.pages.page import Page
from infotainment.pages.telecommunication.phone.callContactPage import CallContactPage
from infotainment.pages.telecommunication.phone.phoneBookPage import PhoneBookPage
from telecommunication.telecommunication import Telecommunication


class PhonePage(Page):
    def __init__(self, stack, telecommunication: Telecommunication):
        super().__init__()
        self.__stack = stack
        self.__telecommunication = telecommunication
        self.__call_contact_page = CallContactPage(stack, telecommunication)
        self.__phone_book_page = PhoneBookPage(stack, telecommunication)

    def start(self):
        while len(self.__stack) > 0:
            choice = input(
                """Select an option:
1) Call Contact
2) Phone Book
3) Call Emergancy Services
0) Back
"""
            )

            assert int(choice) <= 3, "Choice is outside the range"

            if choice == "1":
                self.__stack.append(self.__call_contact_page)
                self.__stack[len(self.__stack) - 1].start()
            elif choice == "2":
                self.__stack.append(self.__phone_book_page)
                self.__stack[len(self.__stack) - 1].start()
            elif choice == "3":
                self.__telecommunication.getPhone().callEmergancyServices()
            elif choice == "0":
                self.__stack.pop()
                self.__stack[len(self.__stack) - 1].start()
