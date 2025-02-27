from shared_enums import Enums


class CheermoteType(Enums):
    GLOBAL_FIRST_PARTY = "global_first_party"
    GLOBAL_THIRD_PARTY = "global_third_party"
    CHANNEL_CUSTOM = "channel_custom"
    DISPLAY_ONLY = "display_only"
    SPONSORED = "sponsored"

class ContentClassificationLabel(Enums):
    DEBATED_SOCIAL_ISSUES_AND_POLITICS = "DebatedSocialIssuesAndPolitics"
    DRUGS_INTOXICATION = "DrugsIntoxication"
    GAMBLING = "Gambling"
    MATURE_GAME = "MatureGame"
    PROFANITY_VULGARITY = "ProfanityVulgarity"
    SEXUAL_THEMES = "SexualThemes"
    VIOLENT_GRAPHIC = "ViolentGraphic"

class EmoteType(Enums):
    BITSTIER = "bitstier"
    FOLLOWER = "follower"
    SUBSCRIPTIONS = "subscriptions"

class EmoteFormat(Enums):
    ANIMATED = "animated"
    STATIC = "static"

class EmoteThemeMode(Enums):
    DARK = "dark"
    LIGHT = "light"

class VideoType(Enums):
    ARCHIVE = "archive"
    HIGHLIGHT = "highlight"
    UPLOAD = "upload"

class UserType(Enums):
    ADMIN = "admin"
    GLOBAL_MOD = "global_mod"
    STAFF = "staff"
    NORMAL = ""

class BroadcasterType(Enums):
    AFFILIATE = "affiliate"
    PARTNER = "partner"
    NORMAL = ""

class VideoType(Enums):
    ARCHIVE = "archive"
    HIGHLIGHT = "highlight"
    UPLOAD = "upload"
