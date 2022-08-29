from infotainment.pages.page import Page
from telecommunication.telecommunication import Telecommunication


class PhoneBookPage(Page):
    def __init__(self, stack, telecommunication: Telecommunication):
        super().__init__()
        self.__stack = stack
        self.__telecommunication = telecommunication

    def start(self):
        while True:
            choice = input(
                """Select an option:
1) Add Contact
2) Remove Contact
3) Update Contact
4) Update Owner Contact
5) Get Emergency Contact
6) Get Contact
0) Back
"""
            )

            if choice == "1":
                self.__telecommunication.getPhone().getPhoneBook().addContact()
            elif choice == "2":
                self.__telecommunication.getCloudServer().disconnect()
            elif choice == "3":
                self.__telecommunication.getCloudServer().uploadStatstics()
            elif choice == "0":
                self.__stack.pop()
                self.__stack[len(self.__stack) - 1].start()
