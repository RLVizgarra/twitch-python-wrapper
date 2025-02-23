from enum import Enum

class UserType(Enum):
    ADMIN = "admin"
    GLOBAL_MOD = "global_mod"
    STAFF = "staff"
    NORMAL = ""

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"

class BroadcasterType(Enum):
    AFFILIATE = "affiliate"
    PARTNER = "partner"
    NORMAL = ""

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"
