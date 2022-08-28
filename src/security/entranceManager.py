from security.door import Door
from .entranceType import EntranceType
from security.trunk import Trunk


class EntranceManager:
    """EntranceManager class controls all of the vehicle entrances"""

    def __init__(self):
        """Creates the entrance manager object"""
        self.__front_doors = [
            Door(EntranceType.FRONT_DOOR),
            Door(EntranceType.FRONT_DOOR),
        ]
        self.__back_doors = [Door(EntranceType.BACK_DOOR), Door(EntranceType.BACK_DOOR)]
        self.__trunk = Trunk(EntranceType.TRUNK)

    def unlockFrontDoors(self):
        """Unlocks all front doors"""
        for front_door in self.__front_doors:
            front_door.unlock()

    def unlockBackDoors(self):
        """Unlocks all back doors"""
        for back_door in self.__back_doors:
            back_door.unlock()

    def unlockTrunk(self):
        """Unlocks the trunk"""
        self.__trunk.unlock()

    def unlockAllEntrances(self):
        """Unlocks all entrances including front doors, back doors, and the trunk"""
        self.unlockFrontDoors()
        self.unlockBackDoors()
        self.unlockTrunk()

    def lockFrontDoors(self):
        """Locks all the front doors"""
        for front_door in self.__front_doors:
            front_door.lock()

    def lockBackDoors(self):
        """Locks all the back doors"""
        for back_door in self.__back_doors:
            back_door.lock()

    def lockTrunk(self):
        """Locks the trunk"""
        self.__trunk.lock()

    def lockAllEntrances(self):
        """Locks all entrances including front doors, back doors, and the trunk"""
        self.lockFrontDoors()
        self.lockBackDoors()
        self.lockTrunk()
