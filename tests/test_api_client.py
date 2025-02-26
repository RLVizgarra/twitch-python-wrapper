import os

from dotenv import load_dotenv

from api.client import APIClient

load_dotenv()

class TestAPIClient:
    client = APIClient(os.getenv("CLIENT_ID"), os.getenv("APP_ACCESS_TOKEN"))

    def test_get_users(self):
        first_user = 95983915723945059
        second_user = -4084956926418039017

        assert self.client.users.get_users(login="foo_bar_baz_qux") is None
        assert hash(self.client.users.get_users(login="twitchdev")) == first_user
        assert hash(self.client.users.get_users(user_id="141981764")) == first_user
        us = self.client.users.get_users(login=["twitchdev", "twitch"])
        for u in us:
            assert hash(u) == first_user or hash(u) == second_user
        us = self.client.users.get_users(user_id=["141981764", "12826"])
        for u in us:
            assert hash(u) == first_user or hash(u) == second_user
        us = self.client.users.get_users(login="twitchdev", user_id="12826")
        for u in us:
            assert hash(u) == first_user or hash(u) == second_user

    def test_get_videos(self):
        assert self.client.videos.get_videos(video_id="123456789123") is None
        assert hash(self.client.videos.get_videos(video_id="335921245")) == 4462134045647488878

    def test_get_clips(self):
        assert self.client.clips.get_clips(clip_id="AwkwardHelplessSalamanderSwiftRage") is None
        assert hash(self.client.clips.get_clips(clip_id="ObedientRelievedPepperoniSwiftRage")) == 4781649331344373151
        assert hash(self.client.clips.get_clips(broadcaster_id="141981764", first=5)) == 5772613717331245050

    def test_get_cheermotes(self):
        assert hash(self.client.bits.get_cheermotes(broadcaster_id="141981764")) == -3447302537155689151

    def test_get_channel_information(self):
        assert hash(self.client.channels.get_channel_information(broadcaster_id="141981764")) == -3908995204320117461
        assert hash(self.client.channels.get_channel_information(broadcaster_id="12826")) == -27976972557750373
        assert hash(self.client.channels.get_channel_information(broadcaster_id=["141981764", "12826"])) == -5573906658155913568

    def test_get_channel_emotes(self):
        assert hash(self.client.chat.get_channel_emotes(broadcaster_id="141981764")) == 1068135883675233598
        assert hash(self.client.chat.get_channel_emotes(broadcaster_id="12826")) == 7332780091495282608
