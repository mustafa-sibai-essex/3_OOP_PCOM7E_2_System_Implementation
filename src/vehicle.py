from autopilot.autopilot import Autopilot
from drivetrain.drivetrain import Drivetrain
from infotainment.infotainment import Infotainment
from security.security import Security
from telecommunication.telecommunication import Telecommunication


class Vehicle:
    def __init__(self):
        self.__drivetrain = Drivetrain()
        self.__telecommunication = Telecommunication()
        self.__security = Security(self.__telecommunication)
        self.__autopilot = Autopilot(self.__drivetrain)
        self.__infotainment = Infotainment(
            self.__drivetrain,
            self.__telecommunication,
            self.__autopilot,
            self.__security,
        )

    def start(self):
        self.__infotainment.start()
