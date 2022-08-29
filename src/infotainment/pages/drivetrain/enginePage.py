from drivetrain.drivetrain import Drivetrain
from infotainment.pages.page import Page


class EnginePage(Page):
    def __init__(self, stack, drivetrain: Drivetrain):
        super().__init__()
        self.__stack = stack
        self.__drivetrain = drivetrain

    def start(self):
        while len(self.__stack) > 0:
            choice = input(
                """Select an option:
1) Start engine
2) Stop engine
3) Accelerate
4) Decelerate
0) Back
"""
            )

            assert int(choice) <= 4, "Choice is outside the range"

            if choice == "1":
                self.__drivetrain.getEngine().start()
            elif choice == "2":
                self.__drivetrain.getEngine().stop()
            elif choice == "3":
                self.__drivetrain.getEngine().accelerate()
            elif choice == "4":
                self.__drivetrain.getEngine().decelerate()
            elif choice == "0":
                self.__stack.pop()
                self.__stack[len(self.__stack) - 1].start()
