from typing import Literal

import httpx
from dateutil.parser import isoparse

from twitch_py_wrapper.api.client import APIClient
from twitch_py_wrapper.api.objects import Pagination, Stream


class Streams:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-stream-key
    def get_stream_key(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-streams
    def get_streams(self,
                    user_id: str | list[str] | None,
                    user_login: str | list[str] | None,
                    game_id: str | list[str] | None,
                    stream_type: Literal["all", "live"] | None,
                    language: str | None,
                    first: int | None,
                    before: Pagination | None,
                    after: Pagination | None) -> Stream | tuple[Stream, ...] | tuple[tuple[Stream, ...], Pagination] | None:
        url = self.client._url + "streams"

        validation = {
            (isinstance(user_id, list) and (len(user_id) < 1 or len(user_id) > 100)): "Cannot look up for 100+ user IDs",
            (isinstance(user_login, list) and (len(user_login) < 1 or len(user_login) > 100)): "Cannot look up for 100+ user logins",
            (isinstance(game_id, list) and (len(game_id) < 1 or len(game_id) > 100)): "Cannot look up for 100+ game IDs",
            (language and language != "other" and len(language) != 2): "Parameter language must be a two-letter language code or 'other'",
            (first and (first < 1 or first > 100)): "Parameter first must be between 1 and 100"
        }

        for condition, error in validation.items():
            if condition: raise ValueError(error)

        parameters = {}

        optional_params = {
            "user_id": user_id,
            "user_login": user_login,
            "game_id": game_id,
            "type": stream_type,
            "language": language,
            "first": first,
            "before": before.cursor if before else None,
            "after": after.cursor if after else None
        }

        for key, value in optional_params.items():
            if value: parameters[key] = value

        req = httpx.get(url,
                        params=parameters,
                        headers=self.client._headers,
                        timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()

        streams = list()
        for stream in res["data"]:
            streams.append(Stream(id=stream["id"],
                                  user_id=stream["user_id"],
                                  user_login=stream["user_login"],
                                  user_name=stream["user_name"],
                                  game_id=stream["game_id"],
                                  game_name=stream["game_name"],
                                  type=stream["type"] if stream["type"] != "" else None,
                                  title=stream["title"],
                                  tags=tuple(stream["tags"]),
                                  viewer_count=stream["viewer_count"],
                                  started_at=int(isoparse(stream["started_at"]).timestamp()),
                                  language=stream["language"],
                                  thumbnail_url=stream["thumbnail_url"],
                                  is_mature=stream["is_mature"]))

        if len(streams) < 2: return streams[0]

        if len(res["pagination"]) > 0: return tuple(streams), Pagination(res["pagination"]["cursor"])

        return tuple(streams)

    # https://dev.twitch.tv/docs/api/reference/#get-followed-streams
    def get_followed_streams(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#create-stream-marker
    def create_stream_marker(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-stream-markers
    def get_stream_markers(self):
        pass
