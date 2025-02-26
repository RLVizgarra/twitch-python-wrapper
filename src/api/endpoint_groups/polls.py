from api.client import APIClient


class Polls:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-polls
    def get_polls(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#create-poll
    def create_poll(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#end-poll
    def end_poll(self):
        pass
