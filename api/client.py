import httpx
from dateutil import parser

from api.enums import UserType, BroadcasterType
from api.objects import User


class APIClient:
    def __init__(self, client_id: str, access_token: str, timeout: float = httpx._config.DEFAULT_TIMEOUT_CONFIG):
        self._url = "https://api.twitch.tv/helix/"
        self.__headers = {
            "Authorization": "Bearer " + access_token,
            "Client-Id": client_id
        }
        self._timeout = timeout

    def get_user(self, user_id: str = None, login: str = None) -> User:
        if user_id is None and login is None:
            raise ValueError("Parameters user_id and login are mutually exclusive")

        if login is None:
            res = httpx.get(self._url + "users", params={"id": user_id}, headers=self.__headers)
        else:
            res = httpx.get(self._url + "users", params={"login": login}, headers=self.__headers)

        user = res.json()["data"][0]
        return User(user["id"],
                    user["login"],
                    user["display_name"],
                    UserType(user["type"]),
                    BroadcasterType(user["broadcaster_type"]),
                    user["description"],
                    user["profile_image_url"],
                    user["offline_image_url"],
                    user["email"] if "email" in user else None,
                    int(parser.isoparse(user["created_at"]).timestamp()))
