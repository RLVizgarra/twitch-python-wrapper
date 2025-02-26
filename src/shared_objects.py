from dataclasses import dataclass
from typing import Literal

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
class SubscriptionTransport(Objects):
    method: Literal["webhook", "websocket", "conduit"]
    callback: str = None
    secret: str = None
    session_id: str = None
    conduit_id: str = None
