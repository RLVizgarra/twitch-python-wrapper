from twitch_py_wrapper.api.client import APIClient


class Teams:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-channel-teams
    def get_channel_teams(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-teams
    def get_teams(self):
        pass
