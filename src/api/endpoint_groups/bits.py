import httpx
from dateutil.parser import isoparse

from api.client import APIClient
from api.enums import CheermoteType
from api.objects import Cheermote, CheerTier


class Bits:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#get-bits-leaderboard
    def get_bits_leaderboard(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-cheermotes
    def get_cheermotes(self,
                       broadcaster_id: str = None) -> tuple[Cheermote, ...]:
        url = self.client._url + "bits/cheermotes"

        if broadcaster_id: parameters = {"broadcaster_id": broadcaster_id}
        else: parameters = {}

        req = httpx.get(url, params=parameters, headers=self.client._headers, timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()["data"]

        cheermotes = list()
        for cheermote in res:
            cheer_tiers = list()
            for tier in cheermote["tiers"]:
                cheer_tiers.append(CheerTier(min_bits=tier["min_bits"],
                                       id=tier["id"],
                                       color=tier["color"],
                                       images=tuple(sorted((str(k), str(v)) for k, v in tier["images"].items())),
                                       can_cheer=tier["can_cheer"],
                                       show_in_bits_card=tier["show_in_bits_card"]))

            cheermotes.append(Cheermote(prefix=cheermote["prefix"],
                                        tiers=tuple(cheer_tiers),
                                        type=CheermoteType(cheermote["type"]),
                                        order=cheermote["order"],
                                        last_update=int(isoparse(cheermote["last_updated"]).timestamp()),
                                        is_charitable=cheermote["is_charitable"]))

        return tuple(cheermotes)

    # https://dev.twitch.tv/docs/api/reference/#get-extension-transactions
    def get_extension_transactions(self):
        pass
