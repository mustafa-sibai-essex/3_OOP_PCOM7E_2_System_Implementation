from enum import Enum


class EntranceType(Enum):
    """EntranceType class represents different types of entrances like front door, back door and the trunk"""

    FRONT_DOOR = "Front Door"
    """Entrance front door enum"""

    BACK_DOOR = "Back Door"
    """Entrance back door enum"""

    TRUNK = "Trunk"
    """Entrance trunk enum"""
