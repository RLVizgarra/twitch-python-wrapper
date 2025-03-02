from datetime import datetime

import httpx
import pytz
from dateutil.parser import isoparse

from twitch_py_wrapper.api.client import APIClient
from twitch_py_wrapper.api.objects import Pagination, Clip


class Clips:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#create-clip
    def create_clip(self):
        pass

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
        url = self.client._url + "clips"

        validation = {
            (broadcaster_id is None and game_id is None and clip_id is None): "Parameters broadcaster_id, game_id and clip_id are mutually exclusive",
            (isinstance(clip_id, list) and (len(clip_id) < 1 or len(clip_id) > 100)): "Cannot look up for clip 100+ IDs",
            (first and (first < 1 or first > 100)): "Parameter first must be between 1 and 100"
        }

        for condition, error in validation.items():
            if condition: raise ValueError(error)

        parameters = {}

        optional_params = {
            "broadcaster_id": broadcaster_id,
            "game_id": game_id,
            "id": clip_id,
            "started_at": datetime.fromtimestamp(started_at, tz=pytz.utc).isoformat("T")[:-6] + "Z" if started_at else None,
            "ended_at": datetime.fromtimestamp(ended_at, tz=pytz.utc).isoformat("T")[:-6] + "Z" if ended_at else None,
            "first": first,
            "before": before.cursor if before else None,
            "after": after.cursor if after else None,
            "is_featured": is_featured
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
                              created_at=int(isoparse(clip["created_at"]).timestamp()),
                              thumbnail_url=clip["thumbnail_url"],
                              duration=clip["duration"],
                              vod_offset=clip["vod_offset"],
                              is_featured=clip["is_featured"]))

        if len(clips) < 2: return clips[0]

        if len(res["pagination"]) > 0: return tuple(clips), Pagination(res["pagination"]["cursor"])

        return tuple(clips)
