from infotainment.pages.page import Page
from telecommunication.telecommunication import Telecommunication


class GPSPage(Page):
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
3) Get Speed
4) Get Lattitude
5) Get Longitude
6) Get Altitude
0) Back
"""
            )

            if choice == "1":
                self.__telecommunication.getGPS().connect()
            elif choice == "2":
                self.__telecommunication.getGPS().disconnect()
            elif choice == "3":
                self.__telecommunication.getGPS().getSpeed()
            elif choice == "4":
                self.__telecommunication.getGPS().getLattitude()
            elif choice == "5":
                self.__telecommunication.getGPS().getLongitude()
            elif choice == "6":
                self.__telecommunication.getGPS().getAltitude()
            elif choice == "0":
                self.__stack.pop()
                self.__stack[len(self.__stack) - 1].start()
