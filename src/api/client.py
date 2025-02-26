from datetime import datetime

import httpx
import pytz
from dateutil import parser

from api.objects import *
from shared_enums import SubscriptionType


class APIClient:
    def __init__(self,
                 client_id: str,
                 access_token: str,
                 timeout: float = httpx._config.DEFAULT_TIMEOUT_CONFIG):
        self._url = "https://api.twitch.tv/helix/"
        self.__headers = {
            "Authorization": "Bearer " + access_token,
            "Client-Id": client_id
        }
        self._timeout = timeout

    # https://dev.twitch.tv/docs/api/reference/#start-commercial
    def start_commercial(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-ad-schedule
    def get_ad_schedule(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#snooze-next-ad
    def snooze_next_ad(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-extension-analytics
    def get_extension_analytics(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-bits-leaderboard
    def get_bits_leaderboard(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-cheermotes
    def get_cheermotes(self,
                       broadcaster_id: str = None) -> tuple[Cheermote, ...]:
        url = self._url + "bits/cheermotes"

        if broadcaster_id: parameters = {"broadcaster_id": broadcaster_id}
        else: parameters = {}

        req = httpx.get(url, params=parameters, headers=self.__headers, timeout=self._timeout)
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
                                        last_update=int(parser.isoparse(cheermote["last_updated"]).timestamp()),
                                        is_charitable=cheermote["is_charitable"]))

        return tuple(cheermotes)

    # https://dev.twitch.tv/docs/api/reference/#get-extension-transactions
    def get_extension_transactions(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-channel-information
    def get_channel_information(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#modify-channel-information
    def modify_channel_information(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-channel-editors
    def get_channel_editors(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-followed-channels
    def get_followed_channels(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#create-custom-rewards
    def create_custom_rewards(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#delete-custom-reward
    def delete_custom_reward(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-custom-reward
    def get_custom_reward(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-custom-reward-redemption
    def get_custom_reward_redemption(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-custom-reward
    def update_custom_reward(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-redemption-status
    def update_redemption_status(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-charity-campaign
    def get_charity_campaign(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-charity-campaign-donations
    def get_charity_campaign_donations(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-chatters
    def get_chatters(self):
        pass
    
    # https://dev.twitch.tv/docs/api/reference/#get-channel-emotes
    def get_channel_emotes(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-global-emotes
    def get_global_emotes(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-emote-sets
    def get_emote_sets(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-channel-chat-badges
    def get_channel_chat_badges(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-global-chat-badges
    def get_global_chat_badges(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-chat-settings
    def get_chat_settings(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-shared-chat-session
    def get_shared_chat_session(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-user-emotes
    def get_user_emotes(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-chat-settings
    def update_chat_settings(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#send-chat-announcement
    def send_chat_announcement(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#send-a-shoutout
    def send_a_shoutout(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#send-chat-message
    def send_chat_message(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-user-chat-color
    def get_user_chat_color(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-user-chat-color
    def update_user_chat_color(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#create-clip
    def create_clip(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-clips
    def get_clips(self,
                  broadcaster_id: str = None,
                  game_id: str = None,
                  clip_id: str | list[str] = None,
                  started_at: int = None,
                  ended_at: int = None,
                  first: int = None,
                  before: Pagination = None,
                  after: Pagination = None,
                  is_featured: bool = None) -> Clip | tuple[Clip, ...] | tuple[tuple[Clip, ...], Pagination] | None:
        url = self._url + "clips"

        validation = {
            (broadcaster_id is None and game_id is None and clip_id is None): "Parameters broadcaster_id, game_id and clip_id are mutually exclusive",
            (type(clip_id) is list and len(clip_id) > 100): "Cannot look up for 100+ IDs",
            (first and (first < 1 or first > 100)): "Parameter first must be between 1 and 100"
        }

        for condition, error in validation.items():
            if condition: raise ValueError(error)

        if clip_id: parameters = {"id": clip_id}
        elif broadcaster_id and game_id: parameters = {"broadcaster_id": broadcaster_id, "game_id": game_id}
        elif broadcaster_id: parameters = {"broadcaster_id": broadcaster_id}
        else: parameters = {"game_id": game_id}

        optional_params = {
            "started_at": datetime.fromtimestamp(started_at, tz=pytz.utc).isoformat("T")[:-6] + "Z" if started_at else None,
            "ended_at": datetime.fromtimestamp(ended_at, tz=pytz.utc).isoformat("T")[:-6] + "Z" if ended_at else None,
            "first": first,
            "before": before.cursor if before else None,
            "after": after.cursor if after else None,
            "is_featured": is_featured
        }

        for key, value in optional_params.items():
            if value: parameters[key] = value

        req = httpx.get(url, params=parameters, headers=self.__headers, timeout=self._timeout)

        if req.status_code == 404:
            return None

        req.raise_for_status()
        res = req.json()

        if len(res["data"]) < 1: return None

        clips = list()
        for clip in res["data"]:
            clips.append(Clip(id=clip["id"],
                              url=clip["url"],
                              embed_url=clip["embed_url"],
                              broadcaster_id=clip["broadcaster_id"],
                              broadcaster_name=clip["broadcaster_name"],
                              creator_id=clip["creator_id"],
                              creator_name=clip["creator_name"],
                              video_id=clip["video_id"] if clip["video_id"] != "" else None,
                              game_id=clip["game_id"],
                              language=clip["language"],
                              title=clip["title"],
                              view_count=clip["view_count"],
                              created_at=int(parser.isoparse(clip["created_at"]).timestamp()),
                              thumbnail_url=clip["thumbnail_url"],
                              duration=clip["duration"],
                              vod_offset=clip["vod_offset"],
                              is_featured=clip["is_featured"]))

        if len(clips) < 2: return clips[0]

        if len(res["pagination"]) > 0: return tuple(clips), Pagination(res["pagination"]["cursor"])

        return tuple(clips)

    # https://dev.twitch.tv/docs/api/reference/#get-conduits
    def get_conduits(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#create-conduits
    def create_conduits(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-conduits
    def update_conduits(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#delete-conduit
    def delete_conduit(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-conduit-shards
    def get_conduit_shards(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-conduit-shards
    def update_conduit_shards(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-content-classification-labels
    def get_content_classification_labels(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-drops-entitlements
    def get_drops_entitlements(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-drops-entitlements
    def update_drops_entitlements(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-extension-configuration-segment
    def get_extension_configuration_segment(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#set-extension-configuration-segment
    def set_extension_configuration_segment(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#set-extension-required-configuration
    def set_extension_required_configuration(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#send-extension-pubsub-message
    def send_extension_pubsub_message(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-extension-live-channels
    def get_extension_live_channels(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-extension-secrets
    def get_extension_secrets(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#create-extension-secret
    def create_extension_secret(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#send-extension-chat-message
    def send_extension_chat_message(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-extensions
    def get_extensions(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-released-extensions
    def get_released_extensions(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-extension-bits-products
    def get_extension_bits_products(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-extension-bits-product
    def update_extension_bits_product(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#create-eventsub-subscription
    def create_eventsub_subscription(self,
                                     subscription_type: SubscriptionType,
                                     version: str,
                                     condition: dict,
                                     transport: SubscriptionTransport) -> tuple[Subscription, int, int, int]:
        url = self._url + "eventsub/subscriptions"

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

        req = httpx.post(url, json=body, headers=self.__headers, timeout=self._timeout)
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
                                    created_at=int(parser.isoparse(sub["created_at"]).timestamp()),
                                    transport=res_transport,
                                    cost=sub["cost"])

        return subscription, res["total"], res["total_cost"], res["max_total_cost"]

    # https://dev.twitch.tv/docs/api/reference/#delete-eventsub-subscription
    def delete_eventsub_subscription(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-eventsub-subscriptions
    def get_eventsub_subscriptions(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-top-games
    def get_top_games(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-games
    def get_games(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-creator-goals
    def get_creator_goals(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-hype-train-events
    def get_hype_train_events(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#check-automod-status
    def check_automod_status(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#manage-held-automod-messages
    def manage_held_automod_messages(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-automod-settings
    def get_automod_settings(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-automod-settings
    def update_automod_settings(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-banned-users
    def get_banned_users(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#ban-user
    def ban_user(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#unban-user
    def unban_user(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-unban-requests
    def get_unban_requests(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#resolve-unban-requests
    def resolve_unban_requests(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-blocked-terms
    def get_blocked_terms(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#add-blocked-term
    def add_blocked_terms(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#remove-blocked-term
    def remove_blocked_term(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#delete-chat-messages
    def delete_chat_messages(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-moderated-channels
    def get_moderated_channels(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-moderators
    def get_moderators(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#add-channel-moderator
    def add_channel_moderator(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#remove-channel-moderator
    def remove_channel_moderator(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-vips
    def get_vips(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#add-channel-vip
    def add_channel_vip(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#remove-channel-vip
    def remove_channel_vip(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-shield-mode-status
    def update_shield_mode_status(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-shield-mode-status
    def get_shield_mode_status(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#warn-chat-user
    def warn_chat_user(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-polls
    def get_polls(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#create-poll
    def create_poll(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#end-poll
    def end_poll(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-predictions
    def get_predictions(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#create-prediction
    def create_prediction(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#end-prediction
    def end_prediction(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#start-a-raid
    def start_a_raid(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#cancel-a-raid
    def cancel_a_raid(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-channel-stream-schedule
    def get_channel_stream_schedule(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-channel-icalendar
    def get_channel_icalendar(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-channel-stream-schedule
    def update_channel_stream_schedule(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#create-channel-stream-schedule-segment
    def create_channel_stream_schedule_segment(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-channel-stream-schedule-segment
    def update_channel_stream_schedule_segment(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#delete-channel-stream-schedule-segment
    def delete_channel_stream_schedule_segment(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#search-categories
    def search_categories(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#search-channels
    def search_channels(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-stream-key
    def get_stream_key(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-streams
    def get_streams(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-followed-streams
    def get_followed_streams(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#create-stream-marker
    def create_stream_marker(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-stream-markers
    def get_stream_markers(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-broadcaster-subscriptions
    def get_broadcaster_subscriptions(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#check-user-subscription
    def check_user_subscription(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-all-stream-tags
    def get_all_stream_tags(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-stream-tags
    def get_stream_tags(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-channel-teams
    def get_channel_teams(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-teams
    def get_teams(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-users
    def get_users(self,
                  user_id: str | list[str] = None,
                  login: str | list[str] = None) -> User | tuple[User, ...] | None:
        url = self._url + "users"

        sum_of_lookups = 0

        if type(user_id) is list: sum_of_lookups += len(user_id)
        elif user_id: sum_of_lookups += 1

        if type(login) is list: sum_of_lookups += len(login)
        elif login: sum_of_lookups += 1

        # TODO: Remove check for user_id and login being mutually exclusive only if token is user access token
        validation = {
            (sum_of_lookups > 100): "Cannot look up for 100+ IDs and/or logins"
        }

        for condition, error in validation.items():
            if condition: raise ValueError(error)

        if user_id and login: parameters = {"id": user_id, "login": login}
        elif user_id: parameters = {"id": user_id}
        elif login: parameters = {"login": login}
        else: parameters = {}

        req = httpx.get(url, params=parameters, headers=self.__headers, timeout=self._timeout)
        req.raise_for_status()
        res = req.json()["data"]

        if len(res) < 1: return None

        users = list()
        for user in res:
            users.append(User(id=user["id"],
                              login=user["login"],
                              display_name=user["display_name"],
                              type=UserType(user["type"]),
                              broadcaster_type=BroadcasterType(user["broadcaster_type"]),
                              description=user["description"],
                              profile_image_url=user["profile_image_url"],
                              offline_image_url=user["offline_image_url"],
                              email=user["email"] if "email" in user else None,
                              created_at=int(parser.isoparse(user["created_at"]).timestamp())))

        if len(users) < 2: return users[0]

        return tuple(users)

    # https://dev.twitch.tv/docs/api/reference/#update-user
    def update_user(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-user-block-list
    def get_user_block_list(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#block-user
    def block_user(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#unblock-user
    def unblock_user(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-user-extensions
    def get_user_extensions(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-user-active-extensions
    def get_user_active_extensions(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#update-user-extensions
    def update_user_extensions(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#get-videos
    def get_videos(self,
                   video_id: str | list[str] = None,
                   user_id: str = None,
                   game_id: str = None,
                   language: str = None,
                   period: Literal["all", "day", "month", "week"] = None,
                   sort: Literal["time", "trending", "views"] = None,
                   video_type: Literal["all", "archive", "highlight", "upload"] = None,
                   first: int = None,
                   after: Pagination = None,
                   before: Pagination = None) -> Video | tuple[Video, ...] | tuple[tuple[Video, ...], Pagination] | None:
        url = self._url + "videos"

        validation = {
            (video_id is None and user_id is None and game_id is None): "Parameters video_id, user_id and game_id are mutually exclusive",
            (type(video_id) is list and len(video_id) > 100): "Cannot look up for 100+ IDs",
            (language and game_id is None): "If you supply language then you must also supply game_id",
            (period and (game_id is None and user_id is None)): "If you supply period then you must also supply game_id or user_id",
            (sort and (game_id is None and user_id is None)): "If you supply sort then you must also supply game_id or user_id",
            (video_type and (game_id is None and user_id is None)): "If you supply video_type then you must also supply game_id or user_id",
            (first and (game_id is None and user_id is None)): "If you supply first then you must also supply game_id or user_id",
            (after and user_id is None): "If you supply after then you must also supply a user_id",
            (before and user_id is None): "If you supply before then you must also supply user_id",
            (first and (first < 1 or first > 100)): "Parameter first must be between 1 and 100"
        }

        for condition, error in validation.items():
            if condition: raise ValueError(error)

        if video_id: parameters = {"id": video_id}
        elif user_id and game_id: parameters = {"user_id": user_id, "game_id": game_id}
        elif user_id: parameters = {"user_id": user_id}
        else: parameters = {"game_id": game_id}

        optional_params = {
            "language": language,
            "period": period,
            "sort": sort,
            "video_type": video_type,
            "first": first,
            "after": after.cursor if after else None,
            "before": before.cursor if before else None
        }

        for key, value in optional_params.items():
            if value: parameters[key] = value

        req = httpx.get(url, params=parameters, headers=self.__headers, timeout=self._timeout)

        if req.status_code == 404: return None

        req.raise_for_status()
        res = req.json()

        if len(res["data"]) < 1: return None

        videos = list()
        for video in res["data"]:
            muted_segments = list()
            if video["muted_segments"]:
                for segment in video["muted_segments"]:
                    muted_segments.append(MutedSegment(segment["duration"], segment["offset"]))
            videos.append(Video(id=video["id"],
                                stream_id=video["stream_id"],
                                user_id=video["user_id"],
                                user_login=video["user_login"],
                                user_name=video["user_name"],
                                title=video["title"],
                                description=video["description"],
                                created_at=int(parser.isoparse(video["created_at"]).timestamp()),
                                published_at=int(parser.isoparse(video["published_at"]).timestamp()),
                                url=video["url"],
                                thumbnail_url=video["thumbnail_url"],
                                viewable=video["viewable"],
                                view_count=video["view_count"],
                                language=video["language"],
                                type=VideoType(video["type"]),
                                duration=video["duration"],
                                muted_segments=tuple(muted_segments)))

        if len(videos) < 2: return videos[0]

        if len(res["pagination"]) > 0: return tuple(videos), Pagination(res["pagination"]["cursor"])

        return tuple(videos)

    # https://dev.twitch.tv/docs/api/reference/#delete-videos
    def delete_videos(self):
        pass

    # https://dev.twitch.tv/docs/api/reference/#send-whisper
    def send_whisper(self):
        pass
