from dataclasses import dataclass
from typing import Literal

from event.enums import MessageType
from shared_enums import SubscriptionType


@dataclass(frozen=True)
class Metadata:
    message_id: str
    message_type: MessageType
    message_timestamp: int
    subscription_type: SubscriptionType | Literal["builtins.connected"] | None
    subscription_version: str | None

    def __iter__(self):
        return iter(self.__dict__.items())
