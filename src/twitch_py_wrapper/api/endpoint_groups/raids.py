from twitch_py_wrapper.api.client import APIClient


class Raids:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#start-a-raid
    def start_a_raid(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#cancel-a-raid
    def cancel_a_raid(self):
        pass
