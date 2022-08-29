from infotainment.pages.page import Page
from security.security import Security


class EntrancePage(Page):
    def __init__(self, stack, security: Security):
        super().__init__()
        self.__stack = stack
        self.__security = security

    def start(self):
        while len(self.__stack) > 0:
            choice = input(
                """Select an option:
1) Lock Front Doors
2) Lock Back Doors
3) Lock Trunk
4) Lock All Entrances
5) Unlock FrontDoors
6) Unlock BackDoors
7) Unlock Trunk
8) Unlock All Entrances
0) Back
"""
            )

            assert int(choice) <= 8, "Choice is outside the range"

            if choice == "1":
                self.__security.getEntranceManager().lockFrontDoors()
            elif choice == "2":
                self.__security.getEntranceManager().lockBackDoors()
            elif choice == "3":
                self.__security.getEntranceManager().lockTrunk()
            elif choice == "4":
                self.__security.getEntranceManager().lockAllEntrances()
            elif choice == "5":
                self.__security.getEntranceManager().unlockFrontDoors()
            elif choice == "6":
                self.__security.getEntranceManager().unlockBackDoors()
            elif choice == "7":
                self.__security.getEntranceManager().unlockTrunk()
            elif choice == "8":
                self.__security.getEntranceManager().unlockAllEntrances()
            elif choice == "0":
                self.__stack.pop()

            self.__stack[len(self.__stack) - 1].start()
