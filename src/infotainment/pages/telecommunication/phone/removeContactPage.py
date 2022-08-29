from infotainment.pages.page import Page
from loggingSystem import LoggingSystem
from telecommunication.telecommunication import Telecommunication


class RemoveContactPage(Page):
    def __init__(self, stack, telecommunication: Telecommunication):
        super().__init__()
        self.__stack = stack
        self.__telecommunication = telecommunication

    def start(self):

        LoggingSystem.logInfo(
            self.__telecommunication.getPhone().getPhoneBook().__str__()
        )

        index = input(
            """Enter the number to remove
"""
        )

        self.__telecommunication.getPhone().getPhoneBook().removeContactByIndex(int(index))

        LoggingSystem.logInfo(
            """
Contact removed!
"""
        )

        self.__stack.pop()
        self.__stack[len(self.__stack) - 1].start()
