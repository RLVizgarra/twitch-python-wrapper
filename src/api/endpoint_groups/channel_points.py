from api.client import APIClient


class ChannelPoints:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#create-custom-rewards
    def create_custom_rewards(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#delete-custom-reward
    def delete_custom_reward(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-custom-reward
    def get_custom_reward(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-custom-reward-redemption
    def get_custom_reward_redemption(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-custom-reward
    def update_custom_reward(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-redemption-status
    def update_redemption_status(self):
        pass
