from drivetrain.drivetrain import Drivetrain
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
        telecommunication: Telecommunication,
        drivetrain: Drivetrain,
        security: Security,
    ):
        super().__init__()
        self.__stack = stack
        self.__telecommunication_page = TelecommunicationPage(stack, telecommunication)
        self.__drivetrain_page = DrivetrainPage(stack, drivetrain)
        self.__security_page = SecurityPage(stack, security)

    def start(self):
        while True:
            choice = input(
                """Select an option:
1) Telecommunication
2) Drivetrain
3) Security
0) Exit
"""
            )

            if choice == "1":
                self.__stack.append(self.__telecommunication_page)
            elif choice == "2":
                self.__stack.append(self.__drivetrain_page)
            elif choice == "3":
                self.__stack.append(self.__security_page)
            elif choice == "0":
                break

            self.__stack[len(self.__stack) - 1].start()
