from alert import Alert
from loggingSystem import LoggingSystem
from security.entranceManager import EntranceManager
from vehicle import Vehicle


alert = Alert()
alert.setAlertVolumeLevel(20)

entranceManager = EntranceManager()
entranceManager.lockAllEntrances()
entranceManager.unlockFrontDoors()
entranceManager.unlockBackDoors()
entranceManager.unlockTrunk()
entranceManager.lockAllEntrances()
entranceManager.unlockAllEntrances()

entranceManager.lockFrontDoors()
entranceManager.lockBackDoors()
entranceManager.lockTrunk()
entranceManager.unlockAllEntrances()
entranceManager.lockAllEntrances()

vehicle = Vehicle()
