from infotainment.pages.page import Page
from security.security import Security


class AlertPage(Page):
    def __init__(self, stack, security: Security):
        super().__init__()
        self.__stack = stack
        self.__security = security

    def start(self):
        while len(self.__stack) > 0:
            choice = input(
                """Select an option:
1) Arm alert
2) Disarm alert
3) Alert from speakers
4) Alert from horn
5) Increase alert volume level
6) Decrease alert volume level
7) Get alert volume level
0) Back
"""
            )

            assert int(choice) <= 7, "Choice is outside the range"

            if choice == "1":
                self.__security.getAlert().arm()
            elif choice == "2":
                self.__security.getAlert().disarm()
            elif choice == "3":
                self.__security.getAlert().alertFromSpeakers()
            elif choice == "4":
                self.__security.getAlert().alertFromHorn()
            elif choice == "5":
                self.__security.getAlert().increaseAlertVolumeLevel(10)
            elif choice == "6":
                self.__security.getAlert().decreaseAlertVolumeLevel(10)
            elif choice == "7":
                self.__security.getAlert().getAlertVolumeLevel()
            elif choice == "0":
                self.__stack.pop()

            self.__stack[len(self.__stack) - 1].start()
