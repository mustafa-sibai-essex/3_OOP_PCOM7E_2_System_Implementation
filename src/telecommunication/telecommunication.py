from telecommunication.cloudServer import CloudServer
from telecommunication.email.emailManager import EmailManager
from telecommunication.gps import GPS
from telecommunication.phone.phone import Phone
from telecommunication.satellite import Satellite
from telecommunication.sms.smsManager import SMSManager


class Telecommunication:
    """Telecommunication class is responsible for everything to deal with communication like Satellite, GPS, and Cloud Server"""

    def __init__(self):
        """Creates the Telecommunication class object and sets up Satellite, GPS, Cloud Server, SMS Manager, and Email Manager"""
        self.__satellite = Satellite()
        self.__gps = GPS(self.__satellite)
        self.__cloud_server = CloudServer(self.__satellite)
        self.__sms_manager = SMSManager(self.__satellite)
        self.__email_manager = EmailManager(self.__satellite)
        self.__phone = Phone(self.__satellite)

    def getSatellite(self):
        """Returns the Satellite object"""
        return self.__satellite

    def getGPS(self):
        """Returns the GPS object"""
        return self.__gps

    def getCloudServer(self):
        """Returns the Cloud Server object"""
        return self.__cloud_server

    def getSMSManager(self):
        """Returns the SMS Manager object"""
        return self.__sms_manager

    def getEmailManager(self):
        """Returns the Email Manager object"""
        return self.__email_manager

    def getPhone(self):
        """Returns the phone object"""
        return self.__phone

    def sendGPSLocationViaSMS(self):
        pass
