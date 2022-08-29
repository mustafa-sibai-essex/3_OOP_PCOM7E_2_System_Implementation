from drivetrain.drivetrain import Drivetrain
from infotainment.pages.page import Page


class SteeringPage(Page):
    def __init__(self, stack, drivetrain: Drivetrain):
        super().__init__()
        self.__stack = stack
        self.__drivetrain = drivetrain

    def start(self):
        while True:
            choice = input(
                """Select an option:
1) Steer right
2) Steer left
0) Back
"""
            )

            if choice == "1":
                self.__drivetrain.getSteering().steerRight(10)
            elif choice == "2":
                self.__drivetrain.getSteering().steerLeft(10)
            elif choice == "0":
                self.__stack.pop()
                self.__stack[len(self.__stack) - 1].start()
