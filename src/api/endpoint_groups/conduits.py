import httpx

from api.client import APIClient
from api.enums import ConduitShardStatus
from api.objects import Conduit, Pagination, ConduitShard
from shared_enums import NotificationTransportMethod
from shared_objects import NotificationTransport


class Conduits:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-conduits
    def get_conduits(self) -> Conduit | tuple[Conduit, ...] | None:
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

        if len(conduits) < 2: return conduits[0]

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
    def get_conduit_shards(self,
                           conduit_id: str,
                           status: ConduitShardStatus | None,
                           after: Pagination | None) -> ConduitShard | tuple[ConduitShard, ...] | tuple[tuple[ConduitShard, ...], Pagination] | None:
        url = self.client._url + "eventsub/conduits/shards"

        parameters = {"conduit_id": conduit_id}

        optional_params = {
            "status": status,
            "after": after.cursor
        }

        for key, value in optional_params:
            if value: parameters[key] = value

        req = httpx.get(url,
                        params=parameters,
                        headers=self.client._headers,
                        timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()

        if len(res["data"]) < 1: return None

        shards = list()
        for shard in res:
            transport = NotificationTransport(method=NotificationTransportMethod(shard["transport"]["method"]),
                                              callback=shard["transport"]["callback"] if shard["transport"]["callback"] else None,
                                              secret=shard["transport"]["secret"] if shard["transport"]["secret"] else None,
                                              session_id=shard["transport"]["session_id"] if shard["transport"]["session_id"] else None,
                                              conduit_id=shard["transport"]["conduit_id"] if shard["transport"]["conduit_id"] else None,
                                              connected_at=shard["transport"]["connected_at"] if shard["transport"]["connected_at"] else None,
                                              disconnected_at=shard["transport"]["disconnected_at"] if shard["transport"]["disconnected_at"] else None)

            shards.append(ConduitShard(id=shard["id"],
                                       status=ConduitShardStatus(shard["status"]),
                                       transport=transport))

        if len(shards) < 2: return shards[0]

        if len(res["pagination"]) > 0: return tuple(shards), Pagination(res["pagination"]["cursor"])

        return tuple(shards)

    # https://dev.twitch.tv/docs/api/reference/#update-conduit-shards
    def update_conduit_shards(self):
        pass
