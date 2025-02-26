from api.client import APIClient


class Chat:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-chatters
    def get_chatters(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-channel-emotes
    def get_channel_emotes(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-global-emotes
    def get_global_emotes(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-emote-sets
    def get_emote_sets(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-channel-chat-badges
    def get_channel_chat_badges(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-global-chat-badges
    def get_global_chat_badges(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-chat-settings
    def get_chat_settings(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-shared-chat-session
    def get_shared_chat_session(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-user-emotes
    def get_user_emotes(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-chat-settings
    def update_chat_settings(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#send-chat-announcement
    def send_chat_announcement(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#send-a-shoutout
    def send_a_shoutout(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#send-chat-message
    def send_chat_message(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-user-chat-color
    def get_user_chat_color(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-user-chat-color
    def update_user_chat_color(self):
        pass
