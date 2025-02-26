from api.client import APIClient


class Channels:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-channel-information
    def get_channel_information(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#modify-channel-information
    def modify_channel_information(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-channel-editors
    def get_channel_editors(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-followed-channels
    def get_followed_channels(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-channel-followers
    def get_channel_followers(self):
        pass
