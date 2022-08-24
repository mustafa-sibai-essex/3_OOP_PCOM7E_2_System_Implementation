from drivetrain.breakManager import BreakManager
from drivetrain.engine import Engine
from drivetrain.steering import Steering


class Drivetrain:
    def __init__(self):
        self._steering = Steering()
        self._engine = Engine()
        self._breaks_manager = BreakManager()
