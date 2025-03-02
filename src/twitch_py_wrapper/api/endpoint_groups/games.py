import httpx

from twitch_py_wrapper.api.client import APIClient
from twitch_py_wrapper.api.objects import Pagination, Game


class Games:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-top-games
    def get_top_games(self,
                      first: int = None,
                      after: Pagination = None,
                      before: Pagination = None) -> tuple[Game, ...] | tuple[tuple[Game, ...], Pagination]:
        url = self.client._url + "games/top"

        if first and (first < 1 or first > 100):
            raise ValueError("Parameter first must be between 1 and 100")

        parameters = {}

        optional_params = {
            "first": first,
            "after": after.cursor if after else None,
            "before": before.cursor if before else None
        }

        for key, value in optional_params.items():
            if value: parameters[key] = value

        req = httpx.get(url,
                  params=parameters,
                  headers=self.client._headers,
                  timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()

        games = list()
        for game in res["data"]:
            games.append(Game(id=game["id"],
                              name=game["name"],
                              box_art_url=game["box_art_url"],
                              igdb_id=game["igdb_id"] if game["igdb_id"] != "" else None))

        if len(res["pagination"]) > 0: return tuple(games), Pagination(res["pagination"]["cursor"])

        return tuple(games)

    # https://dev.twitch.tv/docs/api/reference/#get-games
    def get_games(self):
        pass
