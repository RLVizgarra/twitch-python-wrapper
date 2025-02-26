from api.client import APIClient


class Conduits:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-conduits
    def get_conduits(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#create-conduits
    def create_conduits(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-conduits
    def update_conduits(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#delete-conduit
    def delete_conduit(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-conduit-shards
    def get_conduit_shards(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-conduit-shards
    def update_conduit_shards(self):
        pass
