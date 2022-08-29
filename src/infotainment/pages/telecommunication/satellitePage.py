from infotainment.pages.page import Page
from telecommunication.telecommunication import Telecommunication


class SatellitePage(Page):
    def __init__(self, stack, telecommunication: Telecommunication):
        super().__init__()
        self.__stack = stack
        self.__telecommunication = telecommunication

    def start(self):
        while len(self.__stack) > 0:
            choice = input(
                """Select an option:
1) Connect
2) Disconnects
3) Get State
0) Back
"""
            )

            assert int(choice) <= 3, "Choice is outside the range"

            if choice == "1":
                self.__telecommunication.getSatellite().connect()
            elif choice == "2":
                self.__telecommunication.getSatellite().disconnect()
            elif choice == "3":
                self.__telecommunication.getSatellite().getState()
            elif choice == "0":
                self.__stack.pop()
                self.__stack[len(self.__stack) - 1].start()
