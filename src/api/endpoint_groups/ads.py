from api.client import APIClient


class Ads:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#start-commercial
    def start_commercial(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-ad-schedule
    def get_ad_schedule(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#snooze-next-ad
    def snooze_next_ad(self):
        pass
