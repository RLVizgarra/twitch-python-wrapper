import httpx

from twitch_py_wrapper.api.client import APIClient
from twitch_py_wrapper.api.objects import Pagination, Category


class Search:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#search-categories
    def search_categories(self,
                          query: str,
                          first: int = None,
                          after: Pagination = None) -> Category | tuple[Category, ...] | tuple[tuple[Category, ...], Pagination] | None:
        url = self.client._url + "search/categories"

        if first and (first < 1 or first > 100):
            raise ValueError("Parameter first must be between 1 and 100")

        parameters = {"query": query}

        optional_params = {
            "first": first,
            "after": after.cursor if after else None
        }

        for key, value in optional_params.items():
            if value: parameters[key] = value

        req = httpx.get(url,
                        params=parameters,
                        headers=self.client._headers,
                        timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()

        if len(res["data"]) < 1: return None

        categories = list()
        for category in res["data"]:
            categories.append(Category(id=category["id"],
                                       name=category["name"],
                                       box_art_url="https://static-cdn.jtvnw.net/ttv-boxart/" + category["id"] + "-{width}x{height}.jpg",
                                       igdb_id=None))

        if len(categories) < 2: return categories[0]

        if len(res["pagination"]) > 0: return tuple(categories), Pagination(cursor=res["pagination"]["cursor"])

        return tuple(categories)

    # https://dev.twitch.tv/docs/api/reference/#search-channels
    def search_channels(self):
        pass
