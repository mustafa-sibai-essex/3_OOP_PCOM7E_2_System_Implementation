from loggingSystem import LoggingSystem


class Steering:
    """Steering class controls the front wheels steering to the left and right"""

    def __init__(self):
        """Creates the Steering class object and sets current and max wheel y axis rotation"""
        self.__current_wheel_y_axis_rotation = 0
        self.__max_wheel_y_axis_rotation = 60

    def steerRight(self, angle: int):
        """Turns the vehicle front wheels to the right by a certain angle. Wheel turn cannot exceed wheel max y-axis rotation"""
        self.__current_wheel_rotation += angle
        LoggingSystem.logInfo(
            """Vehicle is steering right. Current wheel y-axis rotation {0}""".format(
                self.__current_wheel_y_axis_rotation
            )
        )

        if self.__current_wheel_y_axis_rotation > self.__max_wheel_y_axis_rotation:
            self.__current_wheel_y_axis_rotation = self.__max_wheel_y_axis_rotation
            LoggingSystem.logWarrning(
                """Wheel y-axis rotation cannot exceed {0}. 
Wheel y-axis rotation has been set to the max value of {1}""".format(
                    self.__max_wheel_y_axis_rotation, self.__max_wheel_y_axis_rotation
                )
            )

    def steerLeft(self, angle: int):
        """Turns the vehicle front wheels to the left by a certain angle. Wheel turn cannot exceed wheel max y-axis rotation"""
        self.__current_wheel_rotation -= angle
        LoggingSystem.logInfo(
            "Vehicle is steering left. Current wheel rotation {0}".format(
                self.__current_wheel_rotation
            )
        )

        if self.__current_wheel_y_axis_rotation < -self.__max_wheel_y_axis_rotation:
            self.__current_wheel_y_axis_rotation = -self.__max_wheel_y_axis_rotation

            LoggingSystem.logWarrning(
                """Wheel y-axis rotation cannot exceed {0}. 
Wheel y-axis rotation has been set to the max value of {1}""".format(
                    -self.__max_wheel_y_axis_rotation, -self.__max_wheel_y_axis_rotation
                )
            )
