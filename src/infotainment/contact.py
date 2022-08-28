import datetime
from infotainment.contactType import ContactType
from .basicContact import BasicContact


class Contact(BasicContact):
    """Conctact class inherits from BasicContact and contains name, phone number, email and birthdate"""

    def __init__(
        self,
        name: str,
        phone_number: str,
        contact_type: ContactType,
        email: str,
        birthdate: datetime = datetime(),
    ):
        """Sets the contact name, phone number email, birthdate and contact type"""
        BasicContact.__init__(self, name, phone_number, contact_type)
        self.__email = email
        self.__birthdate = birthdate

    def __str__(self):
        """Prints the contact information like name, phone number, email, and birthdate"""
        return """{0}
Email: {1}
Birthdate: {2}""".format(
            BasicContact.__str__(self), self.__email, self.__birthdate
        )

    def getEmail(self):
        """Returns the contact email address"""
        return self.__email

    def getBirthdate(self):
        """Returns the contact birthdate"""
        return self.__birthdate
