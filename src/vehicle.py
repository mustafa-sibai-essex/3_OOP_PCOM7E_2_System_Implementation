from autopilot.autopilot import Autopilot
from diagnostics import Diagnostics
from drivetrain.drivetrain import Drivetrain
from infotainment.infotainment import Infotainment
from security.security import Security
from telecommunication.telecommunication import Telecommunication


class Vehicle:
    """Vehicle class contains all the of major systems"""

    def __init__(self):
        """Creates the vehicle class object and sets up all major systems"""
        self.__diagnostics = Diagnostics()
        self.__diagnostics.startVerificationProcess()
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
        """Starts the vehicle infortainment system"""
        self.__infotainment.start()
