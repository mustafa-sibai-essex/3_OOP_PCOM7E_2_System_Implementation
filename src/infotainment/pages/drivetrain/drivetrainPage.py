from drivetrain.drivetrain import Drivetrain
from infotainment.pages.drivetrain.breaksPage import BreaksPage
from infotainment.pages.drivetrain.enginePage import EnginePage
from infotainment.pages.drivetrain.steeringPage import SteeringPage
from infotainment.pages.page import Page


class DrivetrainPage(Page):
    def __init__(self, stack, drivetrain: Drivetrain):
        super().__init__()
        self.__stack = stack
        self.__enginePage = EnginePage(self.__stack, drivetrain)
        self.__steeringPage = SteeringPage(self.__stack, drivetrain)
        self.__breaksPage = BreaksPage(self.__stack, drivetrain)

    def start(self):
        while True:
            choice = input(
                """Select an option:
1) Engine
2) Steering
3) Breaks
0) Back
"""
            )

            if choice == "1":
                self.__stack.append(self.__enginePage)
            elif choice == "2":
                self.__stack.append(self.__steeringPage)
            elif choice == "3":
                self.__stack.append(self.__breaksPage)
            elif choice == "0":
                self.__stack.pop()

            self.__stack[len(self.__stack) - 1].start()
