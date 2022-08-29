from autopilot.autopilot import Autopilot
from drivetrain.drivetrain import Drivetrain
from infotainment.pages.autopilot.autopilotPage import AutopilotPage
from infotainment.pages.page import Page
from infotainment.pages.security.securityPage import SecurityPage
from security.security import Security
from telecommunication.telecommunication import Telecommunication
from .telecommunication.telecommunicationPage import TelecommunicationPage
from .drivetrain.drivetrainPage import DrivetrainPage


class InfotainmentPage(Page):
    def __init__(
        self,
        stack,
        drivetrain: Drivetrain,
        telecommunication: Telecommunication,
        autopilot: Autopilot,
        security: Security,
    ):
        super().__init__()
        self.__stack = stack
        self.__drivetrain_page = DrivetrainPage(stack, drivetrain)
        self.__telecommunication_page = TelecommunicationPage(stack, telecommunication)
        self.__autopilot_page = AutopilotPage(stack, autopilot)
        self.__security_page = SecurityPage(stack, security)

    def start(self):
        while len(self.__stack) > 0:
            choice = input(
                """Select an option:
1) Drivetrain
2) Telecommunication
3) Autopilot
4) Security
0) Exit
"""
            )

            assert int(choice) <= 4, "Choice is outside the range"

            if choice == "1":
                self.__stack.append(self.__drivetrain_page)
            elif choice == "2":
                self.__stack.append(self.__telecommunication_page)
            elif choice == "3":
                self.__stack.append(self.__autopilot_page)
            elif choice == "4":
                self.__stack.append(self.__security_page)
            elif choice == "0":
                return self.__stack.pop()

            self.__stack[len(self.__stack) - 1].start()
