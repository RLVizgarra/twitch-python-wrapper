from dataclasses import dataclass
from typing import Literal


@dataclass
class SubscriptionTransport:
    method: Literal["webhook", "websocket", "conduit"]
    callback: str = None
    secret: str = None
    session_id: str = None
    conduit_id: str = None

    def __iter__(self):
        return iter(self.__dict__.items())