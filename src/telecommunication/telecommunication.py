from telecommunication.cloudServer import CloudServer
from telecommunication.email.emailManager import EmailManager
from telecommunication.gps import GPS
from telecommunication.satellite import Satellite
from telecommunication.sms.smsManager import SMSManager


class Telecommunication:
    def __init__(self):
        self.__satellite = Satellite()
        self.__gps = GPS()
        self.__sms_manager = SMSManager()
        self.__email_manager = EmailManager()
        self.__cloud_server = CloudServer()

    def getSatellite(self):
        """Returns the satellite object"""
        return self.__satellite

    def connectToSatellite(self):
        pass

    def connectToInternet(self):
        pass

    def sendGPSLocationViaSMS(self):
        pass
