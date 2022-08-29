from drivetrain.engine.engineState import EngineState
from loggingSystem import LoggingSystem


class Engine:
    """Engine class is responsible for managing the vehicle engine"""

    def __init__(self):
        """Creates the vehicle engine class object and sets the engine rpm, torque and speed"""
        self.__current_engine_state = EngineState.ENGINE_OFF

        self.__max_rpm = 7000
        self.__min_rpm = 0
        self.__idle_rpm = 900
        self.__current_rpm = self.__min_rpm

        self.__max_torque = 500
        self.__min_torque = 0
        self.__current_torque = self.__min_torque

        self.__max_speed = 200
        self.__min_speed = 0
        self.__current_speed = self.__min_speed

    def start(self):
        """Starts the vehicle engine"""

        if self.__current_engine_state == EngineState.ENGINE_ON:
            return LoggingSystem.logError("Engine is already on")

        self.__current_engine_state = EngineState.ENGINE_ON
        self.__current_speed = self.__min_speed
        self.__current_rpm = self.__idle_rpm
        self.__current_torque = self.__min_torque
        LoggingSystem.logInfo("Engine started!")

    def stop(self):
        """Stops the vehicle engine"""

        if self.__current_engine_state == EngineState.ENGINE_OFF:
            return LoggingSystem.logError("Engine is already off")

        self.__current_engine_state = EngineState.ENGINE_OFF
        self.__current_speed = self.__min_speed
        self.__current_rpm = self.__min_rpm
        self.__current_torque = self.__min_torque
        LoggingSystem.logInfo("Engine stopped")

    def accelerate(self):
        """Accelerates the vehicle engine"""

        if self.__current_engine_state != EngineState.ENGINE_ON:
            return LoggingSystem.logError("Cannot accelerate when engine is off")

        self.__current_rpm += 305
        self.__current_speed += 10

        if self.__current_rpm > self.__max_rpm:
            self.__current_rpm = self.__max_rpm
            LoggingSystem.logWarrning(
                """Current engine RPM cannot exceed {0}. 
Engine RPM has been set to the max value of {1}""".format(
                    self.__max_rpm, self.__max_rpm
                )
            )

        if self.__current_speed > self.__max_speed:
            self.__current_speed = self.__max_speed
            return LoggingSystem.logWarrning(
                """Vehicle speed cannot exceed {0}. 
Vehicle speed set to the max value of {1}""".format(
                    self.__max_speed, self.__max_speed
                )
            )

        LoggingSystem.logInfo(
            "Engine accelerating. Current RPM is {0}, and speed is {1}".format(
                self.__current_rpm, self.__current_speed
            )
        )

    def decelerate(self):
        """Decelerate the vehicle engine"""

        if self.__current_engine_state != EngineState.ENGINE_ON:
            return LoggingSystem.logError("Cannot decelerate when engine is off")

        self.__current_rpm -= 305
        self.__current_speed -= 10

        if self.__current_rpm < self.__min_rpm:
            self.__current_rpm = self.__min_rpm
            LoggingSystem.logWarrning(
                """Current engine RPM cannot be below {0}. 
Engine RPM has been set to the min value of {1}""".format(
                    self.__min_rpm, self.__min_rpm
                )
            )

        if self.__current_speed < self.__min_speed:
            self.__current_speed = self.__min_speed
            return LoggingSystem.logWarrning(
                """Vehicle speed cannot be below {0}. 
Vehicle speed set to the min value of {1}""".format(
                    self.__min_speed, self.__min_speed
                )
            )

        LoggingSystem.logInfo(
            "Engine decelerating. Current RPM is {0}, and speed is {1}".format(
                self.__current_rpm, self.__current_speed
            )
        )

    def getEngineState(self):
        return self.__current_engine_state
