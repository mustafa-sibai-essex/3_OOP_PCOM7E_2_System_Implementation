from autopilot.autopilot import Autopilot
from infotainment.pages.page import Page


class AutopilotPage(Page):
    def __init__(self, stack, autopilot: Autopilot):
        super().__init__()
        self.__stack = stack
        self.__autopilot = autopilot

    def start(self):
        while len(self.__stack) > 0:
            choice = input(
                """Select an option:
1) Autopilot On
2) Autopilot Off
0) Back
"""
            )

            if choice == "1":
                self.__autopilot.turnOnAutopilot()
            elif choice == "2":
                self.__autopilot.turnOffAutopilot()
            elif choice == "0":
                self.__stack.pop()
                self.__stack[len(self.__stack) - 1].start()
