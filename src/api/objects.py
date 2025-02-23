from dataclasses import dataclass
from enum import Enum

from api.enums import UserType, BroadcasterType, VideoType


@dataclass
class Pagination:
    cursor: str

    def __iter__(self):
        return iter(self.__dict__.items())

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


@dataclass
class MutedSegment:
    duration: int
    offset: int

    def __iter__(self):
        return iter(self.__dict__.items())


@dataclass
class Video:
    id: str
    stream_id: str | None
    user_id: str
    user_login: str
    user_name: str
    title: str
    description: str
    created_at: int
    published_at: int
    url: str
    thumbnail_url: str
    viewable: str
    view_count: int
    language: str
    type: VideoType
    duration: str
    muted_segments: list[MutedSegment]

    def __repr__(self):
        attributes = ", ".join(
            f"{key}={value if isinstance(value, Enum) else repr(value)}"
            for key, value in self.__dict__.items()
        )
        return f"Video({attributes})"

    def __iter__(self):
        return iter(self.__dict__.items())

@dataclass
class Clip:
    id: str
    url: str
    embed_url: str
    broadcaster_id: str
    broadcaster_name: str
    creator_id: str
    creator_name: str
    video_id: str | None
    game_id: str
    language: str
    title: str
    view_count: int
    created_at: int
    thumbnail_url: str
    duration: float
    vod_offset: int
    is_featured: bool

    def __iter__(self):
        return iter(self.__dict__.items())
