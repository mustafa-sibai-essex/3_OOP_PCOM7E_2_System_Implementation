from drivetrain.breaks.breakPosition import BreakPosition
from drivetrain.breaks.vehicleBreak import VehicleBreak


class BreaksManager:
    """BreaksManager class controls all four breaks in the vehicle"""

    def __init__(self):
        """Creates BreaksManager class object"""

        self.__breaks = [
            VehicleBreak(BreakPosition.FRONT_BREAK),
            VehicleBreak(BreakPosition.FRONT_BREAK),
            VehicleBreak(BreakPosition.REAR_BREAK),
            VehicleBreak(BreakPosition.REAR_BREAK),
        ]
        """Front breaks are index 0 and 1. Rear breaks are index 2 and 3"""

    def increaseFrontBreaksForce(self, force: int):
        """Increase the force of the front breaks. Breaks force cannot exceed max break force"""
        self.__breaks[0].increaseBreakForce(force)
        self.__breaks[1].increaseBreakForce(force)

    def decreaseFrontBreaksForce(self, force: int):
        """Decreases the force of the front breaks. Breaks force cannot exceed max break force"""
        self.__breaks[0].decreaseBreakForce(force)
        self.__breaks[1].decreaseBreakForce(force)

    def increaseRearBreaksForce(self, force: int):
        """Increase the force of the rear breaks. Breaks force cannot exceed max break force"""
        self.__breaks[2].increaseBreakForce(force)
        self.__breaks[3].increaseBreakForce(force)

    def decreaseRearBreaksForce(self, force: int):
        """Decreases the force of the rear breaks. Breaks force cannot exceed max break force"""
        self.__breaks[2].decreaseBreakForce(force)
        self.__breaks[3].decreaseBreakForce(force)

    def turnOnParkingBreaks(self):
        """Sets the force of all four breaks to 100% which is maximum breaks force"""
        for vehicleBreak in self.__breaks:
            vehicleBreak.increaseBreakForce(vehicleBreak.getMaxBreakForce())

    def turnOffParkingBreaks(self):
        """Sets the force of all four breaks to 0% which is minimum breaks force"""
        for vehicleBreak in self.__breaks:
            vehicleBreak.decreaseBreakForce(vehicleBreak.getMaxBreakForce())
