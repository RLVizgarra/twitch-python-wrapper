from api.client import APIClient


class Goals:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-creator-goals
    def get_creator_goals(self):
        pass
