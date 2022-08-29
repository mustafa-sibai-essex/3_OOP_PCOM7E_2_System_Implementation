from infotainment.pages.page import Page
from infotainment.pages.telecommunication.gpsPage import GPSPage
from infotainment.pages.telecommunication.phone.phonePage import PhonePage
from infotainment.pages.telecommunication.satellitePage import SatellitePage
from infotainment.pages.telecommunication.cloudServerPage import CloudServerPage
from telecommunication.telecommunication import Telecommunication


class TelecommunicationPage(Page):
    def __init__(self, stack, telecommunication: Telecommunication):
        super().__init__()
        self.__stack = stack
        self.__telecommunication = telecommunication
        self.__satellite_page = SatellitePage(self.__stack, self.__telecommunication)
        self.__gps_page = GPSPage(self.__stack, self.__telecommunication)
        self.__cloud_server_page = CloudServerPage(
            self.__stack, self.__telecommunication
        )
        self.__phone_page = PhonePage(stack, telecommunication)

    def start(self):
        while len(self.__stack) > 0:
            choice = input(
                """Select an option:
1) Sattellite
2) GPS
3) Cloud Server
4) Phone
0) Back
"""
            )

            assert int(choice) <= 4, "Choice is outside the range"

            if choice == "1":
                self.__stack.append(self.__satellite_page)
            elif choice == "2":
                self.__stack.append(self.__gps_page)
            elif choice == "3":
                self.__stack.append(self.__cloud_server_page)
            elif choice == "4":
                self.__stack.append(self.__phone_page)
            elif choice == "0":
                self.__stack.pop()

            self.__stack[len(self.__stack) - 1].start()
