from enum import Enum


class MessageType(str, Enum):
    SESSION_WELCOME = "session_welcome"
    SESSION_KEEPALIVE = "session_keepalive"
    NOTIFICATION = "notification"
    SESSION_RECONNECT = "session_reconnect"
    REVOCATION = "revocation"

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"
