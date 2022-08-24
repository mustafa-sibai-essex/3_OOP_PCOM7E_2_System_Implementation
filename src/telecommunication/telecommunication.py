from telecommunication.cloudServer import CloudServer
from telecommunication.email.emailManager import EmailManager
from telecommunication.gps import GPS
from telecommunication.sms.smsManager import SMSManager


class Telecommunication:
    def __init__(self):
        self._gps = GPS()
        self._sms_manager = SMSManager()
        self._email_manager = EmailManager()
        self._cloud_server = CloudServer()
