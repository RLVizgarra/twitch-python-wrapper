import httpx

from api.client import APIClient
from api.enums import ContentClassificationLabel
from api.objects import Channel


class Channels:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-channel-information
    def get_channel_information(self,
                                broadcaster_id: str | list[str]) -> Channel | tuple[Channel, ...] | None:
        url = self.client._url + "channels"

        if isinstance(broadcaster_id, list) and (len(broadcaster_id) < 1 or len(broadcaster_id) > 100):
            raise ValueError("Cannot look up for 100+ IDs and/or logins")

        req = httpx.get(url, params={"broadcaster_id": broadcaster_id}, headers=self.client._headers, timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()

        if len(res["data"]) < 1: return None

        channels = list()
        for channel in res["data"]:
            content_classification_labels = list()
            for label in channel["content_classification_labels"]:
                content_classification_labels.append(ContentClassificationLabel(label))
            channels.append(Channel(broadcaster_id=channel["broadcaster_id"],
                                    broadcaster_login=channel["broadcaster_login"],
                                    broadcaster_name=channel["broadcaster_name"],
                                    broadcaster_language=channel["broadcaster_language"],
                                    game_name=channel["game_name"],
                                    game_id=channel["game_id"],
                                    title=channel["title"],
                                    delay=channel["delay"],
                                    tags=tuple(channel["tags"]),
                                    content_classification_labels=tuple(content_classification_labels),
                                    is_branded_content=channel["is_branded_content"]))

        if len(channels) < 2: return channels[0]

        return tuple(channels)

    # https://dev.twitch.tv/docs/api/reference/#modify-channel-information
    def modify_channel_information(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-channel-editors
    def get_channel_editors(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-followed-channels
    def get_followed_channels(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-channel-followers
    def get_channel_followers(self):
        pass
