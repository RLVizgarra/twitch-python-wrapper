from dataclasses import dataclass
from enum import Enum

from shared_enums import NotificationTransportMethod


class Objects:
    def __repr__(self):
        attributes = ", ".join(
            f"{key}={value if isinstance(value, Enum) else repr(value)}"
            for key, value in self.__dict__.items()
        )
        return f"Cheermote({attributes})"

    def __iter__(self):
        return iter(self.__dict__.items())

@dataclass
class NotificationTransport(Objects):
    method: NotificationTransportMethod
    callback: str = None
    secret: str = None
    session_id: str = None
    conduit_id: str = None
