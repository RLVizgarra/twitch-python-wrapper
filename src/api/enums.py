from enum import Enum


class CheermoteType(str, Enum):
    GLOBAL_FIRST_PARTY = "global_first_party"
    GLOBAL_THIRD_PARTY = "global_third_party"
    CHANNEL_CUSTOM = "channel_custom"
    DISPLAY_ONLY = "display_only"
    SPONSORED = "sponsored"


class VideoType(str, Enum):
    ARCHIVE = "archive"
    HIGHLIGHT = "highlight"
    UPLOAD = "upload"

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"

class SubscriptionType(str, Enum):
    AUTOMOD_MESSAGE_HOLD = "automod.message.hold"
    AUTOMOD_MESSAGE_UPDATE = "automod.message.update"
    AUTOMOD_SETTINGS_UPDATE = "automod.settings.update"
    AUTOMOD_TERMS_UPDATE = "automod.terms.update"
    CHANNEL_UPDATE = "channel.update"
    CHANNEL_FOLLOW = "channel.follow"
    CHANNEL_AD_BREAK_BEGIN = "channel.ad_break.begin"
    CHANNEL_CHAT_CLEAR = "channel.chat.clear"
    CHANNEL_CHAT_CLEAR_USER_MESSAGES = "channel.chat.clear_user_messages"
    CHANNEL_CHAT_MESSAGE = "channel.chat.message"
    CHANNEL_CHAT_MESSAGE_DELETE = "channel.chat.message_delete"
    CHANNEL_CHAT_NOTIFICATION = "channel.chat.notification"
    CHANNEL_CHAT_SETTINGS_UPDATE = "channel.chat_settings.update"
    CHANNEL_CHAT_USER_MESSAGE_HOLD = "channel.chat.user_message_hold"
    CHANNEL_CHAT_USER_MESSAGE_UPDATE = "channel.chat.user_message_update"
    CHANNEL_SHARED_CHAT_BEGIN = "channel.shared_chat.begin"
    CHANNEL_SHARED_CHAT_UPDATE = "channel.shared_chat.update"
    CHANNEL_SHARED_CHAT_END = "channel.shared_chat.end"
    CHANNEL_SUBSCRIBE = "channel.subscribe"
    CHANNEL_SUBSCRIPTION_END = "channel.subscription.end"
    CHANNEL_SUBSCRIPTION_GIFT = "channel.subscription.gift"
    CHANNEL_SUBSCRIPTION_MESSAGE = "channel.subscription.message"
    CHANNEL_CHEER = "channel.cheer"
    CHANNEL_RAID = "channel.raid"
    CHANNEL_BAN = "channel.ban"
    CHANNEL_UNBAN = "channel.unban"
    CHANNEL_UNBAN_REQUEST_CREATE = "channel.unban_request.create"
    CHANNEL_UNBAN_REQUEST_RESOLVE = "channel.unban_request.resolve"
    CHANNEL_MODERATE = "channel.moderate"
    CHANNEL_MODERATOR_ADD = "channel.moderator.add"
    CHANNEL_MODERATOR_REMOVE = "channel.moderator.remove"
    CHANNEL_CHANNEL_POINTS_AUTOMATIC_REWARD_REDEMPTION_ADD = "channel.channel_points_automatic_reward_redemption.add"
    CHANNEL_CHANNEL_POINTS_CUSTOM_REWARD_ADD = "channel.channel_points_custom_reward.add"
    CHANNEL_CHANNEL_POINTS_CUSTOM_REWARD_UPDATE = "channel.channel_points_custom_reward.update"
    CHANNEL_CHANNEL_POINTS_CUSTOM_REWARD_REMOVE = "channel.channel_points_custom_reward.remove"
    CHANNEL_CHANNEL_POINTS_CUSTOM_REWARD_REDEMPTION_ADD = "channel.channel_points_custom_reward_redemption.add"
    CHANNEL_CHANNEL_POINTS_CUSTOM_REWARD_REDEMPTION_UPDATE = "channel.channel_points_custom_reward_redemption.update"
    CHANNEL_POLL_BEGIN = "channel.poll.begin"
    CHANNEL_POLL_PROGRESS = "channel.poll.progress"
    CHANNEL_POLL_END = "channel.poll.end"
    CHANNEL_PREDICTION_BEGIN = "channel.prediction.begin"
    CHANNEL_PREDICTION_PROGRESS = "channel.prediction.progress"
    CHANNEL_PREDICTION_LOCK = "channel.prediction.lock"
    CHANNEL_PREDICTION_END = "channel.prediction.end"
    CHANNEL_SUSPICIOUS_USER_MESSAGE = "channel.suspicious_user.message"
    CHANNEL_SUSPICIOUS_USER_UPDATE = "channel.suspicious_user.update"
    CHANNEL_VIP_ADD = "channel.vip.add"
    CHANNEL_VIP_REMOVE = "channel.vip.remove"
    CHANNEL_WARNING_ACKNOWLEDGE = "channel.warning.acknowledge"
    CHANNEL_WARNING_SEND = "channel.warning.send"
    CHANNEL_CHARITY_CAMPAIGN_DONATE = "channel.charity_campaign.donate"
    CHANNEL_CHARITY_CAMPAIGN_START = "channel.charity_campaign.start"
    CHANNEL_CHARITY_CAMPAIGN_PROGRESS = "channel.charity_campaign.progress"
    CHANNEL_CHARITY_CAMPAIGN_STOP = "channel.charity_campaign.stop"
    CONDUIT_SHARD_DISABLED = "conduit.shard.disabled"
    DROP_ENTITLEMENT_GRANT = "drop.entitlement.grant"
    EXTENSION_BITS_TRANSACTION_CREATE = "extension.bits_transaction.create"
    CHANNEL_GOAL_BEGIN = "channel.goal.begin"
    CHANNEL_GOAL_PROGRESS = "channel.goal.progress"
    CHANNEL_GOAL_END = "channel.goal.end"
    CHANNEL_HYPE_TRAIN_BEGIN = "channel.hype_train.begin"
    CHANNEL_HYPE_TRAIN_PROGRESS = "channel.hype_train.progress"
    CHANNEL_HYPE_TRAIN_END = "channel.hype_train.end"
    CHANNEL_SHIELD_MODE_BEGIN = "channel.shield_mode.begin"
    CHANNEL_SHIELD_MODE_END = "channel.shield_mode.end"
    CHANNEL_SHOUTOUT_CREATE = "channel.shoutout.create"
    CHANNEL_SHOUTOUT_RECEIVE = "channel.shoutout.receive"
    STREAM_ONLINE = "stream.online"
    STREAM_OFFLINE = "stream.offline"
    USER_AUTHORIZATION_GRANT = "user.authorization.grant"
    USER_AUTHORIZATION_REVOKE = "user.authorization.revoke"
    USER_UPDATE = "user.update"
    USER_WHISPER_MESSAGE = "user.whisper.message"

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"

class UserType(str, Enum):
    ADMIN = "admin"
    GLOBAL_MOD = "global_mod"
    STAFF = "staff"
    NORMAL = ""

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"


class BroadcasterType(str, Enum):
    AFFILIATE = "affiliate"
    PARTNER = "partner"
    NORMAL = ""

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"
