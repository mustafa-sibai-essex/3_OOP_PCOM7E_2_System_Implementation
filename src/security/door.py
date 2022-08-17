from security.entrance import Entrance
from security.entranceType import EntranceType


class Door(Entrance):
    def __init__(self, entranceType: EntranceType):
        Entrance.__init__(self, entranceType)
        pass

    def Lock(self):
        Entrance.Lock(self)
        print("{0} Locked".format(self._entranceType.value))

    def Unlock(self):
        Entrance.Unlock(self)
        print("{0} Unlocked".format(self._entranceType.value))
