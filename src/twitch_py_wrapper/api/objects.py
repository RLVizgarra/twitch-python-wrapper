from dataclasses import dataclass, field
from typing import Literal

from twitch_py_wrapper.api.enums import *
from twitch_py_wrapper.shared_enums import SubscriptionType
from twitch_py_wrapper.shared_objects import NotificationTransport, Objects


# https://dev.twitch.tv/docs/api/guide/#pagination
@dataclass(frozen=True)
class Pagination(Objects):
    cursor: str

@dataclass(frozen=True)
class CheerTier(Objects):
    min_bits: int
    id: Literal["1", "100", "500", "1000", "5000", "10000", "10000"]
    color: str
    images: tuple[tuple[str, str], ...]
    can_cheer: bool
    show_in_bits_card: bool

@dataclass(frozen=True)
class Cheermote(Objects):
    prefix: str
    tiers: tuple[CheerTier, ...]
    type: CheermoteType
    order: int
    last_update: int
    is_charitable: bool

@dataclass(frozen=True)
class Channel(Objects):
    broadcaster_id: str
    broadcaster_login: str
    broadcaster_name: str
    broadcaster_language: str
    game_name: str
    game_id: str
    title: str
    delay: int
    tags: tuple[str, ...]
    content_classification_labels: tuple[ContentClassificationLabelId, ...]
    is_branded_content: bool

@dataclass(frozen=True)
class Emote(Objects):
    id: str
    name: str
    images: tuple[tuple[str, str], ...]
    tier: str | None
    emote_type: EmoteType | None
    emote_set_id: str | None
    owner_id: str | None
    format: tuple[EmoteFormat, ...]
    scale: tuple[Literal["1.0", "2.0", "3.0"], ...]
    theme_mode: tuple[EmoteThemeMode, ...]

@dataclass(frozen=True)
class ChatBadge(Objects):
    id: str
    image_url_1x: str
    image_url_2x: str
    image_url_4x: str
    title: str
    description: str
    click_action: str | None
    click_url: str | None

@dataclass(frozen=True)
class ChatBadgeSet(Objects):
    set_id: str
    versions: tuple[ChatBadge, ...]

@dataclass(frozen=True)
class ChatSettings(Objects):
    broadcaster_id: str
    emote_mode: bool
    follower_mode: bool
    follower_mode_duration: int | None
    moderator_id: str | None
    non_moderator_chat_delay: bool | None
    non_moderator_chat_delay_duration: int | None
    slow_mode: bool
    slow_mode_wait_time: int | None
    subscriber_mode: bool
    unique_chat_mode: bool

@dataclass(frozen=True)
class SharedChatSessionParticipant(Objects):
    broadcaster_id: str

@dataclass(frozen=True)
class SharedChatSession(Objects):
    session_id: str
    host_broadcaster_id: str
    participants: tuple[SharedChatSessionParticipant, ...]
    created_at: int
    updated_at: int

@dataclass(frozen=True)
class UserChatColor(Objects):
    user_id: str
    user_login: str
    user_name: str
    color: str | None

@dataclass(frozen=True)
class Clip(Objects):
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

@dataclass(frozen=True)
class Conduit(Objects):
    id: str
    shard_count: int

@dataclass
class ConduitShard(Objects):
    id: str
    status: ConduitShardStatus
    transport: NotificationTransport

@dataclass(frozen=True)
class ContentClassificationLabel(Objects):
    id: ContentClassificationLabelId
    description: str
    name: str

@dataclass(frozen=True)
class Subscription(Objects):
    id: str
    status: Literal["enabled", "webhook_callback_verification_pending"]
    type: SubscriptionType
    version: str
    condition: tuple[tuple[str, str], ...]
    created_at: int
    transport: NotificationTransport
    cost: int

@dataclass(frozen=True)
class User(Objects):
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


@dataclass(frozen=True)
class MutedSegment(Objects):
    duration: int
    offset: int


@dataclass(frozen=True)
class Video(Objects):
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
