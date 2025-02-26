import httpx

from api.client import APIClient
from api.objects import Conduit


class Conduits:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-conduits
    def get_conduits(self) -> tuple[Conduit, ...] | None:
        url = self.client._url + "eventsub/conduits"

        req = httpx.get(url,
                        headers=self.client._headers,
                        timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()["data"]

        if len(res) < 1: return None

        conduits = list()
        for conduit in res:
            conduits.append(Conduit(id=conduit["id"],
                                    shard_count=conduit["shard_count"]))

        return tuple(conduits)

    # https://dev.twitch.tv/docs/api/reference/#create-conduits
    def create_conduits(self,
                        shard_count: int) -> Conduit:
        url = self.client._url + "eventsub/conduits"

        req = httpx.post(url,
                         json={"shard_count": shard_count},
                         headers=self.client._headers,
                         timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()["data"][0]

        return Conduit(id=res["id"],
                       shard_count=res["shard_count"])

    # https://dev.twitch.tv/docs/api/reference/#update-conduits
    def update_conduits(self,
                        conduit_id: str,
                        shard_count: int) -> Conduit:
        url = self.client._url + "eventsub/conduits"

        req = httpx.patch(url,
                          json={"id": conduit_id, "shard_count": shard_count},
                          headers=self.client._headers,
                          timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()["data"][0]

        return Conduit(id=res["id"],
                       shard_count=res["shard_count"])

    # https://dev.twitch.tv/docs/api/reference/#delete-conduit
    def delete_conduit(self,
                        conduit_id: str) -> None:
        url = self.client._url + "eventsub/conduits"

        req = httpx.delete(url,
                           params={"id": conduit_id},
                           headers=self.client._headers,
                           timeout=self.client._timeout)
        req.raise_for_status()

    # https://dev.twitch.tv/docs/api/reference/#get-conduit-shards
    def get_conduit_shards(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-conduit-shards
    def update_conduit_shards(self):
        pass
