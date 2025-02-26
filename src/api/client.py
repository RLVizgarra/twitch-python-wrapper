class APIClient:
    def __init__(self,
                 client_id: str,
                 access_token: str,
                 timeout: float = 5.0):
        self._url = "https://api.twitch.tv/helix/"
        self.__headers = {
            "Authorization": "Bearer " + access_token,
            "Client-Id": client_id
        }
        self._timeout = timeout

        from api.endpoint_groups.ads import Ads
        from api.endpoint_groups.analytics import Analytics
        from api.endpoint_groups.bits import Bits
        from api.endpoint_groups.channels import Channels
        from api.endpoint_groups.channel_points import ChannelPoints
        from api.endpoint_groups.charity import Charity
        from api.endpoint_groups.chat import Chat
        from api.endpoint_groups.clips import Clips
        from api.endpoint_groups.conduits import Conduits
        from api.endpoint_groups.ccls import CCLs
        from api.endpoint_groups.entitlements import Entitlements
        from api.endpoint_groups.extensions import Extensions
        from api.endpoint_groups.eventsub import EventSub
        from api.endpoint_groups.games import Games
        from api.endpoint_groups.goals import Goals
        from api.endpoint_groups.hype_train import HypeTrain
        from api.endpoint_groups.moderation import Moderation
        from api.endpoint_groups.polls import Polls
        from api.endpoint_groups.predictions import Predictions
        from api.endpoint_groups.schedule import Schedule
        from api.endpoint_groups.search import Search
        from api.endpoint_groups.streams import Streams
        from api.endpoint_groups.subscriptions import Subscriptions
        from api.endpoint_groups.tags import Tags
        from api.endpoint_groups.teams import Teams
        from api.endpoint_groups.users import Users
        from api.endpoint_groups.videos import Videos
        from api.endpoint_groups.whispers import Whispers

        self.ads = Ads(self)
        self.analytics = Analytics(self)
        self.bits = Bits(self)
        self.channels = Channels(self)
        self.channel_points = ChannelPoints(self)
        self.charity = Charity(self)
        self.chat = Chat(self)
        self.clips = Clips(self)
        self.conduits = Conduits(self)
        self.ccls = CCLs(self)
        self.entitlements = Entitlements(self)
        self.extensions = Extensions(self)
        self.eventsub = EventSub(self)
        self.games = Games(self)
        self.goals = Goals(self)
        self.hype_train = HypeTrain(self)
        self.moderation = Moderation(self)
        self.polls = Polls(self)
        self.predictions = Predictions(self)
        self.schedule = Schedule(self)
        self.search = Search(self)
        self.streams = Streams(self)
        self.subscriptions = Subscriptions(self)
        self.tags = Tags(self)
        self.teams = Teams(self)
        self.users = Users(self)
        self.videos = Videos(self)
        self.whispers = Whispers(self)

    @property
    def _headers(self):
        return self.__headers
