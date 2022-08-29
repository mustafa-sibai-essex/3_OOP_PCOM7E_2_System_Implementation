from infotainment.pages.page import Page
from infotainment.pages.security.entrancePage import EntrancePage
from security.security import Security


class SecurityPage(Page):
    def __init__(self, stack, security: Security):
        super().__init__()
        self.__stack = stack
        self.__security = security
        self.__entrance_page = EntrancePage(stack, security)

    def start(self):
        choice = input(
            """Select an option:
1) Entrance
2) Alert
3) Start Detecting Break In
4) Stop Detecting Break In 
5) Send GPS Location To Owner Via SMS
6) Send Break In Notification To Owner Via SMS
7) Send Break In Notification To Owner Via Email
0) Back
"""
        )

        if choice == "1":
            self.__stack.append(self.__entrance_page)
        elif choice == "2":
            self.__stack.append(self.__gps_page)
        elif choice == "3":
            self.__stack.append(self.__cloud_server_page)
        elif choice == "0":
            self.__stack.pop()

        self.__stack[len(self.__stack) - 1].start()
