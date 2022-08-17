from alert import Alert
from security.entranceManager import EntranceManager
from vehicle import Vehicle

alert = Alert()
alert.setAlertVolumeLevel(20)

entranceManager = EntranceManager()
entranceManager.LockAllEntrances()
entranceManager.UnlockFrontDoors()
entranceManager.UnlockBackDoors()
entranceManager.UnlockTrunk()
entranceManager.LockAllEntrances()
entranceManager.UnlockAllEntrances()

entranceManager.LockFrontDoors()
entranceManager.LockBackDoors()
entranceManager.LockTrunk()
entranceManager.UnlockAllEntrances()
entranceManager.LockAllEntrances()

vehicle = Vehicle()
