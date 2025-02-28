from twitch_py_wrapper.api.client import APIClient


class CCLs:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-content-classification-labels
    def get_content_classification_labels(self):
        pass
