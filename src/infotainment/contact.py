import datetime
from infotainment.contactType import ContactType
from .basicContact import BasicContact


class Contact(BasicContact):
    def __init__(
        self,
        name: str,
        phone_number: str,
        contact_type: ContactType,
        email: str,
        birthdate: datetime,
    ):
        BasicContact.__init__(self, name, phone_number, contact_type)
        self.email = email
        self.birthdate = birthdate

    def __str__(self):
        return """{0}
Email: {1}
Birthdate: {2}""".format(
            BasicContact.__str__(self), self.email, self.birthdate
        )
