from api.client import APIClient


class Subscriptions:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-broadcaster-subscriptions
    def get_broadcaster_subscriptions(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#check-user-subscription
    def check_user_subscription(self):
        pass
