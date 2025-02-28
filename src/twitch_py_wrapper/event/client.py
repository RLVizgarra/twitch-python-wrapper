import asyncio
import json
import ssl
import time
from typing import Callable, Literal

import certifi
import websockets
from dateutil.parser import isoparse

from twitch_py_wrapper.api.client import APIClient
from twitch_py_wrapper.event.enums import MessageType
from twitch_py_wrapper.event.objects import Metadata
from twitch_py_wrapper.shared_enums import SubscriptionType, NotificationTransportMethod
from twitch_py_wrapper.shared_objects import NotificationTransport

BuiltinNotifications = Literal["builtins.message.welcome",
                         "builtins.message.keepalive",
                         "builtins.message.notification",
                         "builtins.message.reconnect",
                         "builtins.message.revocation"]

class EventClient:
    _ssl = ssl.create_default_context()
    _ssl.load_verify_locations(certifi.where())


    def __init__(self, client_id: str, access_token: str, url: str = None, timeout: int = 10):
        self._api = APIClient(client_id, access_token)
        self._timeout = timeout

        self._url = url if url else "wss://eventsub.wss.twitch.tv/ws?keepalive_timeout_seconds=" + str(self._timeout)
        self._registered_event_handlers: list[dict] = []
        self._previous_messages: list[str] = []
        self.__ws = None

    def on(self, subscription: SubscriptionType | BuiltinNotifications, version: str = None, condition: dict = None):
        validation = {
            ((not version and not condition) and isinstance(subscription, SubscriptionType)): "When subscription is a SubscriptionType, version and condition must be supplied",
            ((version and condition) and not isinstance(subscription, SubscriptionType)): "When subscription is a string, version and condition must not be supplied",
        }

        for validation_condition, error in validation.items():
            if validation_condition:
                raise ValueError(error)

        def callback(function: Callable[[Metadata, dict], None]):
            self._registered_event_handlers.append({
                "subscription": subscription,
                "condition": condition,
                "version": version,
                "callback": function,
                "registered": False
            })
            return function
        return callback

    def __register(self, handler: dict, session_id: str):
        if handler["registered"]: return

        self._api.eventsub.create_eventsub_subscription(subscription_type=handler["subscription"],
                                               version=handler["version"],
                                               condition=handler["condition"],
                                               transport=NotificationTransport(method=NotificationTransportMethod.WEBSOCKET,
                                                                               callback=None,
                                                                               secret=None,
                                                                               session_id=session_id,
                                                                               conduit_id=None,
                                                                               connected_at=None,
                                                                               disconnected_at=None))
        handler["registered"] = True

    def _trigger_notification(self, metadata: Metadata, payload: dict):
        if not metadata.subscription_type or not isinstance(metadata.subscription_type, SubscriptionType): return

        handler = None
        for event_handler in self._registered_event_handlers:
            if event_handler["subscription"] != metadata.subscription_type: continue
            handler = event_handler
            break
        if handler: handler["callback"](metadata, payload)

    def _trigger_message(self, metadata: Metadata, payload: dict):
        message_type = metadata.message_type.value
        if "_" in message_type:
            message_type = message_type.split("_")[1]

        subscription = "builtins.message." + message_type
        handler = None
        for event_handler in self._registered_event_handlers:
            if event_handler["subscription"] != subscription: continue
            handler = event_handler
            break
        if handler: handler["callback"](metadata, payload)

    async def connect(self):
        while True:
            async with websockets.connect(self._url, ssl=self._ssl if self._url.startswith("wss") else None) as self.__ws:
                try:
                    while True:
                        raw_message = await asyncio.wait_for(self.__ws.recv(), timeout=self._timeout + 1)
                        message = json.loads(raw_message)
                        metadata = Metadata(message_id=message["metadata"]["message_id"],
                                 message_type=MessageType(message["metadata"]["message_type"]),
                                 message_timestamp=int(isoparse(message["metadata"]["message_timestamp"]).timestamp()),
                                 subscription_type=SubscriptionType(message["metadata"]["subscription_type"]) if "subscription_type" in message["metadata"] else None,
                                 subscription_version=message["metadata"]["subscription_version"] if "subscription_version" in message["metadata"] else None)
                        payload = message["payload"]

                        if metadata.message_timestamp < time.time() - 10*60 or self._previous_messages.count(metadata.message_id) > 0: continue
                        self._previous_messages.append(metadata.message_id)

                        match metadata.message_type:
                            case MessageType.SESSION_WELCOME:
                                session_id: str = payload["session"]["id"]
                                if not self._timeout: self._timeout = payload["session"]["keepalive_timeout_seconds"]
                                for handler in self._registered_event_handlers:
                                    if not isinstance(handler["subscription"], SubscriptionType): continue
                                    self.__register(handler, session_id)

                            case MessageType.NOTIFICATION:
                                self._trigger_notification(metadata, payload)

                            case MessageType.REVOCATION:
                                handler = None
                                for event_handler in self._registered_event_handlers:
                                    if event_handler["subscription"] != SubscriptionType(payload["subscription"]["type"] or event_handler["condition"] != payload["subscription"]["condition"]): continue
                                    handler = event_handler
                                    break
                                if handler: self._registered_event_handlers.remove(handler)

                            case MessageType.SESSION_RECONNECT:
                                self._url = payload["session"]["reconnect_url"]
                                await self.__ws.close()
                                break

                        self._trigger_message(metadata, payload)

                except asyncio.TimeoutError:
                    await self.__ws.close()

                except websockets.ConnectionClosed:
                    await self.__ws.close()

                except asyncio.CancelledError or KeyboardInterrupt:
                    await self.__ws.close()
                    break

            await asyncio.sleep(5)
