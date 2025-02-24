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
