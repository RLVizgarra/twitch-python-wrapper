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
        assert hash(self.client.chat.get_channel_emotes(broadcaster_id="141981764")) == 196265680831279960
        assert hash(self.client.chat.get_channel_emotes(broadcaster_id="12826")) == -5584805614351045098

    def test_get_global_emotes(self):
        assert hash(self.client.chat.get_global_emotes()) == -1911754963837804676

    def test_get_emote_sets(self):
        assert hash(self.client.chat.get_emote_sets(emote_set_id="301590448")) == 8199447653793326264
        assert hash(self.client.chat.get_emote_sets(emote_set_id="374814395")) == -1838195492418291180
        assert hash(self.client.chat.get_emote_sets(emote_set_id=["301590448", "374814395"])) == -8056364215214985908

    def test_get_channel_chat_badges(self):
        assert hash(self.client.chat.get_channel_chat_badges("12826")) ==8269109171712613325
        assert hash(self.client.chat.get_channel_chat_badges("197886470")) == -3076710540262200488

    def test_get_global_chat_badges(self):
        assert hash(self.client.chat.get_global_chat_badges()) == -2677478051108591865

    def test_get_chat_settings(self):
        assert hash(self.client.chat.get_chat_settings("141981764")) == 8585977543539151482
        assert hash(self.client.chat.get_chat_settings("12826")) == -2700731223437012002
