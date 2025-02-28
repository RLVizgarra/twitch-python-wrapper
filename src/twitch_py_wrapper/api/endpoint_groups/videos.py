from typing import Literal

import httpx
from dateutil.parser import isoparse

from twitch_py_wrapper.api.client import APIClient
from twitch_py_wrapper.api.enums import VideoType
from twitch_py_wrapper.api.objects import Pagination, Video, MutedSegment


class Videos:
    def __init__(self, client: APIClient):
        self.client = client

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
        url = self.client._url + "videos"

        validation = {
            (video_id is None and user_id is None and game_id is None): "Parameters video_id, user_id and game_id are mutually exclusive",
            (isinstance(video_id, list) and (len(video_id) < 1 or len(video_id) > 100)): "Cannot look up for 100+ video IDs",
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

        req = httpx.get(url,
                        params=parameters,
                        headers=self.client._headers,
                        timeout=self.client._timeout)

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
                                created_at=int(isoparse(video["created_at"]).timestamp()),
                                published_at=int(isoparse(video["published_at"]).timestamp()),
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

    # https://dev.twitch.tv/docs/api/reference/#delete-videos
    def delete_videos(self):
        pass
