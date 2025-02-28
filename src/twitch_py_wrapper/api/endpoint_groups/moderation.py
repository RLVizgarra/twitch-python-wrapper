from twitch_py_wrapper.api.client import APIClient


class Moderation:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#check-automod-status
    def check_automod_status(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#manage-held-automod-messages
    def manage_held_automod_messages(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-automod-settings
    def get_automod_settings(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-automod-settings
    def update_automod_settings(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-banned-users
    def get_banned_users(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#ban-user
    def ban_user(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#unban-user
    def unban_user(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-unban-requests
    def get_unban_requests(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#resolve-unban-requests
    def resolve_unban_requests(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-blocked-terms
    def get_blocked_terms(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#add-blocked-term
    def add_blocked_terms(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#remove-blocked-term
    def remove_blocked_term(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#delete-chat-messages
    def delete_chat_messages(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-moderated-channels
    def get_moderated_channels(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-moderators
    def get_moderators(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#add-channel-moderator
    def add_channel_moderator(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#remove-channel-moderator
    def remove_channel_moderator(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-vips
    def get_vips(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#add-channel-vip
    def add_channel_vip(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#remove-channel-vip
    def remove_channel_vip(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-shield-mode-status
    def update_shield_mode_status(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-shield-mode-status
    def get_shield_mode_status(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#warn-chat-user
    def warn_chat_user(self):
        pass
