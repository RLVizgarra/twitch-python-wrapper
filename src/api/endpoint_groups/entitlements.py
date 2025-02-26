from api.client import APIClient


class Entitlements:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-drops-entitlements
    def get_drops_entitlements(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-drops-entitlements
    def update_drops_entitlements(self):
        pass
