from datetime import datetime
from typing import Literal

import httpx
import pytz
from dateutil import parser

from api.enums import UserType, BroadcasterType, VideoType, CheermoteType
from api.objects import User, Video, Pagination, MutedSegment, Clip, Cheermote, CheerTier


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

    # https://dev.twitch.tv/docs/api/reference/#get-cheermotes
    def get_cheermotes(self,
                       broadcaster_id: str = None) -> tuple[Cheermote, ...]:
        url = self._url + "bits/cheermotes"

        if broadcaster_id: parameters = {"broadcaster_id": broadcaster_id}
        else: parameters = {}

        req = httpx.get(url, params=parameters, headers=self.__headers, timeout=self._timeout)
        req.raise_for_status()
        res = req.json()["data"]

        cheermotes = list()
        for cheermote in res:
            cheer_tiers = list()
            for tier in cheermote["tiers"]:
                cheer_tiers.append(CheerTier(min_bits=tier["min_bits"],
                                       id=tier["id"],
                                       color=tier["color"],
                                       images=tuple(sorted((str(k), str(v)) for k, v in tier["images"].items())),
                                       can_cheer=tier["can_cheer"],
                                       show_in_bits_card=tier["show_in_bits_card"]))

            cheermotes.append(Cheermote(prefix=cheermote["prefix"],
                                        tiers=tuple(cheer_tiers),
                                        type=CheermoteType(cheermote["type"]),
                                        order=cheermote["order"],
                                        last_update=int(parser.isoparse(cheermote["last_updated"]).timestamp()),
                                        is_charitable=cheermote["is_charitable"]))

        return tuple(cheermotes)

    # https://dev.twitch.tv/docs/api/reference/#get-clips
    def get_clips(self,
                  broadcaster_id: str = None,
                  game_id: str = None,
                  clip_id: str | list[str] = None,
                  started_at: int = None,
                  ended_at: int = None,
                  first: int = None,
                  before: Pagination = None,
                  after: Pagination = None,
                  is_featured: bool = None) -> Clip | tuple[Clip, ...] | tuple[tuple[Clip, ...], Pagination] | None:
        url = self._url + "clips"

        validation = {
            (broadcaster_id is None and game_id is None and clip_id is None): "Parameters broadcaster_id, game_id and clip_id are mutually exclusive",
            (type(clip_id) is list and len(clip_id) > 100): "Cannot look up for 100+ IDs",
            (first and (first < 1 or first > 100)): "Parameter first must be between 1 and 100"
        }

        for condition, error in validation.items():
            if condition: raise ValueError(error)

        if clip_id: parameters = {"id": clip_id}
        elif broadcaster_id and game_id: parameters = {"broadcaster_id": broadcaster_id, "game_id": game_id}
        elif broadcaster_id: parameters = {"broadcaster_id": broadcaster_id}
        else: parameters = {"game_id": game_id}

        optional_params = {
            "started_at": datetime.fromtimestamp(started_at, tz=pytz.utc).isoformat("T")[:-6] + "Z" if started_at else None,
            "ended_at": datetime.fromtimestamp(ended_at, tz=pytz.utc).isoformat("T")[:-6] + "Z" if ended_at else None,
            "first": first,
            "before": before.cursor if before else None,
            "after": after.cursor if after else None,
            "is_featured": is_featured
        }

        for key, value in optional_params.items():
            if value: parameters[key] = value

        req = httpx.get(url, params=parameters, headers=self.__headers, timeout=self._timeout)

        if req.status_code == 404:
            return None

        req.raise_for_status()
        res = req.json()

        if len(res["data"]) < 1: return None

        clips = list()
        for clip in res["data"]:
            clips.append(Clip(id=clip["id"],
                              url=clip["url"],
                              embed_url=clip["embed_url"],
                              broadcaster_id=clip["broadcaster_id"],
                              broadcaster_name=clip["broadcaster_name"],
                              creator_id=clip["creator_id"],
                              creator_name=clip["creator_name"],
                              video_id=clip["video_id"] if clip["video_id"] != "" else None,
                              game_id=clip["game_id"],
                              language=clip["language"],
                              title=clip["title"],
                              view_count=clip["view_count"],
                              created_at=int(parser.isoparse(clip["created_at"]).timestamp()),
                              thumbnail_url=clip["thumbnail_url"],
                              duration=clip["duration"],
                              vod_offset=clip["vod_offset"],
                              is_featured=clip["is_featured"]))

        if len(clips) < 2: return clips[0]

        if len(res["pagination"]) > 0: return tuple(clips), Pagination(res["pagination"]["cursor"])

        return tuple(clips)

    # https://dev.twitch.tv/docs/api/reference/#get-users
    def get_users(self,
                  user_id: str | list[str] = None,
                  login: str | list[str] = None) -> User | tuple[User, ...] | None:
        url = self._url + "users"

        sum_of_lookups = 0

        if type(user_id) is list: sum_of_lookups += len(user_id)
        elif user_id: sum_of_lookups += 1

        if type(login) is list: sum_of_lookups += len(login)
        elif login: sum_of_lookups += 1

        # TODO: Remove check for user_id and login being mutually exclusive if token is user access token
        validation = {
            (sum_of_lookups > 100): "Cannot look up for 100+ IDs and/or logins"
        }

        for condition, error in validation.items():
            if condition: raise ValueError(error)

        if user_id and login: parameters = {"id": user_id, "login": login}
        elif user_id: parameters = {"id": user_id}
        elif login: parameters = {"login": login}
        else: parameters = {}

        req = httpx.get(url, params=parameters, headers=self.__headers, timeout=self._timeout)
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
                              created_at=int(parser.isoparse(user["created_at"]).timestamp())))

        if len(users) < 2: return users[0]

        return tuple(users)

    # https://dev.twitch.tv/docs/api/reference/#get-videos
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
                   before: Pagination = None) -> Video | tuple[Video, ...] | tuple[tuple[Video, ...], Pagination] | None:
        url = self._url + "videos"

        validation = {
            (video_id is None and user_id is None and game_id is None): "Parameters video_id, user_id and game_id are mutually exclusive",
            (type(video_id) is list and len(video_id) > 100): "Cannot look up for 100+ IDs",
            (language and game_id is None): "If you supply language then you must also supply game_id",
            (period and (game_id is None and user_id is None)): "If you supply period then you must also supply game_id or user_id",
            (sort and (game_id is None and user_id is None)): "If you supply sort then you must also supply game_id or user_id",
            (video_type and (game_id is None and user_id is None)): "If you supply video_type then you must also supply game_id or user_id",
            (first and (game_id is None and user_id is None)): "If you supply first then you must also supply game_id or user_id",
            (after and user_id is None): "If you supply after then you must also supply a user_id",
            (before and user_id is None): "If you supply before then you must also supply user_id",
            (first and (first < 1 or first > 100)): "Parameter first must be between 1 and 100"
        }

        for condition, error in validation.items():
            if condition: raise ValueError(error)

        if video_id: parameters = {"id": video_id}
        elif user_id and game_id: parameters = {"user_id": user_id, "game_id": game_id}
        elif user_id: parameters = {"user_id": user_id}
        else: parameters = {"game_id": game_id}

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
            if value: parameters[key] = value

        req = httpx.get(url, params=parameters, headers=self.__headers, timeout=self._timeout)

        if req.status_code == 404: return None

        req.raise_for_status()
        res = req.json()

        if len(res["data"]) < 1: return None

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
                                muted_segments=tuple(muted_segments)))

        if len(videos) < 2: return videos[0]

        if len(res["pagination"]) > 0: return tuple(videos), Pagination(res["pagination"]["cursor"])

        return tuple(videos)
