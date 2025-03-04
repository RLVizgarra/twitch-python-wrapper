from dataclasses import dataclass
from typing import Literal

from twitch_py_wrapper.enums import SubscriptionType
from twitch_py_wrapper.eventsub.enums import MessageType
from twitch_py_wrapper.objects import Objects


@dataclass(frozen=True)
class Metadata(Objects):
    message_id: str
    message_type: MessageType
    message_timestamp: int
    subscription_type: SubscriptionType | Literal["builtins.connected"] | None
    subscription_version: str | None
