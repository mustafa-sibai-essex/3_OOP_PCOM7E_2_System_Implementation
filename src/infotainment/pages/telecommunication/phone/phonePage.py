from infotainment.pages.page import Page
from telecommunication.telecommunication import Telecommunication


class PhonePage(Page):
    def __init__(self, stack, telecommunication: Telecommunication):
        super().__init__()
        self.__stack = stack
        self.__telecommunication = telecommunication

    def start(self):
        choice = input(
            """Select an option:
1) Call Contact
2) Phone Book
3) Call Emergancy Services
0) Back
"""
        )

        if choice == "1":
            self.__telecommunication.getPhone().call()
        elif choice == "2":
            self.__telecommunication.getPhone().getPhoneBook()
        elif choice == "3":
            self.__telecommunication.getCloudServer().uploadStatstics()
        elif choice == "0":
            self.__stack.pop()
            self.__stack[len(self.__stack) - 1].start()
