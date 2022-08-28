import abc


class HealthSensor(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def measure(self):
        pass

    @abc.abstractclassmethod
    def inRange(self):
        pass
