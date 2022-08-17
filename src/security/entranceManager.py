from security.door import Door
from .entranceType import EntranceType
from security.trunk import Trunk


class EntranceManager:
    def __init__(self):
        self._front_doors = [
            Door(EntranceType.FRONT_DOOR),
            Door(EntranceType.FRONT_DOOR),
        ]
        self._back_doors = [Door(EntranceType.BACK_DOOR), Door(EntranceType.BACK_DOOR)]
        self._trunk = Trunk(EntranceType.TRUNK)

    def UnlockFrontDoors(self):
        for front_door in self._front_doors:
            front_door.Unlock()

    def UnlockBackDoors(self):
        for back_door in self._back_doors:
            back_door.Unlock()

    def UnlockTrunk(self):
        self._trunk.Unlock()

    def UnlockAllEntrances(self):
        self.UnlockFrontDoors()
        self.UnlockBackDoors()
        self.UnlockTrunk()

    def LockFrontDoors(self):
        for front_door in self._front_doors:
            front_door.Lock()

    def LockBackDoors(self):
        for back_door in self._back_doors:
            back_door.Lock()

    def LockTrunk(self):
        self._trunk.Lock()

    def LockAllEntrances(self):
        self.LockFrontDoors()
        self.LockBackDoors()
        self.LockTrunk()
