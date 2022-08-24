from loggingSystem import LoggingSystem


class Engine:
    def __init__(self):
        self._max_rpm = 7000
        self._idle_rpm = 900
        self._max_torque = 500
        self._max_speed = 200
        self._current_rpm = 0
        self._current_torque = 0
        self._current_speed = 0

    def start(self):
        LoggingSystem.logInfo("Engine started!")
        self._current_rpm = self._idle_rpm

    def stop(self):
        LoggingSystem.logInfo("Engine stopped")
        self._current_rpm = 0

    def accelerate(self):
        LoggingSystem.logInfo("Engine accelerating")
        self._current_rpm += 100
        self._current_speed += 10
        self._current_rpm = min(self._current_rpm, self._max_rpm)
        self._current_speed = min(self._current_speed, self._max_speed)

    def decelerate(self):
        LoggingSystem.logInfo("Engine decelerating")
        self._current_rpm -= 100
        self._current_speed -= 10
        self._current_rpm = max(self._current_rpm, self._idle_rpm)
        self._current_speed = max(self._current_speed, 0)
