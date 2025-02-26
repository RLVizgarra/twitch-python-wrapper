from api.client import APIClient


class Charity:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-charity-campaign
    def get_charity_campaign(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-charity-campaign-donations
    def get_charity_campaign_donations(self):
        pass
