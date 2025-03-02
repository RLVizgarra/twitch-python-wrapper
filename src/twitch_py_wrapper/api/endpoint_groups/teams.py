import httpx
from dateutil.parser import isoparse

from twitch_py_wrapper.api.client import APIClient
from twitch_py_wrapper.api.objects import BroadcasterTeam, Team, TeamUser


class Teams:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-channel-teams
    def get_channel_teams(self,
                          broadcaster_id: str) -> BroadcasterTeam | tuple[BroadcasterTeam, ...] | None:
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
            teams.append(BroadcasterTeam(broadcaster_id=team["broadcaster_id"],
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
    def get_teams(self,
                  name: str = None,
                  team_id: str = None) -> Team | None:
        url = self.client._url + "teams"

        if name is None and team_id is None:
            raise ValueError("Parameters name and team_id are mutually exclusive")

        parameters = {}

        optional_params = {
            "name": name,
            "id": team_id
        }

        for key, value in optional_params.items():
            if value: parameters[key] = value

        req = httpx.get(url,
                        params=parameters,
                        headers=self.client._headers,
                        timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()["data"]

        if len(res) < 1: return None
        res = res[0]

        users = list()
        for user in res["users"]:
            users.append(TeamUser(user_id=user["user_id"],
                                  user_login=user["user_login"],
                                  user_name=user["user_name"]))

        return Team(users=tuple(users),
                    background_image_url=res["background_image_url"],
                    banner=res["banner"],
                    created_at=int(isoparse(res["created_at"]).timestamp()),
                    updated_at=int(isoparse(res["updated_at"]).timestamp()),
                    info=res["info"],
                    thumbnail_url=res["thumbnail_url"],
                    team_name=res["team_name"],
                    team_display_name=res["team_display_name"],
                    id=res["id"])
