import httpx
from dateutil.parser import isoparse

from twitch_py_wrapper.api.client import APIClient
from twitch_py_wrapper.api.objects import BroadcasterTeams


class Teams:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-channel-teams
    def get_channel_teams(self,
                          broadcaster_id: str) -> BroadcasterTeams | tuple[BroadcasterTeams, ...] | None:
        url = self.client._url + "teams/channel"

        req = httpx.get(url,
                        params={"broadcaster_id": broadcaster_id},
                        headers=self.client._headers,
                        timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()["data"]

        if len(res) < 1: return None

        teams = list()
        for team in res:
            teams.append(BroadcasterTeams(broadcaster_id=team["broadcaster_id"],
                                          broadcaster_login=team["broadcaster_login"],
                                          broadcaster_name=team["broadcaster_name"],
                                          background_image_url=team["background_image_url"],
                                          banner=team["banner"],
                                          created_at=int(isoparse(team["created_at"]).timestamp()),
                                          updated_at=int(isoparse(team["updated_at"]).timestamp()),
                                          info=team["info"],
                                          thumbnail_url=team["thumbnail_url"],
                                          team_name=team["team_name"],
                                          team_display_name=team["team_display_name"],
                                          id=team["id"]))

        if len(teams) < 2: return teams[0]

        return tuple(teams)

    # https://dev.twitch.tv/docs/api/reference/#get-teams
    def get_teams(self):
        pass
