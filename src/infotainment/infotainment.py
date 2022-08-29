from autopilot.autopilot import Autopilot
from drivetrain.drivetrain import Drivetrain
from infotainment.pages.infotainmentPage import InfotainmentPage
from security.security import Security
from telecommunication.telecommunication import Telecommunication


class Infotainment:
    def __init__(
        self,
        drivetrain: Drivetrain,
        telecommunication: Telecommunication,
        autopilot: Autopilot,
        security: Security,
    ):
        self.__stack = []
        self.__infotainment_page = InfotainmentPage(
            self.__stack, drivetrain, telecommunication, autopilot, security
        )

    def start(self):
        self.__stack.append(self.__infotainment_page)
        self.__stack[0].start()
