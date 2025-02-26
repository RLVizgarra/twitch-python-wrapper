from api.client import APIClient


class Whispers:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#send-whisper
    def send_whisper(self):
        pass
