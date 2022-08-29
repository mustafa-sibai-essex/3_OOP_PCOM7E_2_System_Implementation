from enum import Enum


class ConnectionState(Enum):
    """ConnectionState has different state types"""

    NOT_CONNECTED = "Not connected"
    """Not connected state"""

    CONNECTING = "Connecting"
    """Connecting state"""

    FAILED_TO_CONNECT = "Failed to connect"
    """Failed to connect state"""

    CONNECTED = "Connected"
    """Connected state"""

    DISCONNECTING = "Disconnecting"
    """Disconnecting state"""

    FAILED_TO_DISCONNECT = "Failed to disconnect"
    """Failed to disconnect state"""

    DISCONNECTED = "Disconnected"
    """Disconnected state"""
