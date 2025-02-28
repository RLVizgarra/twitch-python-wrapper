from twitch_py_wrapper.api.client import APIClient


class Streams:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-stream-key
    def get_stream_key(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-streams
    def get_streams(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-followed-streams
    def get_followed_streams(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#create-stream-marker
    def create_stream_marker(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-stream-markers
    def get_stream_markers(self):
        pass
