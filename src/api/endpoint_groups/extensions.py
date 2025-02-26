from api.client import APIClient


class Extensions:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-extension-configuration-segment
    def get_extension_configuration_segment(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#set-extension-configuration-segment
    def set_extension_configuration_segment(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#set-extension-required-configuration
    def set_extension_required_configuration(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#send-extension-pubsub-message
    def send_extension_pubsub_message(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-extension-live-channels
    def get_extension_live_channels(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-extension-secrets
    def get_extension_secrets(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#create-extension-secret
    def create_extension_secret(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#send-extension-chat-message
    def send_extension_chat_message(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-extensions
    def get_extensions(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-released-extensions
    def get_released_extensions(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-extension-bits-products
    def get_extension_bits_products(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-extension-bits-product
    def update_extension_bits_product(self):
        pass
