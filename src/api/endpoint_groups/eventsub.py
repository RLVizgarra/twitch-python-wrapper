import httpx
from dateutil.parser import isoparse

from api.client import APIClient
from api.objects import Subscription
from shared_enums import SubscriptionType
from shared_objects import SubscriptionTransport


class EventSub:
    def __init__(self, client: APIClient):
        self.client = client

    # https://dev.twitch.tv/docs/api/reference/#create-eventsub-subscription
    def create_eventsub_subscription(self,
                                     subscription_type: SubscriptionType,
                                     version: str,
                                     condition: dict,
                                     transport: SubscriptionTransport) -> tuple[Subscription, int, int, int]:
        url = self.client._url + "eventsub/subscriptions"

        validation = {
            (transport.method == "webhook" and ((transport.callback is None or transport.secret is None) and (transport.session_id is not None or transport.conduit_id is not None))): "If transport.method is webhook then transport.callback and transport.secret must not be None and transport.session_id and transport.conduit_id must be None",
            (transport.method == "websocket" and ((transport.session_id is None) and (transport.callback is not None or transport.secret is not None or transport.conduit_id is not None))): "If transport.method is websocket then transport.session_id must not be None and transport.callback, transport.secret and transport.conduit_id must be None",
            (transport.method == "conduit" and ((transport.conduit_id is None) and (transport.callback is not None or transport.secret is not None or transport.session_id is not None))): "If transport.method is conduit then transport.conduit_id must not be None and transport.callback, transport.secret and transport.session_id must be None"
        }

        for validation_condition, error in validation.items():
            if validation_condition: raise ValueError(error)

        body = {
            "type": subscription_type.value,
            "version": version,
            "condition": condition,
            "transport": {
                "method": transport.method
            }
        }
        match transport.method:
            case "webhook":
                body["transport"]["callback"] = transport.callback
                body["transport"]["secret"] = transport.secret
            case "websocket":
                body["transport"]["session_id"] = transport.session_id
            case "conduit":
                body["transport"]["conduit_id"] = transport.conduit_id

        req = httpx.post(url,
                         json=body,
                         headers=self.client._headers,
                         timeout=self.client._timeout)
        req.raise_for_status()
        res = req.json()

        sub = res["data"][0]
        raw_res_transport = sub["transport"]
        res_transport = SubscriptionTransport(method=raw_res_transport["method"])

        match res_transport.method:
            case "webhook":
                res_transport.callback = raw_res_transport["callback"]
                res_transport.secret = raw_res_transport["secret"]
            case "websocket":
                res_transport.session_id = raw_res_transport["session_id"]
            case "conduit":
                res_transport.conduit_id = raw_res_transport["conduit_id"]

        subscription = Subscription(id=sub["id"],
                                    status=sub["status"],
                                    type=SubscriptionType(sub["type"]),
                                    version=sub["version"],
                                    condition=tuple(sorted((str(k), str(v)) for k, v in sub["condition"].items())),
                                    created_at=int(isoparse(sub["created_at"]).timestamp()),
                                    transport=res_transport,
                                    cost=sub["cost"])

        return subscription, res["total"], res["total_cost"], res["max_total_cost"]

    # https://dev.twitch.tv/docs/api/reference/#delete-eventsub-subscription
    def delete_eventsub_subscription(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-eventsub-subscriptions
    def get_eventsub_subscriptions(self):
        pass
