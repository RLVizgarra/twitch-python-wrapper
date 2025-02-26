from api.client import APIClient


class Predictions:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-predictions
    def get_predictions(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#create-prediction
    def create_prediction(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#end-prediction
    def end_prediction(self):
        pass
