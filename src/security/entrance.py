from security.entranceType import EntranceType


class Entrance:
    """Entrance class represents a single entrance of a vehicle whether its a door or the trunk"""

    def __init__(self, entrance_type: EntranceType):
        """Creates the entrance object"""
        self._locked = False
        self._entrance_type = entrance_type

    def _lock(self):
        """Sets the entrance state to locked"""
        self._locked = True

    def _unlock(self):
        """Sets the entrance state to unlocked"""
        self._locked = False
