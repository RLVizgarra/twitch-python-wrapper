from api.client import APIClient


class Search:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#search-categories
    def search_categories(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#search-channels
    def search_channels(self):
        pass
