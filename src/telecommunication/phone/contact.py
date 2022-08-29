from telecommunication.phone.contactType import ContactType
from .basicContact import BasicContact


class Contact(BasicContact):
    """Conctact class inherits from BasicContact and contains name, phone number, and email"""

    def __init__(
        self, name: str, phone_number: str, contact_type: ContactType, email: str
    ):
        """Sets the contact name, phone number email and contact type"""
        BasicContact.__init__(self, name, phone_number, contact_type)
        self.__email = email

    def __str__(self):
        """Prints the contact information like name, phone number, and email"""
        return """{0}
Email: {1}""".format(
            BasicContact.__str__(self), self.__email
        )

    def getEmail(self):
        """Returns the contact email address"""
        return self.__email
