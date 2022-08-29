from drivetrain.drivetrain import Drivetrain
from infotainment.pages.page import Page


class BreaksPage(Page):
    def __init__(self, stack, drivetrain: Drivetrain):
        super().__init__()
        self.__stack = stack
        self.__drivetrain = drivetrain

    def start(self):
        choice = input(
            """Select an option:
1) Apply front breaks
2) Apply rear breaks
3) Turn on parking breaks
4) Turn off parking breaks
0) Back
"""
        )

        if choice == "1":
            self.__drivetrain.getBreaksManager().applyFrontBreaks(10)
        elif choice == "2":
            self.__drivetrain.getBreaksManager().applyRearBreaks(10)
        elif choice == "3":
            self.__drivetrain.getBreaksManager().turnOnParkingBreaks()
        elif choice == "4":
            self.__drivetrain.getBreaksManager().turnOffParkingBreaks()
        elif choice == "0":
            self.__stack.pop()
            self.__stack[len(self.__stack) - 1].start()
