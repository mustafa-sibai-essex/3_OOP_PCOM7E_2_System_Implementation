from datetime import date
from autopilot import Autopilot
from drivetrain.drivetrain import Drivetrain
from infotainment.contactType import ContactType
from infotainment.contact import Contact
from infotainment.infotainment import Infotainment


class Vehicle:
    def __init__(self):
        self.drivetrain = Drivetrain()
        self.autopilot = Autopilot(self.drivetrain)
        self.infotainment = Infotainment()
        self.infotainment.getPhone().getPhoneBook().addContact(
            Contact(
                "Mustafa Sibai",
                "+971557716033",
                ContactType.NORMAL,
                "contact@m-sibai.com",
                date.today(),
            )
        )
        print(self.infotainment.getPhone().getPhoneBook())

        print(
            self.autopilot.getObjectDetection().getCamera().getFrameBuffer().getWidth()
        )
        print(
            self.autopilot.getObjectDetection().getCamera().getFrameBuffer().getHeight()
        )
        print(
            len(
                self.autopilot.getObjectDetection()
                .getCamera()
                .getFrameBuffer()
                .getColorBuffer()
            )
        )
        print(
            self.autopilot.getObjectDetection()
            .getCamera()
            .getFrameBuffer()
            .getColorBuffer()[0]
        )

    def start(self):
        pass
