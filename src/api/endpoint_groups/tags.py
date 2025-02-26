from api.client import APIClient


class Tags:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-all-stream-tags
    def get_all_stream_tags(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-stream-tags
    def get_stream_tags(self):
        pass
