from drivetrain.drivetrain import Drivetrain
from infotainment.pages.page import Page


class BreaksPage(Page):
    def __init__(self, stack, drivetrain: Drivetrain):
        super().__init__()
        self.__stack = stack
        self.__drivetrain = drivetrain

    def start(self):
        while True:
            choice = input(
                """Select an option:
1) Increase front breaks force
2) Decrease front breaks force
3) Increase rear breaks force
4) Decrease rear breaks force
5) Turn on parking breaks
6) Turn off parking breaks
0) Back
"""
            )

            if choice == "1":
                self.__drivetrain.getBreaksManager().increaseFrontBreaksForce(10)
            elif choice == "2":
                self.__drivetrain.getBreaksManager().decreaseFrontBreaksForce(10)
            elif choice == "3":
                self.__drivetrain.getBreaksManager().increaseRearBreaksForce(10)
            elif choice == "4":
                self.__drivetrain.getBreaksManager().decreaseRearBreaksForce(10)
            elif choice == "5":
                self.__drivetrain.getBreaksManager().turnOnParkingBreaks()
            elif choice == "6":
                self.__drivetrain.getBreaksManager().turnOffParkingBreaks()
            elif choice == "0":
                self.__stack.pop()
                self.__stack[len(self.__stack) - 1].start()
