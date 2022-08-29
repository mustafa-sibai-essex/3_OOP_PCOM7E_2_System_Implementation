from drivetrain.breaksManager import BreaksManager
from drivetrain.engine.engine import Engine
from drivetrain.steering import Steering


class Drivetrain:
    """Drivertrain class contains the steering, engine, and breaks maanger"""

    def __init__(self):
        """Creates the steering, engine and breaks manager objects"""
        self.__steering = Steering()
        self.__engine = Engine()
        self.__breaks_manager = BreaksManager()

    def getSteering(self):
        """Returns the Steering object"""
        return self.__steering

    def getEngine(self):
        """Returns the Engine object"""
        return self.__engine

    def getBreaksManager(self):
        """Returns the BreaksManager object"""
        return self.__breaks_manager
