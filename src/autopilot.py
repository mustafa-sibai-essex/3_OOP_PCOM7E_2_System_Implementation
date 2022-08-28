from drivetrain.drivetrain import Drivetrain
from objectDetection.objectDetection import ObjectDetection


class Autopilot:
    def __init__(self, drivetrain: Drivetrain):
        self.__objectDetection = ObjectDetection()
        self.__drivetrain = drivetrain

    def getObjectDetection(self):
        return self.__objectDetection

    def getDrivetrain(self):
        return self.__drivetrain

    def turnOnAutopilot(self):
        pass

    def turnOffAutopilot(self):
        pass
