from typing import Literal

import httpx
from dateutil import parser

from api.enums import UserType, BroadcasterType, VideoType
from api.objects import User, Video, Pagination, MutedSegment


class APIClient:
    def __init__(self,
                 client_id: str,
                 access_token: str,
                 timeout: float = httpx._config.DEFAULT_TIMEOUT_CONFIG):
        self._url = "https://api.twitch.tv/helix/"
        self.__headers = {
            "Authorization": "Bearer " + access_token,
            "Client-Id": client_id
        }
        self._timeout = timeout

    def get_users(self,
                  user_id: str | list[str] = None,
                  login: str | list[str] = None) -> User | list[User] | None:
        url = self._url + "users"

        if user_id is None and login is None:
            raise ValueError("Parameters user_id and login are mutually exclusive")

        sum_of_lookups = 0

        if type(user_id) is list:
            sum_of_lookups += len(user_id)
        elif user_id:
            sum_of_lookups += 1

        if type(login) is list:
            sum_of_lookups += len(login)
        elif login:
            sum_of_lookups += 1

        if sum_of_lookups > 100:
            raise ValueError("Cannot look up for 100+ IDs and/or logins")

        parameters: dict
        if user_id and login:
            parameters = {"id": user_id, "login": login}
        elif user_id:
            parameters = {"id": user_id}
        else:
            parameters = {"login": login}

        req = httpx.get(url, params=parameters, headers=self.__headers, timeout=self._timeout)
        req.raise_for_status()
        res = req.json()["data"]

        if len(res) < 1:
            return None

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
                              created_at=int(parser.isoparse(user["created_at"]).timestamp())))

        if len(users) < 2:
            return users[0]
        return users

    def get_videos(self,
                   video_id: str | list[str] = None,
                   user_id: str = None,
                   game_id: str = None,
                   language: str = None,
                   period: Literal["all", "day", "month", "week"] = None,
                   sort: Literal["time", "trending", "views"] = None,
                   video_type: Literal["all", "archive", "highlight", "upload"] = None,
                   first: int = None,
                   after: Pagination = None,
                   before: Pagination = None) -> Video | list[Video] | tuple[list[Video], Pagination] | None:
        url = self._url + "videos"

        validation = {
            (
                        video_id is None and user_id is None and game_id is None): "Parameters video_id, user_id and game_id are mutually exclusive",
            (type(video_id) is list and len(video_id) > 100): "Cannot look up for 100+ IDs",
            (language and game_id is None): "If you supply a language then you must also supply a game_id",
            (period and (
                        game_id is None or user_id is None)): "If you supply a period then you must also supply a game_id or a user_id",
            (sort and (
                        game_id is None or user_id is None)): "If you supply a sort then you must also supply a game_id or a user_id",
            (video_type and (
                        game_id is None or user_id is None)): "If you supply a video_type then you must also supply a game_id or a user_id",
            (first and (
                        game_id is None or user_id is None)): "If you supply a first then you must also supply a game_id or a user_id",
            (after and user_id is None): "If you supply a after then you must also supply a user_id",
            (before and user_id is None): "If you supply a before then you must also supply a user_id"
        }

        for condition, error in validation.items():
            if condition:
                raise ValueError(error)

        parameters: dict
        if video_id:
            parameters = {"id": video_id}
        elif user_id and game_id:
            parameters = {"user_id": user_id, "game_id": game_id}
        elif user_id:
            parameters = {"user_id": user_id}
        else:
            parameters = {"game_id": game_id}

        optional_params = {
            "language": language,
            "period": period,
            "sort": sort,
            "video_type": video_type,
            "first": first,
            "after": after.cursor if after else None,
            "before": before.cursor if before else None
        }

        for key, value in optional_params.items():
            if value is not None:
                parameters[key] = value

        req = httpx.get(url, params=parameters, headers=self.__headers, timeout=self._timeout)

        if req.status_code == 404:
            return None

        req.raise_for_status()
        res = req.json()

        if len(res["data"]) < 1:
            return None

        videos = list()
        for video in res["data"]:
            muted_segments = list()
            if video["muted_segments"]:
                for segment in video["muted_segments"]:
                    muted_segments.append(MutedSegment(segment["duration"], segment["offset"]))
            videos.append(Video(id=video["id"],
                                stream_id=video["stream_id"],
                                user_id=video["user_id"],
                                user_login=video["user_login"],
                                user_name=video["user_name"],
                                title=video["title"],
                                description=video["description"],
                                created_at=int(parser.isoparse(video["created_at"]).timestamp()),
                                published_at=int(parser.isoparse(video["published_at"]).timestamp()),
                                url=video["url"],
                                thumbnail_url=video["thumbnail_url"],
                                viewable=video["viewable"],
                                view_count=video["view_count"],
                                language=video["language"],
                                type=VideoType(video["type"]),
                                duration=video["duration"],
                                muted_segments=muted_segments))

        if len(videos) < 2:
            return videos[0]

        if len(res["pagination"]) > 0:
            return videos, Pagination(res["pagination"]["cursor"])

        return videos
