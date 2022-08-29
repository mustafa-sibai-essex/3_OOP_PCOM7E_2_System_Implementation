from loggingSystem import LoggingSystem
from security.entrances.entrance import Entrance
from security.entrances.entranceType import EntranceType


class Door(Entrance):
    """Door class inherits from Entrance and represents a single door"""

    def __init__(self, entrance_type: EntranceType):
        """Creates the door object"""
        Entrance.__init__(self, entrance_type)

    def lock(self):
        """Sets the door state to locked"""
        Entrance._lock(self)
        LoggingSystem.logInfo("{0} Locked".format(self._entrance_type.value))

    def unlock(self):
        """Sets the door state to unlocked"""
        Entrance._unlock(self)
        LoggingSystem.logInfo("{0} Unlocked".format(self._entrance_type.value))
