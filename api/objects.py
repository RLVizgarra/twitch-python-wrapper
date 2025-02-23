from dataclasses import dataclass
from enum import Enum

from api.enums import UserType, BroadcasterType

@dataclass
class User:
    id: str
    login: str
    display_name: str
    type: UserType
    broadcaster_type: BroadcasterType
    description: str
    profile_image_url: str
    offline_image_url: str
    email: str | None
    created_at: int

    def __repr__(self):
        attributes = ", ".join(
            f"{key}={value if isinstance(value, Enum) else repr(value)}"
            for key, value in self.__dict__.items()
        )
        return f"User({attributes})"

    def __iter__(self):
        return iter(self.__dict__.items())
