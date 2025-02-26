from api.client import APIClient


class Games:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-top-games
    def get_top_games(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-games
    def get_games(self):
        pass
