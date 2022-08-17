from infotainment.contactType import ContactType


class BasicContact:
    def __init__(self, name: str, phone_number: str, contact_type: ContactType):
        self.name = name
        self.phone_number = phone_number
        self.contact_type = contact_type

    def __str__(self):
        return """Name: {0}
Phone Number: {1}""".format(
            self.name, self.phone_number
        )
