import os

from dotenv import load_dotenv

from api.client import APIClient
from api.enums import UserType, BroadcasterType, VideoType
from api.objects import User, Video, Clip, Pagination

load_dotenv()


class TestAPIClient:
    client = APIClient(os.getenv("CLIENT_ID"), os.getenv("APP_ACCESS_TOKEN"))

    def test_get_users(self):
        first_user = User(id='141981764',
                          login='twitchdev',
                          display_name='TwitchDev',
                          type=UserType.NORMAL,
                          broadcaster_type=BroadcasterType.PARTNER,
                          description='Supporting third-party developers building Twitch integrations from chatbots to game integrations.',
                          profile_image_url='https://static-cdn.jtvnw.net/jtv_user_pictures/8a6381c7-d0c0-4576-b179-38bd5ce1d6af-profile_image-300x300.png',
                          offline_image_url='https://static-cdn.jtvnw.net/jtv_user_pictures/3f13ab61-ec78-4fe6-8481-8682cb3b0ac2-channel_offline_image-1920x1080.png',
                          email=None,
                          created_at=1481747548)
        second_user = User(id="12826", login="twitch",
                           display_name="Twitch",
                           type=UserType.NORMAL,
                           broadcaster_type=BroadcasterType.PARTNER,
                           description="Twitch is where thousands of communities come together for whatever, every day. ",
                           profile_image_url="https://static-cdn.jtvnw.net/jtv_user_pictures/d5e6ebb4-a245-4ebf-bea6-2183e2f39600-profile_image-300x300.png",
                           offline_image_url="https://static-cdn.jtvnw.net/jtv_user_pictures/3f5f72bf-ae59-4470-8f8a-730d9ef87500-channel_offline_image-1920x1080.png",
                           email=None,
                           created_at=1179830394)

        assert self.client.get_users(login="foo_bar_baz_qux") is None
        assert self.client.get_users(login="twitchdev") == first_user
        assert self.client.get_users(user_id="141981764") == first_user
        x = self.client.get_users(login=["twitchdev", "twitch"])
        assert first_user in x and second_user in x
        x = self.client.get_users(user_id=["141981764", "12826"])
        assert first_user in x and second_user in x
        x = self.client.get_users(login="twitchdev", user_id="12826")
        assert first_user in x and second_user in x

    def test_get_videos(self):
        video = Video(id='335921245',
                      user_id='141981764',
                      user_login='twitchdev',
                      user_name='TwitchDev',
                      title='Twitch Developers 101',
                      description='Welcome to Twitch development! Here is a quick overview of our products and information to help you get started.',
                      created_at=1542231018,
                      published_at=1542233070,
                      url='https://www.twitch.tv/videos/335921245',
                      thumbnail_url='https://static-cdn.jtvnw.net/cf_vods/d2nvs31859zcd8/twitchdev/335921245/ce0f3a7f-57a3-4152-bc06-0c6610189fb3/thumb/index-0000000000-%{width}x%{height}.jpg',
                      view_count=1863062,
                      language='en',
                      type=VideoType.UPLOAD,
                      duration='3m21s',
                      muted_segments=[],
                      stream_id=None,
                      viewable='public')

        assert self.client.get_videos(video_id="123456789123") is None
        x = self.client.get_videos(video_id="335921245")
        video.view_count = x.view_count
        assert x == video

    def test_get_clips(self):
        first_clip = Clip(id='ObedientRelievedPepperoniSwiftRage',
                          url='https://clips.twitch.tv/ObedientRelievedPepperoniSwiftRage',
                          embed_url='https://clips.twitch.tv/embed?clip=ObedientRelievedPepperoniSwiftRage',
                          broadcaster_id='141981764',
                          broadcaster_name='TwitchDev',
                          creator_id='75907964',
                          creator_name='PyroShield793',
                          video_id='327237000',
                          game_id='509670',
                          language='en',
                          title='TOS D:',
                          view_count=1153,
                          created_at=1540493441,
                          thumbnail_url='https://static-cdn.jtvnw.net/twitch-clips/AT-cm%7C331592365-preview-480x272.jpg',
                          duration=34.1,
                          vod_offset=8124,
                          is_featured=False)
        second_clips = ([Clip(id='LivelySaltyAyeayeNerfRedBlaster',
                              url='https://clips.twitch.tv/LivelySaltyAyeayeNerfRedBlaster',
                              embed_url='https://clips.twitch.tv/embed?clip=LivelySaltyAyeayeNerfRedBlaster',
                              broadcaster_id='141981764',
                              broadcaster_name='TwitchDev',
                              creator_id='39214945',
                              creator_name='batc_',
                              video_id='327237000',
                              game_id='509670',
                              language='en',
                              title='YIKES',
                              view_count=205699,
                              created_at=1540496403,
                              thumbnail_url='https://static-cdn.jtvnw.net/twitch-clips/AT-cm%7C331619892-preview-480x272.jpg',
                              duration=22.4,
                              vod_offset=11395,
                              is_featured=False),
                         Clip(id='ArborealAlertKleeTheThing',
                              url='https://clips.twitch.tv/ArborealAlertKleeTheThing',
                              embed_url='https://clips.twitch.tv/embed?clip=ArborealAlertKleeTheThing',
                              broadcaster_id='141981764',
                              broadcaster_name='TwitchDev',
                              creator_id='138187893',
                              creator_name='ayyyyy_rik',
                              video_id='183456518',
                              game_id='',
                              language='en',
                              title='Pay 2 win',
                              view_count=96259,
                              created_at=1508437238,
                              thumbnail_url='https://static-cdn.jtvnw.net/twitch-clips/140663156-preview-480x272.jpg',
                              duration=25.8,
                              vod_offset=1894,
                              is_featured=False),
                         Clip(id='WimpyBumblingClipsmomDancingBanana',
                              url='https://clips.twitch.tv/WimpyBumblingClipsmomDancingBanana',
                              embed_url='https://clips.twitch.tv/embed?clip=WimpyBumblingClipsmomDancingBanana',
                              broadcaster_id='141981764',
                              broadcaster_name='TwitchDev',
                              creator_id='42146490',
                              creator_name='Scubaz',
                              video_id='398950655',
                              game_id='509658',
                              language='en',
                              title='1',
                              view_count=39415,
                              created_at=1553198887,
                              thumbnail_url='https://static-cdn.jtvnw.net/twitch-clips/AT-cm%7C422800962-preview-480x272.jpg',
                              duration=51.1,
                              vod_offset=7232,
                              is_featured=False),
                         Clip(id='FairTawdryWatercressCorgiDerp',
                              url='https://clips.twitch.tv/FairTawdryWatercressCorgiDerp',
                              embed_url='https://clips.twitch.tv/embed?clip=FairTawdryWatercressCorgiDerp',
                              broadcaster_id='141981764',
                              broadcaster_name='TwitchDev',
                              creator_id='42146490',
                              creator_name='Scubaz',
                              video_id='398950655',
                              game_id='509658',
                              language='en',
                              title='2',
                              view_count=37582,
                              created_at=1553198903,
                              thumbnail_url='https://static-cdn.jtvnw.net/twitch-clips/AT-cm%7C422801162-preview-480x272.jpg',
                              duration=17,
                              vod_offset=7282,
                              is_featured=False),
                         Clip(id='BoredRacySheepPRChase',
                              url='https://clips.twitch.tv/BoredRacySheepPRChase',
                              embed_url='https://clips.twitch.tv/embed?clip=BoredRacySheepPRChase',
                              broadcaster_id='141981764',
                              broadcaster_name='TwitchDev',
                              creator_id='136707671',
                              creator_name='porcupinetv',
                              video_id='171283183',
                              game_id='417752',
                              language='en',
                              title="Porcupine's Kappa Pet and Live Emote Reactions",
                              view_count=3226,
                              created_at=1504221448,
                              thumbnail_url='https://static-cdn.jtvnw.net/twitch-clips/26150143088-offset-3096-preview-480x272.jpg',
                              duration=29,
                              vod_offset=3072,
                              is_featured=False)],
                        Pagination(cursor='eyJiIjpudWxsLCJhIjp7IkN1cnNvciI6Ik5RPT0ifX0'))

        assert self.client.get_clips(clip_id="AwkwardHelplessSalamanderSwiftRage") is None
        assert self.client.get_clips(clip_id="ObedientRelievedPepperoniSwiftRage") == first_clip
        assert self.client.get_clips(broadcaster_id="141981764", first=5) == second_clips
