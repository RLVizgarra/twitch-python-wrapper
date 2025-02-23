import os

from dotenv import load_dotenv

from api.client import APIClient
from api.enums import UserType, BroadcasterType, VideoType
from api.objects import User, Video

load_dotenv()


class TestAPIClient:
    client = APIClient(os.getenv("CLIENT_ID"), os.getenv("APP_ACCESS_TOKEN"))

    def test_get_users(self):
        twitchdev = User(id='141981764', login='twitchdev', display_name='TwitchDev', type=UserType.NORMAL,
                         broadcaster_type=BroadcasterType.PARTNER,
                         description='Supporting third-party developers building Twitch integrations from chatbots to game integrations.',
                         profile_image_url='https://static-cdn.jtvnw.net/jtv_user_pictures/8a6381c7-d0c0-4576-b179-38bd5ce1d6af-profile_image-300x300.png',
                         offline_image_url='https://static-cdn.jtvnw.net/jtv_user_pictures/3f13ab61-ec78-4fe6-8481-8682cb3b0ac2-channel_offline_image-1920x1080.png',
                         email=None, created_at=1481747548)
        twitch = User(id="12826", login="twitch", display_name="Twitch", type=UserType.NORMAL,
                      broadcaster_type=BroadcasterType.PARTNER,
                      description="Twitch is where thousands of communities come together for whatever, every day. ",
                      profile_image_url="https://static-cdn.jtvnw.net/jtv_user_pictures/d5e6ebb4-a245-4ebf-bea6-2183e2f39600-profile_image-300x300.png",
                      offline_image_url="https://static-cdn.jtvnw.net/jtv_user_pictures/3f5f72bf-ae59-4470-8f8a-730d9ef87500-channel_offline_image-1920x1080.png",
                      email=None, created_at=1179830394)

        assert self.client.get_users(login="foo_bar_baz_qux") is None
        assert self.client.get_users(login="twitchdev") == twitchdev
        assert self.client.get_users(user_id="141981764") == twitchdev
        x = self.client.get_users(login=["twitchdev", "twitch"])
        assert twitchdev in x and twitch in x
        x = self.client.get_users(user_id=["141981764", "12826"])
        assert twitchdev in x and twitch in x
        x = self.client.get_users(login="twitchdev", user_id="12826")
        assert twitchdev in x and twitch in x

    def test_get_videos(self):
        twitchdev_video = Video(id='335921245', user_id='141981764', user_login='twitchdev', user_name='TwitchDev',
                                title='Twitch Developers 101',
                                description='Welcome to Twitch development! Here is a quick overview of our products and information to help you get started.',
                                created_at=1542231018, published_at=1542233070,
                                url='https://www.twitch.tv/videos/335921245',
                                thumbnail_url='https://static-cdn.jtvnw.net/cf_vods/d2nvs31859zcd8/twitchdev/335921245/ce0f3a7f-57a3-4152-bc06-0c6610189fb3/thumb/index-0000000000-%{width}x%{height}.jpg',
                                view_count=3078159, language='en', type=VideoType.UPLOAD, duration='3m21s',
                                muted_segments=[],
                                stream_id=None, viewable='public')

        x = self.client.get_videos(video_id="335921245")
        twitchdev_video.view_count = x.view_count
        assert x == twitchdev_video
