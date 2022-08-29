from enum import Enum


class AutopilotState(Enum):
    """AutopilotState class represents different states of the autopilot like on and off"""

    AUTOPILOT_ON = "Front Door"
    """Autopilot is on enum state"""

    AUTOPILOT_OFF = "Back Door"
    """Autopilot is off enum state"""
