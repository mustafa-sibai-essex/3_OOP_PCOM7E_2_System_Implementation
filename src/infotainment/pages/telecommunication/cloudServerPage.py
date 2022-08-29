from infotainment.pages.page import Page
from telecommunication.telecommunication import Telecommunication


class CloudServerPage(Page):
    def __init__(self, stack, telecommunication: Telecommunication):
        super().__init__()
        self.__stack = stack
        self.__telecommunication = telecommunication

    def start(self):
        while len(self.__stack) > 0:
            choice = input(
                """Select an option:
1) Connect
2) Disconnects
3) Upload Statstics
4) Upload Data
5) Stream Data
0) Back
"""
            )

            if choice == "1":
                self.__telecommunication.getCloudServer().connect()
            elif choice == "2":
                self.__telecommunication.getCloudServer().disconnect()
            elif choice == "3":
                self.__telecommunication.getCloudServer().uploadStatstics()
            elif choice == "4":
                self.__telecommunication.getCloudServer().uploadData([1, 2, 3, 4, 5])
            elif choice == "5":
                self.__telecommunication.getCloudServer().streamData([1, 2, 3, 4, 5])
            elif choice == "0":
                self.__stack.pop()
                self.__stack[len(self.__stack) - 1].start()
