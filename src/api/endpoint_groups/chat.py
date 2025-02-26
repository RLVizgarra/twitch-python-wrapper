import httpx

from api.client import APIClient
from api.enums import EmoteType, EmoteFormat, EmoteThemeMode
from api.objects import Emote, ChatBadgeSet, ChatBadge


class Chat:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-chatters
    def get_chatters(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-channel-emotes
    def get_channel_emotes(self,
                           broadcaster_id: str) -> tuple[Emote, str] | tuple[tuple[Emote, ...], str] | None:
        url = self.client._url + "chat/emotes"

        req = httpx.get(url,
                        params={"broadcaster_id": broadcaster_id},
                        headers=self.client._headers,
                        timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()

        if len(res["data"]) < 1: return None

        emotes = list()
        for emote in res["data"]:
            formats = list()
            for emote_format in emote["format"]: formats.append(EmoteFormat(emote_format))
            scales = list()
            for scale in emote["scale"]: formats.append(scale)
            themes_modes = list()
            for theme_mode in emote["theme_mode"]: themes_modes.append(EmoteThemeMode(theme_mode))
            emotes.append(Emote(id=emote["id"],
                                name=emote["name"],
                                images=tuple(sorted((str(k), str(v)) for k, v in emote["images"].items())),
                                tier=emote["tier"] if emote["tier"] != "" else None,
                                emote_type=EmoteType(emote["emote_type"]),
                                emote_set_id=emote["emote_set_id"],
                                owner_id=None,
                                format=tuple(formats),
                                scale=tuple(scales),
                                theme_mode=tuple(themes_modes)))

        if len(emotes) < 2: return emotes[0], res["template"]

        return tuple(emotes), res["template"]

    # https://dev.twitch.tv/docs/api/reference/#get-global-emotes
    def get_global_emotes(self) -> tuple[tuple[Emote, ...], str] | None:
        url = self.client._url + "chat/emotes/global"

        req = httpx.get(url,
                        headers=self.client._headers,
                        timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()

        emotes = list()
        for emote in res["data"]:
            formats = list()
            for emote_format in emote["format"]: formats.append(EmoteFormat(emote_format))
            scales = list()
            for scale in emote["scale"]: formats.append(scale)
            themes_modes = list()
            for theme_mode in emote["theme_mode"]: themes_modes.append(EmoteThemeMode(theme_mode))
            emotes.append(Emote(id=emote["id"],
                                name=emote["name"],
                                images=tuple(sorted((str(k), str(v)) for k, v in emote["images"].items())),
                                tier=None,
                                emote_type=None,
                                emote_set_id=None,
                                owner_id=None,
                                format=tuple(formats),
                                scale=tuple(scales),
                                theme_mode=tuple(themes_modes)))

        return tuple(emotes), res["template"]

    # https://dev.twitch.tv/docs/api/reference/#get-emote-sets
    def get_emote_sets(self,
                       emote_set_id: str | list[str]) -> tuple[Emote, str] | tuple[tuple[Emote, ...], str] | None:
        url = self.client._url + "chat/emotes/set"

        if isinstance(emote_set_id, list) and (len(emote_set_id) < 1 or len(emote_set_id) > 25):
            raise ValueError("Cannot look up for 25+ emote set IDs")

        req = httpx.get(url,
                        params={"emote_set_id": emote_set_id},
                        headers=self.client._headers,
                        timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()

        if len(res["data"]) < 1: return None

        emotes = list()
        for emote in res["data"]:
            formats = list()
            for emote_format in emote["format"]: formats.append(EmoteFormat(emote_format))
            scales = list()
            for scale in emote["scale"]: formats.append(scale)
            themes_modes = list()
            for theme_mode in emote["theme_mode"]: themes_modes.append(EmoteThemeMode(theme_mode))
            emotes.append(Emote(id=emote["id"],
                                name=emote["name"],
                                images=tuple(sorted((str(k), str(v)) for k, v in emote["images"].items())),
                                tier=None,
                                emote_type=EmoteType(emote["emote_type"]),
                                emote_set_id=emote["emote_set_id"],
                                owner_id=emote["owner_id"],
                                format=tuple(formats),
                                scale=tuple(scales),
                                theme_mode=tuple(themes_modes)))

        if len(emotes) < 2: return emotes[0], res["template"]

        return tuple(emotes), res["template"]

    # https://dev.twitch.tv/docs/api/reference/#get-channel-chat-badges
    def get_channel_chat_badges(self,
                                broadcaster_id: str) -> ChatBadgeSet | tuple[ChatBadgeSet, ...] | None:
        url = self.client._url + "chat/badges"

        req = httpx.get(url,
                        params={"broadcaster_id": broadcaster_id},
                        headers=self.client._headers,
                        timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()

        if len(res["data"]) < 1: return None

        badge_sets = list()
        for badges_set in res["data"]:
            badges = list()
            for badge in badges_set["versions"]:
                badges.append(ChatBadge(id=badge["id"],
                                        image_url_1x=badge["image_url_1x"],
                                        image_url_2x=badge["image_url_2x"],
                                        image_url_4x=badge["image_url_4x"],
                                        title=badge["title"],
                                        description=badge["description"],
                                        click_action=badge["click_action"],
                                        click_url=badge["click_url"]))

            badge_sets.append(ChatBadgeSet(set_id=badges_set["set_id"],
                                           versions=tuple(badges)))

        if len(badge_sets) < 2: return badge_sets[0]

        return tuple(badge_sets)

    # https://dev.twitch.tv/docs/api/reference/#get-global-chat-badges
    def get_global_chat_badges(self) -> tuple[ChatBadgeSet, ...]:
        url = self.client._url + "chat/badges/global"

        req = httpx.get(url,
                        headers=self.client._headers,
                        timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()["data"]

        badge_sets = list()
        for badges_set in res:
            badges = list()
            for badge in badges_set["versions"]:
                badges.append(ChatBadge(id=badge["id"],
                                        image_url_1x=badge["image_url_1x"],
                                        image_url_2x=badge["image_url_2x"],
                                        image_url_4x=badge["image_url_4x"],
                                        title=badge["title"],
                                        description=badge["description"],
                                        click_action=badge["click_action"],
                                        click_url=badge["click_url"]))

            badge_sets.append(ChatBadgeSet(set_id=badges_set["set_id"],
                                           versions=tuple(badges)))

        return tuple(badge_sets)

    # https://dev.twitch.tv/docs/api/reference/#get-chat-settings
    def get_chat_settings(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-shared-chat-session
    def get_shared_chat_session(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-user-emotes
    def get_user_emotes(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-chat-settings
    def update_chat_settings(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#send-chat-announcement
    def send_chat_announcement(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#send-a-shoutout
    def send_a_shoutout(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#send-chat-message
    def send_chat_message(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-user-chat-color
    def get_user_chat_color(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-user-chat-color
    def update_user_chat_color(self):
        pass
