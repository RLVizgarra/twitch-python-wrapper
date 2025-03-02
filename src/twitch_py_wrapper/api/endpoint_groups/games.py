import httpx

from twitch_py_wrapper.api.client import APIClient
from twitch_py_wrapper.api.objects import Pagination, Category


class Games:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-top-games
    def get_top_games(self,
                      first: int = None,
                      after: Pagination = None,
                      before: Pagination = None) -> tuple[Category, ...] | tuple[tuple[Category, ...], Pagination]:
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
            games.append(Category(id=game["id"],
                                  name=game["name"],
                                  box_art_url=game["box_art_url"],
                                  igdb_id=game["igdb_id"] if game["igdb_id"] != "" else None))

        if len(res["pagination"]) > 0: return tuple(games), Pagination(res["pagination"]["cursor"])

        return tuple(games)

    # https://dev.twitch.tv/docs/api/reference/#get-games
    def get_games(self,
                  game_id: str | list[str] = None,
                  name: str | list[str] = None,
                  igdb_id: str | list[str] = None) -> Category | tuple[Category, ...] | None:
        url = self.client._url + "games"

        sum_of_lookups = 0

        if isinstance(game_id, list):
            sum_of_lookups += len(game_id)
        elif game_id:
            sum_of_lookups += 1

        if isinstance(name, list):
            sum_of_lookups += len(name)
        elif name:
            sum_of_lookups += 1

        if isinstance(igdb_id, list):
            sum_of_lookups += len(igdb_id)
        elif igdb_id:
            sum_of_lookups += 1

        if sum_of_lookups > 100:
            raise ValueError("Cannot look up for 100+ IDs and/or names")

        parameters = {}

        optional_params = {
            "id": game_id,
            "name": name,
            "igdb_id": igdb_id
        }

        for key, value in optional_params.items():
            if key: parameters[key] = value

        req = httpx.get(url,
                        params=parameters,
                        headers=self.client._headers,
                        timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()["data"]

        if len(res) < 1: return None

        games = list()
        for game in res:
            games.append(Category(id=game["id"],
                                  name=game["name"],
                                  box_art_url=game["box_art_url"],
                                  igdb_id=game["igdb_id"]))

        if len(games) < 2: return games[0]

        return tuple(games)
