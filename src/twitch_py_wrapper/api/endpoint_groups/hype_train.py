from twitch_py_wrapper.api.client import APIClient


class HypeTrain:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-hype-train-events
    def get_hype_train_events(self):
        pass
