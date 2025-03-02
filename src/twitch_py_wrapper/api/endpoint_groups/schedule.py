from datetime import datetime

import httpx
import pytz
from dateutil.parser import isoparse

from twitch_py_wrapper.api.client import APIClient
from twitch_py_wrapper.api.objects import Pagination, ScheduleSegment, Category, BroadcasterSchedule, ScheduleVacation


class Schedule:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-channel-stream-schedule
    def get_channel_stream_schedule(self,
                                    broadcaster_id: str,
                                    segment_id: str | list[str] = None,
                                    start_time: int = None,
                                    first: int = None,
                                    after: Pagination = None) -> BroadcasterSchedule | tuple[BroadcasterSchedule, Pagination] | None:
        url = self.client._url + "schedule"

        sum_of_lookups = 0

        if isinstance(segment_id, list):
            sum_of_lookups += len(segment_id)
        elif segment_id:
            sum_of_lookups += 1

        if sum_of_lookups > 100:
            raise ValueError("Cannot look up for 100+ IDs")

        parameters = {"broadcaster_id": broadcaster_id}

        optional_params = {
            "id": segment_id,
            "start_time": datetime.fromtimestamp(start_time, tz=pytz.utc).isoformat("T")[:-6] + "Z" if start_time else None,
            "first": first,
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

        if len(res["data"]) < 1: return None

        segments = list()
        for segment in res["data"]["segments"]:
            segments.append(ScheduleSegment(id=segment["id"],
                                            start_time=int(isoparse(segment["start_time"]).timestamp()),
                                            end_time=int(isoparse(segment["end_time"]).timestamp()),
                                            title=segment["title"],
                                            canceled_until=int(isoparse(segment["canceled_until"]).timestamp()) if segment["canceled_until"] else None,
                                            category=Category(id=segment["category"]["id"],
                                                              name=segment["category"]["name"],
                                                              box_art_url="https://static-cdn.jtvnw.net/ttv-boxart/" + segment["category"]["id"] + "-{width}x{height}.jpg",
                                                              igdb_id=None) if segment["category"] else None,
                                            is_recurring=segment["is_recurring"]))

        schedule = BroadcasterSchedule(segments=tuple(segments),
                                       broadcaster_id=res["data"]["broadcaster_id"],
                                       broadcaster_name=res["data"]["broadcaster_name"],
                                       broadcaster_login=res["data"]["broadcaster_login"],
                                       vacation=ScheduleVacation(start_time=int(isoparse(res["data"]["vacation"]["start_time"]).timestamp()),
                                                                 end_time=int(isoparse(res["data"]["vacation"]["end_time"]).timestamp())) if res["data"]["vacation"] else None)

        if len(res["pagination"]) > 0: return schedule, Pagination(res["pagination"]["cursor"])

        return schedule

    # https://dev.twitch.tv/docs/api/reference/#get-channel-icalendar
    def get_channel_icalendar(self,
                              broadcaster_id: str) -> str:
        url = self.client._url + "schedule/icalendar"

        req = httpx.get(url,
                        params={"broadcaster_id": broadcaster_id})
        req.raise_for_status()
        return req.text

    # https://dev.twitch.tv/docs/api/reference/#update-channel-stream-schedule
    def update_channel_stream_schedule(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#create-channel-stream-schedule-segment
    def create_channel_stream_schedule_segment(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-channel-stream-schedule-segment
    def update_channel_stream_schedule_segment(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#delete-channel-stream-schedule-segment
    def delete_channel_stream_schedule_segment(self):
        pass
