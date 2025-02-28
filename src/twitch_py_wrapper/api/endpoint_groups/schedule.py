from twitch_py_wrapper.api.client import APIClient


class Schedule:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-channel-stream-schedule
    def get_channel_stream_schedule(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-channel-icalendar
    def get_channel_icalendar(self):
        pass

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
