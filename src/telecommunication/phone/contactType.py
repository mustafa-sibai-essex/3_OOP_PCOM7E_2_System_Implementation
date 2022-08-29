from enum import Enum


class ContactType(Enum):
    """ContactType includes different contact types like owner, normal and emergency contact"""

    OWNER = "Owner"
    """Owner contact type"""

    NORMAL = "Normal"
    """Normal contact type"""

    EMERGENCY = "Emergency"
    """Emergency contact type"""
