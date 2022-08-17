from security.entranceType import EntranceType


class Entrance:
    def __init__(self, entranceType: EntranceType):
        self._locked = False
        self._entranceType = entranceType

    def Lock(self):
        self._locked = True

    def Unlock(self):
        self._locked = False
