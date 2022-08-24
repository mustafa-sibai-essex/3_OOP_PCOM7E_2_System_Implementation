from datetime import date
from autopilot import Autopilot
from infotainment.contactType import ContactType
from infotainment.contact import Contact
from infotainment.infotainment import Infotainment
from logging import Logging

class Vehicle:
    def __init__(self):
        self.logging = Logging()
        self.autopilot = Autopilot()
        self.infotainment = Infotainment()
        self.infotainment.phone.getPhoneBook().addContact(
            Contact(
                "Mustafa Sibai",
                "+971557716033",
                ContactType.NORMAL,
                "contact@m-sibai.com",
                date.today(),
            )
        )
        print(self.infotainment.getPhone().getPhoneBook())

        print(self.autopilot.objectDetection.getCamera().getFrameBuffer().getWidth())
        print(self.autopilot.objectDetection.getCamera().getFrameBuffer().getHeight())
        print(
            len(
                self.autopilot.objectDetection.getCamera()
                .getFrameBuffer()
                .getColorBuffer()
            )
        )
        print(
            self.autopilot.objectDetection.getCamera()
            .getFrameBuffer()
            .getColorBuffer()[0]
        )

    def start(self):
        pass