from autopilot.autopilotState import AutopilotState
from drivetrain.drivetrain import Drivetrain
from drivetrain.engine.engineState import EngineState
from loggingSystem import LoggingSystem
from objectDetection.objectDetection import ObjectDetection


class Autopilot:
    def __init__(self, drivetrain: Drivetrain):
        self.__objectDetection = ObjectDetection()
        self.__drivetrain = drivetrain
        self.__autopilot_state = AutopilotState.AUTOPILOT_OFF

    def getObjectDetection(self):
        return self.__objectDetection

    def getDrivetrain(self):
        return self.__drivetrain

    def turnOnAutopilot(self):
        if self.__drivetrain.getEngine().getEngineState() == EngineState.ENGINE_OFF:
            return LoggingSystem.logError("Cannot turn on autopilot when engine is off")

        if self.__autopilot_state == AutopilotState.AUTOPILOT_ON:
            return LoggingSystem.logError("Autopilot is already on")

        self.__objectDetection.detectObjectsFromImage()
        LoggingSystem.logInfo("Autopilot is on")

    def turnOffAutopilot(self):
        if self.__autopilot_state == AutopilotState.AUTOPILOT_OFF:
            return LoggingSystem.logError("Autopilot is already off")

        LoggingSystem.logInfo("Autopilot is off")
