from loggingSystem import LoggingSystem
from security.entrances.entrance import Entrance
from security.entrances.entranceType import EntranceType


class Trunk(Entrance):
    """Trunk class represents and controls the trunk"""

    def __init__(self, entrance_type: EntranceType):
        """Creates the trunk object and initializes the entrance class"""
        Entrance.__init__(self, entrance_type)

    def lock(self):
        """Sets the trunk state to locked"""
        Entrance._lock(self)
        LoggingSystem.logInfo("{0} Locked".format(self._entrance_type.value))

    def unlock(self):
        """Sets the trunk state to unlocked"""
        Entrance._unlock(self)
        LoggingSystem.logInfo("{0} Unlocked".format(self._entrance_type.value))
