from dataclasses import dataclass, field
from typing import Literal

from api.enums import *
from shared_enums import SubscriptionType
from shared_objects import SubscriptionTransport


# https://dev.twitch.tv/docs/api/guide/#pagination
@dataclass(frozen=True)
class Pagination:
    cursor: str

    def __iter__(self):
        return iter(self.__dict__.items())

@dataclass(frozen=True)
class CheerTier:
    min_bits: int
    id: Literal["1", "100", "500", "1000", "5000", "10000", "10000"]
    color: str
    images: tuple[tuple[str, str], ...]
    can_cheer: bool
    show_in_bits_card: bool

    def __iter__(self):
        return iter(self.__dict__.items())

@dataclass(frozen=True)
class Cheermote:
    prefix: str
    tiers: tuple[CheerTier, ...]
    type: CheermoteType
    order: int
    last_update: int
    is_charitable: bool

    def __repr__(self):
        attributes = ", ".join(
            f"{key}={value if isinstance(value, Enum) else repr(value)}"
            for key, value in self.__dict__.items()
        )
        return f"Cheermote({attributes})"

    def __iter__(self):
        return iter(self.__dict__.items())

@dataclass(frozen=True)
class Channel:
    broadcaster_id: str
    broadcaster_login: str
    broadcaster_name: str
    broadcaster_language: str
    game_name: str
    game_id: str
    title: str
    delay: int
    tags: tuple[str, ...]
    content_classification_labels: tuple[Literal["DebatedSocialIssuesAndPolitics", "DrugsIntoxication", "Gambling", "MatureGame", "ProfanityVulgarity", "SexualThemes", "ViolentGraphic"], ...]
    is_branded_content: bool

@dataclass(frozen=True)
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
    view_count: int = field(hash=False)
    created_at: int
    thumbnail_url: str
    duration: float
    vod_offset: int
    is_featured: bool

    def __iter__(self):
        return iter(self.__dict__.items())

@dataclass(frozen=True)
class Subscription:
    id: str
    status: Literal["enabled", "webhook_callback_verification_pending"]
    type: SubscriptionType
    version: str
    condition: tuple[tuple[str, str], ...]
    created_at: int
    transport: SubscriptionTransport
    cost: int

@dataclass(frozen=True)
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


@dataclass(frozen=True)
class MutedSegment:
    duration: int
    offset: int

    def __iter__(self):
        return iter(self.__dict__.items())


@dataclass(frozen=True)
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
    view_count: int = field(hash=False)
    language: str
    type: VideoType
    duration: str
    muted_segments: tuple[MutedSegment, ...]

    def __repr__(self):
        attributes = ", ".join(
            f"{key}={value if isinstance(value, Enum) else repr(value)}"
            for key, value in self.__dict__.items()
        )
        return f"Video({attributes})"

    def __iter__(self):
        return iter(self.__dict__.items())
