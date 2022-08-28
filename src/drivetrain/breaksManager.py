from drivetrain.vehicleBreak import VehicleBreak


class BreaksManager:
    """BreaksManager class controls all four breaks in the vehicle"""

    def __init__(self):
        """Creates BreaksManager class object"""

        self.__breaks = [VehicleBreak(), VehicleBreak(), VehicleBreak(), VehicleBreak()]
        """Front breaks are index 0 and 1. Rear breaks are index 2 and 3"""

    def applyFrontBreaks(self, force: int):
        """Sets the force of the front breaks. Breaks force cannot exceed max break force"""
        self.__breaks[0].applyBreak(force)
        self.__breaks[1].applyBreak(force)

    def applyRearBreaks(self, force: int):
        """Sets the force of the rear breaks. Breaks force cannot exceed max break force"""
        self.__breaks[2].applyBreak(force)
        self.__breaks[3].applyBreak(force)

    def turnOnParkingBreaks(self):
        """Sets the force of all four breaks to 100% which is maximum breaks force"""
        for vehicleBreak in self.__breaks:
            vehicleBreak.applyBreak(vehicleBreak.getMaxBreakForce())

    def turnOffParkingBreaks(self):
        """Sets the force of all four breaks to 0% which is minimum breaks force"""
        for vehicleBreak in self.__breaks:
            vehicleBreak.applyBreak(vehicleBreak.getMinBreakForce())
