from drivetrain.breaks.breakPosition import BreakPosition
from loggingSystem import LoggingSystem


class VehicleBreak:
    """VehicleBreak class controls a single break in the vehicle"""

    def __init__(self, break_position: BreakPosition):
        """Creates the break object and sets max and current break force"""
        self.__break_position = break_position
        self.__max_break_force = 100
        self.__min_break_force = 0
        self.__current_break_force = self.__min_break_force

    def increaseBreakForce(self, force: int):
        """Increases the break force to the force value. break force value cannot exceed max_break_force"""
        self.__current_break_force += force

        if self.__current_break_force > self.__max_break_force:
            self.__current_break_force = self.__max_break_force
            return LoggingSystem.logWarrning(
                "break force cannot exceed {0}. break force set to {1}".format(
                    self.__max_break_force, self.__max_break_force
                )
            )

        LoggingSystem.logInfo(
            "{0} breaks force increased by force of {1}".format(
                self.__break_position.value, self.__current_break_force
            )
        )

    def decreaseBreakForce(self, force: int):
        """Decreases the break force to the force value. break force value cannot exceed max_break_force"""
        self.__current_break_force -= force

        if self.__current_break_force < self.__min_break_force:
            self.__current_break_force = self.__min_break_force
            return LoggingSystem.logWarrning(
                "break force cannot be below {0}. break force set to {1}".format(
                    self.__min_break_force, self.__min_break_force
                )
            )

        LoggingSystem.logInfo(
            "{0} breaks force decreased by force of {1}".format(
                self.__break_position.value, self.__current_break_force
            )
        )

    def getCurrentBreakForce(self):
        """Returns current break force"""
        LoggingSystem.logInfo(
            "Current break force is {0}".format(self.__current_break_force)
        )
        return self.__current_break_force

    def getMinBreakForce(self):
        """Returns min break force"""
        LoggingSystem.logInfo(
            "Min break force is {0}".format(self.__min_break_force)
        )
        return self.__min_break_force

    def getMaxBreakForce(self):
        """Returns max break force"""
        LoggingSystem.logInfo(
            "Max break force is {0}".format(self.__max_break_force)
        )
        return self.__max_break_force
