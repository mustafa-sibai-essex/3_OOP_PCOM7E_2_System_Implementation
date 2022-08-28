from loggingSystem import LoggingSystem


class VehicleBreak:
    """VehicleBreak class controls a single break in the vehicle"""

    def __init__(self):
        """Creates the break object and sets max and current break force"""
        self.__max_break_force = 100
        self.__min_break_force = 0
        self.__current_break_force = self.__min_break_force

    def applyBreak(self, force: int):
        """Sets the break force to the force value. break force value cannot exceed max_break_force"""
        self.__current_break_force = force

        if self.__current_break_force > self.__max_break_force:
            self.__current_break_force = self.__max_break_force
            LoggingSystem.logWarrning(
                "break force cannot exceed {0}. break force set to {1}".format(
                    self.__max_break_force, self.__max_break_force
                )
            )

    def getCurrentBreakForce(self):
        """Returns current break force"""
        return self.__current_break_force

    def getMinBreakForce(self):
        """Returns min break force"""
        return self.__min_break_force

    def getMaxBreakForce(self):
        """Returns max break force"""
        return self.__max_break_force
