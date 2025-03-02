import httpx
from dateutil.parser import isoparse

from twitch_py_wrapper.api.client import APIClient
from twitch_py_wrapper.api.enums import UserType, BroadcasterType
from twitch_py_wrapper.api.objects import User


class Users:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-users
    def get_users(self,
                  user_id: str | list[str] = None,
                  login: str | list[str] = None) -> User | tuple[User, ...] | None:
        url = self.client._url + "users"

        sum_of_lookups = 0

        if isinstance(user_id, list): sum_of_lookups += len(user_id)
        elif user_id: sum_of_lookups += 1

        if isinstance(login, list): sum_of_lookups += len(login)
        elif login: sum_of_lookups += 1

        # TODO: Remove check for user_id and login being mutually exclusive only if token is user access token
        if sum_of_lookups > 100:
            raise ValueError("Cannot look up for 100+ user IDs and/or logins")

        parameters = {}

        optional_params = {
            "id": user_id,
            "login": login
        }

        for key, value in optional_params.items():
            if value: parameters[key] = value

        req = httpx.get(url,
                        params=parameters,
                        headers=self.client._headers,
                        timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()["data"]

        if len(res) < 1: return None

        users = list()
        for user in res:
            users.append(User(id=user["id"],
                              login=user["login"],
                              display_name=user["display_name"],
                              type=UserType(user["type"]),
                              broadcaster_type=BroadcasterType(user["broadcaster_type"]),
                              description=user["description"],
                              profile_image_url=user["profile_image_url"],
                              offline_image_url=user["offline_image_url"],
                              email=user["email"] if "email" in user else None,
                              created_at=int(isoparse(user["created_at"]).timestamp())))

        if len(users) < 2: return users[0]

        return tuple(users)

    # https://dev.twitch.tv/docs/api/reference/#update-user
    def update_user(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-user-block-list
    def get_user_block_list(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#block-user
    def block_user(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#unblock-user
    def unblock_user(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-user-extensions
    def get_user_extensions(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-user-active-extensions
    def get_user_active_extensions(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-user-extensions
    def update_user_extensions(self):
        pass
