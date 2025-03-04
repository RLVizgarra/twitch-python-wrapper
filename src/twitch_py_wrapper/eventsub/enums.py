from twitch_py_wrapper.shared_enums import Enums


class MessageType(Enums):
    SESSION_WELCOME = "session_welcome"
    SESSION_KEEPALIVE = "session_keepalive"
    NOTIFICATION = "notification"
    SESSION_RECONNECT = "session_reconnect"
    REVOCATION = "revocation"
