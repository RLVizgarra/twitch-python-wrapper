from api.client import APIClient


class Analytics:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-extension-analytics
    def get_extension_analytics(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-game-analytics
    def get_game_analytics(self):
        pass
