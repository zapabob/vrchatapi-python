"""
    VRChat API Documentation

    ![VRChat API Banner](https://vrchatapi.github.io/assets/img/api_banner_1500x400.png)  # Welcome to the VRChat API  Before we begin, we would like to state this is a **COMMUNITY DRIVEN PROJECT**. This means that everything you read on here was written by the community itself and is **not** officially supported by VRChat. The documentation is provided \"AS IS\", and any action you take towards VRChat is completely your own responsibility.  The documentation and additional libraries SHALL ONLY be used for applications interacting with VRChat's API in accordance with their [Terms of Service](https://github.com/VRChatAPI), and MUST NOT be used for modifying the client, \"avatar ripping\", or other illegal activities. Malicious usage or spamming the API may result in account termination. Certain parts of the API are also more sensitive than others, for example moderation, so please tread extra carefully and read the warnings when present.  ![Tupper Policy on API](https://i.imgur.com/yLlW7Ok.png)  Finally, use of the API using applications other than the approved methods (website, VRChat application, Unity SDK) is not officially supported. VRChat provides no guarantee or support for external applications using the API. Access to API endpoints may break **at any time, without notice**. Therefore, please **do not ping** VRChat Staff in the VRChat Discord if you are having API problems, as they do not provide API support. We will make a best effort in keeping this documentation and associated language libraries up to date, but things might be outdated or missing. If you find that something is no longer valid, please contact us on Discord or [create an issue](https://github.com/vrchatapi/specification/issues) and tell us so we can fix it.  # Getting Started  The VRChat API can be used to programmatically retrieve or update information regarding your profile, friends, avatars, worlds and more. The API consists of two parts, \"Photon\" which is only used in-game, and the \"Web API\" which is used by both the game and the website. This documentation focuses only on the Web API.  The API is designed around the REST ideology, providing semi-simple and usually predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise.  <div class=\"callout callout-error\">   <strong>🛑 Warning! Do not touch Photon!</strong><br>   Photon is only used by the in-game client and should <b>not</b> be touched. Doing so may result in permanent account termination. </div>  <div class=\"callout callout-info\">   <strong>ℹ️ API Key and Authentication</strong><br>   The API Key has always been the same and is currently <code>JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26</code>.   Read <a href=\"#tag--authentication\">Authentication</a> for how to log in. </div>  # Using the API  For simply exploring what the API can do it is strongly recommended to download [Insomnia](https://insomnia.rest/download), a free and open-source API client that's great for sending requests to the API in an orderly fashion. Insomnia allows you to send data in the format that's required for VRChat's API. It is also possible to try out the API in your browser, by first logging in at [vrchat.com/home](https://vrchat.com/home/) and then going to [vrchat.com/api/1/auth/user](https://vrchat.com/api/1/auth/user), but the information will be much harder to work with.  For more permanent operation such as software development it is instead recommended to use one of the existing language SDKs. This community project maintains API libraries in several languages, which allows you to interact with the API with simple function calls rather than having to implement the HTTP protocol yourself. Most of these libraries are automatically generated from the API specification, sometimes with additional helpful wrapper code to make usage easier. This allows them to be almost automatically updated and expanded upon as soon as a new feature is introduced in the specification itself. The libraries can be found on [GitHub](https://github.com/vrchatapi) or following:  * [NodeJS (JavaScript)](https://www.npmjs.com/package/vrchat) * [Dart](https://pub.dev/packages/vrchat_dart) * [Rust](https://crates.io/crates/vrchatapi) * [C#](https://github.com/vrchatapi/vrchatapi-csharp) * [Python](https://github.com/vrchatapi/VRChatPython)  # Pagination  Most endpoints enforce pagination, meaning they will only return 10 entries by default, and never more than 100.<br> Using both the limit and offset parameters allows you to easily paginate through a large number of objects.  | Query Parameter | Type | Description | | ----------|--|------- | | `limit` | integer  | The number of objects to return. This value often defaults to 10. Highest limit is always 100.| | `offset` | integer  | A zero-based offset from the default object sorting.|  If a request returns fewer objects than the `limit` parameter, there are no more items available to return.  # Contribution  Do you want to get involved in the documentation effort? Do you want to help improve one of the language API libraries? This project is an [OPEN Open Source Project](https://openopensource.org)! This means that individuals making significant and valuable contributions are given commit-access to the project. It also means we are very open and welcoming of new people making contributions, unlike some more guarded open-source projects.  [![Discord](https://img.shields.io/static/v1?label=vrchatapi&message=discord&color=blueviolet&style=for-the-badge)](https://discord.gg/qjZE9C9fkB)  # noqa: E501

    The version of the OpenAPI document: 1.1.2
    Contact: me@ruby.js.org
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from vrchatapi.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from vrchatapi.exceptions import ApiAttributeError


def lazy_import():
    from vrchatapi.model.avatar_id import AvatarID
    from vrchatapi.model.config_announcements import ConfigAnnouncements
    from vrchatapi.model.config_download_urls import ConfigDownloadUrls
    from vrchatapi.model.config_dynamic_world_rows import ConfigDynamicWorldRows
    from vrchatapi.model.config_events import ConfigEvents
    from vrchatapi.model.deployment_group import DeploymentGroup
    from vrchatapi.model.world_id import WorldID
    globals()['AvatarID'] = AvatarID
    globals()['ConfigAnnouncements'] = ConfigAnnouncements
    globals()['ConfigDownloadUrls'] = ConfigDownloadUrls
    globals()['ConfigDynamicWorldRows'] = ConfigDynamicWorldRows
    globals()['ConfigEvents'] = ConfigEvents
    globals()['DeploymentGroup'] = DeploymentGroup
    globals()['WorldID'] = WorldID


class Config(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('address',): {
            'min_length': 1,
        },
        ('announcements',): {
            'min_items': 1,
        },
        ('api_key',): {
            'min_length': 1,
        },
        ('app_name',): {
            'min_length': 1,
        },
        ('build_version_tag',): {
            'min_length': 1,
        },
        ('client_api_key',): {
            'min_length': 1,
        },
        ('contact_email',): {
            'min_length': 1,
        },
        ('copyright_email',): {
            'min_length': 1,
        },
        ('dev_app_version_standalone',): {
            'min_length': 1,
        },
        ('dev_download_link_windows',): {
            'min_length': 1,
        },
        ('dev_sdk_url',): {
            'min_length': 1,
        },
        ('dev_sdk_version',): {
            'min_length': 1,
        },
        ('dev_server_version_standalone',): {
            'min_length': 1,
        },
        ('download_link_windows',): {
            'min_length': 1,
        },
        ('dynamic_world_rows',): {
            'min_items': 1,
        },
        ('gear_demo_room_id',): {
            'min_length': 1,
        },
        ('homepage_redirect_target',): {
            'min_length': 1,
        },
        ('jobs_email',): {
            'min_length': 1,
        },
        ('message_of_the_day',): {
            'min_length': 1,
        },
        ('moderation_email',): {
            'min_length': 1,
        },
        ('not_allowed_to_select_avatar_in_private_world_message',): {
            'min_length': 1,
        },
        ('plugin',): {
            'min_length': 1,
        },
        ('release_app_version_standalone',): {
            'min_length': 1,
        },
        ('release_sdk_url',): {
            'min_length': 1,
        },
        ('release_sdk_version',): {
            'min_length': 1,
        },
        ('release_server_version_standalone',): {
            'min_length': 1,
        },
        ('sdk_developer_faq_url',): {
            'min_length': 1,
        },
        ('sdk_discord_url',): {
            'min_length': 1,
        },
        ('sdk_not_allowed_to_publish_message',): {
            'min_length': 1,
        },
        ('sdk_unity_version',): {
            'min_length': 1,
        },
        ('server_name',): {
            'min_length': 1,
        },
        ('support_email',): {
            'min_length': 1,
        },
        ('vive_windows_url',): {
            'min_length': 1,
        },
        ('youtubedl_hash',): {
            'min_length': 1,
        },
        ('youtubedl_version',): {
            'min_length': 1,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'address': (str,),  # noqa: E501
            'announcements': ([ConfigAnnouncements],),  # noqa: E501
            'api_key': (str,),  # noqa: E501
            'app_name': (str,),  # noqa: E501
            'build_version_tag': (str,),  # noqa: E501
            'client_api_key': (str,),  # noqa: E501
            'contact_email': (str,),  # noqa: E501
            'copyright_email': (str,),  # noqa: E501
            'current_tos_version': (float,),  # noqa: E501
            'default_avatar': (AvatarID,),  # noqa: E501
            'deployment_group': (DeploymentGroup,),  # noqa: E501
            'dev_app_version_standalone': (str,),  # noqa: E501
            'dev_download_link_windows': (str,),  # noqa: E501
            'dev_sdk_url': (str,),  # noqa: E501
            'dev_sdk_version': (str,),  # noqa: E501
            'dev_server_version_standalone': (str,),  # noqa: E501
            'disable_avatar_copying': (bool,),  # noqa: E501
            'disable_avatar_gating': (bool,),  # noqa: E501
            'disable_community_labs': (bool,),  # noqa: E501
            'disable_community_labs_promotion': (bool,),  # noqa: E501
            'disable_event_stream': (bool,),  # noqa: E501
            'disable_feedback_gating': (bool,),  # noqa: E501
            'disable_registration': (bool,),  # noqa: E501
            'disable_steam_networking': (bool,),  # noqa: E501
            'disable_two_factor_auth': (bool,),  # noqa: E501
            'disable_udon': (bool,),  # noqa: E501
            'disable_upgrade_account': (bool,),  # noqa: E501
            'download_link_windows': (str,),  # noqa: E501
            'download_urls': (ConfigDownloadUrls,),  # noqa: E501
            'dynamic_world_rows': ([ConfigDynamicWorldRows],),  # noqa: E501
            'events': (ConfigEvents,),  # noqa: E501
            'gear_demo_room_id': (str,),  # noqa: E501
            'homepage_redirect_target': (str,),  # noqa: E501
            'home_world_id': (WorldID,),  # noqa: E501
            'hub_world_id': (WorldID,),  # noqa: E501
            'jobs_email': (str,),  # noqa: E501
            'message_of_the_day': (str,),  # noqa: E501
            'moderation_email': (str,),  # noqa: E501
            'moderation_query_period': (float,),  # noqa: E501
            'not_allowed_to_select_avatar_in_private_world_message': (str,),  # noqa: E501
            'plugin': (str,),  # noqa: E501
            'release_app_version_standalone': (str,),  # noqa: E501
            'release_sdk_url': (str,),  # noqa: E501
            'release_sdk_version': (str,),  # noqa: E501
            'release_server_version_standalone': (str,),  # noqa: E501
            'sdk_developer_faq_url': (str,),  # noqa: E501
            'sdk_discord_url': (str,),  # noqa: E501
            'sdk_not_allowed_to_publish_message': (str,),  # noqa: E501
            'sdk_unity_version': (str,),  # noqa: E501
            'server_name': (str,),  # noqa: E501
            'support_email': (str,),  # noqa: E501
            'time_out_world_id': (WorldID,),  # noqa: E501
            'tutorial_world_id': (WorldID,),  # noqa: E501
            'update_rate_ms_maximum': (float,),  # noqa: E501
            'update_rate_ms_minimum': (float,),  # noqa: E501
            'update_rate_ms_normal': (float,),  # noqa: E501
            'update_rate_ms_udon_manual': (float,),  # noqa: E501
            'upload_analysis_percent': (float,),  # noqa: E501
            'url_list': ([str],),  # noqa: E501
            'use_reliable_udp_for_voice': (bool,),  # noqa: E501
            'user_update_period': (float,),  # noqa: E501
            'user_verification_delay': (float,),  # noqa: E501
            'user_verification_retry': (float,),  # noqa: E501
            'user_verification_timeout': (float,),  # noqa: E501
            'vive_windows_url': (str,),  # noqa: E501
            'white_listed_asset_urls': ([str],),  # noqa: E501
            'world_update_period': (float,),  # noqa: E501
            'youtubedl_hash': (str,),  # noqa: E501
            'youtubedl_version': (str,),  # noqa: E501
            'client_bps_ceiling': (float,),  # noqa: E501
            'client_disconnect_timeout': (float,),  # noqa: E501
            'client_reserved_player_bps': (float,),  # noqa: E501
            'client_sent_count_allowance': (float,),  # noqa: E501
            'disable_email': (bool,),  # noqa: E501
            'disable_hello': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'address': 'address',  # noqa: E501
        'announcements': 'announcements',  # noqa: E501
        'api_key': 'apiKey',  # noqa: E501
        'app_name': 'appName',  # noqa: E501
        'build_version_tag': 'buildVersionTag',  # noqa: E501
        'client_api_key': 'clientApiKey',  # noqa: E501
        'contact_email': 'contactEmail',  # noqa: E501
        'copyright_email': 'copyrightEmail',  # noqa: E501
        'current_tos_version': 'currentTOSVersion',  # noqa: E501
        'default_avatar': 'defaultAvatar',  # noqa: E501
        'deployment_group': 'deploymentGroup',  # noqa: E501
        'dev_app_version_standalone': 'devAppVersionStandalone',  # noqa: E501
        'dev_download_link_windows': 'devDownloadLinkWindows',  # noqa: E501
        'dev_sdk_url': 'devSdkUrl',  # noqa: E501
        'dev_sdk_version': 'devSdkVersion',  # noqa: E501
        'dev_server_version_standalone': 'devServerVersionStandalone',  # noqa: E501
        'disable_avatar_copying': 'disableAvatarCopying',  # noqa: E501
        'disable_avatar_gating': 'disableAvatarGating',  # noqa: E501
        'disable_community_labs': 'disableCommunityLabs',  # noqa: E501
        'disable_community_labs_promotion': 'disableCommunityLabsPromotion',  # noqa: E501
        'disable_event_stream': 'disableEventStream',  # noqa: E501
        'disable_feedback_gating': 'disableFeedbackGating',  # noqa: E501
        'disable_registration': 'disableRegistration',  # noqa: E501
        'disable_steam_networking': 'disableSteamNetworking',  # noqa: E501
        'disable_two_factor_auth': 'disableTwoFactorAuth',  # noqa: E501
        'disable_udon': 'disableUdon',  # noqa: E501
        'disable_upgrade_account': 'disableUpgradeAccount',  # noqa: E501
        'download_link_windows': 'downloadLinkWindows',  # noqa: E501
        'download_urls': 'downloadUrls',  # noqa: E501
        'dynamic_world_rows': 'dynamicWorldRows',  # noqa: E501
        'events': 'events',  # noqa: E501
        'gear_demo_room_id': 'gearDemoRoomId',  # noqa: E501
        'homepage_redirect_target': 'homepageRedirectTarget',  # noqa: E501
        'home_world_id': 'homeWorldId',  # noqa: E501
        'hub_world_id': 'hubWorldId',  # noqa: E501
        'jobs_email': 'jobsEmail',  # noqa: E501
        'message_of_the_day': 'messageOfTheDay',  # noqa: E501
        'moderation_email': 'moderationEmail',  # noqa: E501
        'moderation_query_period': 'moderationQueryPeriod',  # noqa: E501
        'not_allowed_to_select_avatar_in_private_world_message': 'notAllowedToSelectAvatarInPrivateWorldMessage',  # noqa: E501
        'plugin': 'plugin',  # noqa: E501
        'release_app_version_standalone': 'releaseAppVersionStandalone',  # noqa: E501
        'release_sdk_url': 'releaseSdkUrl',  # noqa: E501
        'release_sdk_version': 'releaseSdkVersion',  # noqa: E501
        'release_server_version_standalone': 'releaseServerVersionStandalone',  # noqa: E501
        'sdk_developer_faq_url': 'sdkDeveloperFaqUrl',  # noqa: E501
        'sdk_discord_url': 'sdkDiscordUrl',  # noqa: E501
        'sdk_not_allowed_to_publish_message': 'sdkNotAllowedToPublishMessage',  # noqa: E501
        'sdk_unity_version': 'sdkUnityVersion',  # noqa: E501
        'server_name': 'serverName',  # noqa: E501
        'support_email': 'supportEmail',  # noqa: E501
        'time_out_world_id': 'timeOutWorldId',  # noqa: E501
        'tutorial_world_id': 'tutorialWorldId',  # noqa: E501
        'update_rate_ms_maximum': 'updateRateMsMaximum',  # noqa: E501
        'update_rate_ms_minimum': 'updateRateMsMinimum',  # noqa: E501
        'update_rate_ms_normal': 'updateRateMsNormal',  # noqa: E501
        'update_rate_ms_udon_manual': 'updateRateMsUdonManual',  # noqa: E501
        'upload_analysis_percent': 'uploadAnalysisPercent',  # noqa: E501
        'url_list': 'urlList',  # noqa: E501
        'use_reliable_udp_for_voice': 'useReliableUdpForVoice',  # noqa: E501
        'user_update_period': 'userUpdatePeriod',  # noqa: E501
        'user_verification_delay': 'userVerificationDelay',  # noqa: E501
        'user_verification_retry': 'userVerificationRetry',  # noqa: E501
        'user_verification_timeout': 'userVerificationTimeout',  # noqa: E501
        'vive_windows_url': 'viveWindowsUrl',  # noqa: E501
        'white_listed_asset_urls': 'whiteListedAssetUrls',  # noqa: E501
        'world_update_period': 'worldUpdatePeriod',  # noqa: E501
        'youtubedl_hash': 'youtubedl-hash',  # noqa: E501
        'youtubedl_version': 'youtubedl-version',  # noqa: E501
        'client_bps_ceiling': 'clientBPSCeiling',  # noqa: E501
        'client_disconnect_timeout': 'clientDisconnectTimeout',  # noqa: E501
        'client_reserved_player_bps': 'clientReservedPlayerBPS',  # noqa: E501
        'client_sent_count_allowance': 'clientSentCountAllowance',  # noqa: E501
        'disable_email': 'disableEmail',  # noqa: E501
        'disable_hello': 'disableHello',  # noqa: E501
    }

    read_only_vars = {
        'address',  # noqa: E501
        'announcements',  # noqa: E501
        'api_key',  # noqa: E501
        'app_name',  # noqa: E501
        'build_version_tag',  # noqa: E501
        'client_api_key',  # noqa: E501
        'contact_email',  # noqa: E501
        'copyright_email',  # noqa: E501
        'current_tos_version',  # noqa: E501
        'dev_app_version_standalone',  # noqa: E501
        'dev_download_link_windows',  # noqa: E501
        'dev_sdk_url',  # noqa: E501
        'dev_sdk_version',  # noqa: E501
        'dev_server_version_standalone',  # noqa: E501
        'download_link_windows',  # noqa: E501
        'dynamic_world_rows',  # noqa: E501
        'gear_demo_room_id',  # noqa: E501
        'homepage_redirect_target',  # noqa: E501
        'jobs_email',  # noqa: E501
        'message_of_the_day',  # noqa: E501
        'moderation_email',  # noqa: E501
        'not_allowed_to_select_avatar_in_private_world_message',  # noqa: E501
        'plugin',  # noqa: E501
        'release_app_version_standalone',  # noqa: E501
        'release_sdk_url',  # noqa: E501
        'release_sdk_version',  # noqa: E501
        'release_server_version_standalone',  # noqa: E501
        'sdk_developer_faq_url',  # noqa: E501
        'sdk_discord_url',  # noqa: E501
        'sdk_not_allowed_to_publish_message',  # noqa: E501
        'sdk_unity_version',  # noqa: E501
        'server_name',  # noqa: E501
        'support_email',  # noqa: E501
        'update_rate_ms_maximum',  # noqa: E501
        'update_rate_ms_minimum',  # noqa: E501
        'update_rate_ms_normal',  # noqa: E501
        'update_rate_ms_udon_manual',  # noqa: E501
        'upload_analysis_percent',  # noqa: E501
        'url_list',  # noqa: E501
        'user_update_period',  # noqa: E501
        'user_verification_delay',  # noqa: E501
        'user_verification_retry',  # noqa: E501
        'user_verification_timeout',  # noqa: E501
        'vive_windows_url',  # noqa: E501
        'white_listed_asset_urls',  # noqa: E501
        'world_update_period',  # noqa: E501
        'youtubedl_hash',  # noqa: E501
        'youtubedl_version',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, address, announcements, api_key, build_version_tag, client_api_key, contact_email, copyright_email, current_tos_version, default_avatar, deployment_group, dev_app_version_standalone, dev_download_link_windows, dev_sdk_url, dev_sdk_version, dev_server_version_standalone, download_link_windows, download_urls, dynamic_world_rows, events, gear_demo_room_id, home_world_id, hub_world_id, jobs_email, message_of_the_day, moderation_email, moderation_query_period, not_allowed_to_select_avatar_in_private_world_message, plugin, release_app_version_standalone, release_sdk_url, release_sdk_version, release_server_version_standalone, sdk_developer_faq_url, sdk_discord_url, sdk_not_allowed_to_publish_message, sdk_unity_version, server_name, support_email, time_out_world_id, tutorial_world_id, update_rate_ms_maximum, update_rate_ms_minimum, update_rate_ms_normal, update_rate_ms_udon_manual, upload_analysis_percent, url_list, user_update_period, user_verification_delay, user_verification_retry, user_verification_timeout, vive_windows_url, white_listed_asset_urls, world_update_period, youtubedl_hash, youtubedl_version, *args, **kwargs):  # noqa: E501
        """Config - a model defined in OpenAPI

        Args:
            address (str): VRChat's office address
            announcements ([ConfigAnnouncements]): Public Announcements
            api_key (str): apiKey to be used for all other requests
            build_version_tag (str): Build tag of the API server
            client_api_key (str): apiKey to be used for all other requests
            contact_email (str): VRChat's contact email
            copyright_email (str): VRChat's copyright-issues-related email
            current_tos_version (float): Current version number of the Terms of Service
            default_avatar (AvatarID):
            deployment_group (DeploymentGroup):
            dev_app_version_standalone (str): Version number for game development build
            dev_download_link_windows (str): Developer Download link
            dev_sdk_url (str): Link to download the development SDK, use downloadUrls instead
            dev_sdk_version (str): Version of the development SDK
            dev_server_version_standalone (str): Version number for server development build
            download_link_windows (str): Download link for game on the Oculus Rift website.
            download_urls (ConfigDownloadUrls):
            dynamic_world_rows ([ConfigDynamicWorldRows]): Array of DynamicWorldRow objects, used by the game to display the list of world rows
            events (ConfigEvents):
            gear_demo_room_id (str): Unknown
            home_world_id (WorldID):
            hub_world_id (WorldID):
            jobs_email (str): VRChat's job application email
            message_of_the_day (str): MOTD
            moderation_email (str): VRChat's moderation related email
            moderation_query_period (float): Unknown
            not_allowed_to_select_avatar_in_private_world_message (str): Used in-game to notify a user they aren't allowed to select avatars in private worlds
            plugin (str): Extra [plugin](https://doc.photonengine.com/en-us/server/current/plugins/manual) to run in each instance
            release_app_version_standalone (str): Version number for game release build
            release_sdk_url (str): Link to download the release SDK
            release_sdk_version (str): Version of the release SDK
            release_server_version_standalone (str): Version number for server release build
            sdk_developer_faq_url (str): Link to the developer FAQ
            sdk_discord_url (str): Link to the official VRChat Discord
            sdk_not_allowed_to_publish_message (str): Used in the SDK to notify a user they aren't allowed to upload avatars/worlds yet
            sdk_unity_version (str): Unity version supported by the SDK
            server_name (str): Server name of the API server currently responding
            support_email (str): VRChat's support email
            time_out_world_id (WorldID):
            tutorial_world_id (WorldID):
            update_rate_ms_maximum (float): Unknown
            update_rate_ms_minimum (float): Unknown
            update_rate_ms_normal (float): Unknown
            update_rate_ms_udon_manual (float): Unknown
            upload_analysis_percent (float): Unknown
            url_list ([str]): List of allowed URLs that bypass the \"Allow untrusted URL's\" setting in-game
            user_update_period (float): Unknown
            user_verification_delay (float): Unknown
            user_verification_retry (float): Unknown
            user_verification_timeout (float): Unknown
            vive_windows_url (str): Download link for game on the Steam website.
            white_listed_asset_urls ([str]): List of allowed URLs that are allowed to host avatar assets
            world_update_period (float): Unknown
            youtubedl_hash (str): Currently used youtube-dl.exe hash in SHA-256-delimited format
            youtubedl_version (str): Currently used youtube-dl.exe version

        Keyword Args:
            app_name (str): Game name. defaults to "VrChat"  # noqa: E501
            disable_avatar_copying (bool): Toggles if copying avatars should be disabled. defaults to False  # noqa: E501
            disable_avatar_gating (bool): Toggles if avatar gating should be disabled. Avatar gating restricts uploading of avatars to people with the `system_avatar_access` Tag or `admin_avatar_access` Tag. defaults to False  # noqa: E501
            disable_community_labs (bool): Toggles if the Community Labs should be disabled. defaults to False  # noqa: E501
            disable_community_labs_promotion (bool): Toggles if promotion out of Community Labs should be disabled. defaults to False  # noqa: E501
            disable_event_stream (bool): Toggles if Analytics should be disabled (this sreportedly not used in the Client). defaults to False  # noqa: E501
            disable_feedback_gating (bool): Toggles if feedback gating should be disabled. Feedback gating restricts submission of feedback (reporting a World or User) to people with the `system_feedback_access` Tag.. defaults to False  # noqa: E501
            disable_registration (bool): Toggles if new user account registration should be disabled. defaults to False  # noqa: E501
            disable_steam_networking (bool): Toggles if Steam Networking should be disabled. VRChat these days uses Photon Unity Networking (PUN) instead.. defaults to True  # noqa: E501
            disable_two_factor_auth (bool): Toggles if 2FA should be disabled.. defaults to False  # noqa: E501
            disable_udon (bool): Toggles if Udon should be universally disabled in-game.. defaults to False  # noqa: E501
            disable_upgrade_account (bool): Toggles if account upgrading \"linking with Steam/Oculus\" should be disabled.. defaults to False  # noqa: E501
            homepage_redirect_target (str): Redirect target if you try to open the base API domain in your browser. defaults to "https://hello.vrchat.com"  # noqa: E501
            use_reliable_udp_for_voice (bool): Unknown. defaults to False  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            client_bps_ceiling (float): Unknown. [optional]  # noqa: E501
            client_disconnect_timeout (float): Unknown. [optional]  # noqa: E501
            client_reserved_player_bps (float): Unknown. [optional]  # noqa: E501
            client_sent_count_allowance (float): Unknown. [optional]  # noqa: E501
            disable_email (bool): Unknown. [optional] if omitted the server will use the default value of False  # noqa: E501
            disable_hello (bool): Unknown. [optional] if omitted the server will use the default value of False  # noqa: E501
        """

        app_name = kwargs.get('app_name', "VrChat")
        disable_avatar_copying = kwargs.get('disable_avatar_copying', False)
        disable_avatar_gating = kwargs.get('disable_avatar_gating', False)
        disable_community_labs = kwargs.get('disable_community_labs', False)
        disable_community_labs_promotion = kwargs.get('disable_community_labs_promotion', False)
        disable_event_stream = kwargs.get('disable_event_stream', False)
        disable_feedback_gating = kwargs.get('disable_feedback_gating', False)
        disable_registration = kwargs.get('disable_registration', False)
        disable_steam_networking = kwargs.get('disable_steam_networking', True)
        disable_two_factor_auth = kwargs.get('disable_two_factor_auth', False)
        disable_udon = kwargs.get('disable_udon', False)
        disable_upgrade_account = kwargs.get('disable_upgrade_account', False)
        homepage_redirect_target = kwargs.get('homepage_redirect_target', "https://hello.vrchat.com")
        use_reliable_udp_for_voice = kwargs.get('use_reliable_udp_for_voice', False)
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.address = address
        self.announcements = announcements
        self.api_key = api_key
        self.app_name = app_name
        self.build_version_tag = build_version_tag
        self.client_api_key = client_api_key
        self.contact_email = contact_email
        self.copyright_email = copyright_email
        self.current_tos_version = current_tos_version
        self.default_avatar = default_avatar
        self.deployment_group = deployment_group
        self.dev_app_version_standalone = dev_app_version_standalone
        self.dev_download_link_windows = dev_download_link_windows
        self.dev_sdk_url = dev_sdk_url
        self.dev_sdk_version = dev_sdk_version
        self.dev_server_version_standalone = dev_server_version_standalone
        self.disable_avatar_copying = disable_avatar_copying
        self.disable_avatar_gating = disable_avatar_gating
        self.disable_community_labs = disable_community_labs
        self.disable_community_labs_promotion = disable_community_labs_promotion
        self.disable_event_stream = disable_event_stream
        self.disable_feedback_gating = disable_feedback_gating
        self.disable_registration = disable_registration
        self.disable_steam_networking = disable_steam_networking
        self.disable_two_factor_auth = disable_two_factor_auth
        self.disable_udon = disable_udon
        self.disable_upgrade_account = disable_upgrade_account
        self.download_link_windows = download_link_windows
        self.download_urls = download_urls
        self.dynamic_world_rows = dynamic_world_rows
        self.events = events
        self.gear_demo_room_id = gear_demo_room_id
        self.homepage_redirect_target = homepage_redirect_target
        self.home_world_id = home_world_id
        self.hub_world_id = hub_world_id
        self.jobs_email = jobs_email
        self.message_of_the_day = message_of_the_day
        self.moderation_email = moderation_email
        self.moderation_query_period = moderation_query_period
        self.not_allowed_to_select_avatar_in_private_world_message = not_allowed_to_select_avatar_in_private_world_message
        self.plugin = plugin
        self.release_app_version_standalone = release_app_version_standalone
        self.release_sdk_url = release_sdk_url
        self.release_sdk_version = release_sdk_version
        self.release_server_version_standalone = release_server_version_standalone
        self.sdk_developer_faq_url = sdk_developer_faq_url
        self.sdk_discord_url = sdk_discord_url
        self.sdk_not_allowed_to_publish_message = sdk_not_allowed_to_publish_message
        self.sdk_unity_version = sdk_unity_version
        self.server_name = server_name
        self.support_email = support_email
        self.time_out_world_id = time_out_world_id
        self.tutorial_world_id = tutorial_world_id
        self.update_rate_ms_maximum = update_rate_ms_maximum
        self.update_rate_ms_minimum = update_rate_ms_minimum
        self.update_rate_ms_normal = update_rate_ms_normal
        self.update_rate_ms_udon_manual = update_rate_ms_udon_manual
        self.upload_analysis_percent = upload_analysis_percent
        self.url_list = url_list
        self.use_reliable_udp_for_voice = use_reliable_udp_for_voice
        self.user_update_period = user_update_period
        self.user_verification_delay = user_verification_delay
        self.user_verification_retry = user_verification_retry
        self.user_verification_timeout = user_verification_timeout
        self.vive_windows_url = vive_windows_url
        self.white_listed_asset_urls = white_listed_asset_urls
        self.world_update_period = world_update_period
        self.youtubedl_hash = youtubedl_hash
        self.youtubedl_version = youtubedl_version
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, default_avatar, deployment_group, download_urls, events, home_world_id, hub_world_id, moderation_query_period, time_out_world_id, tutorial_world_id, *args, **kwargs):  # noqa: E501
        """Config - a model defined in OpenAPI

            default_avatar (AvatarID):
            deployment_group (DeploymentGroup):
            download_urls (ConfigDownloadUrls):
            events (ConfigEvents):
            home_world_id (WorldID):
            hub_world_id (WorldID):
            moderation_query_period (float): Unknown
            time_out_world_id (WorldID):
            tutorial_world_id (WorldID):
        Keyword Args:
            disable_avatar_copying (bool): Toggles if copying avatars should be disabled. defaults to False  # noqa: E501
            disable_avatar_gating (bool): Toggles if avatar gating should be disabled. Avatar gating restricts uploading of avatars to people with the `system_avatar_access` Tag or `admin_avatar_access` Tag. defaults to False  # noqa: E501
            disable_community_labs (bool): Toggles if the Community Labs should be disabled. defaults to False  # noqa: E501
            disable_community_labs_promotion (bool): Toggles if promotion out of Community Labs should be disabled. defaults to False  # noqa: E501
            disable_event_stream (bool): Toggles if Analytics should be disabled (this sreportedly not used in the Client). defaults to False  # noqa: E501
            disable_feedback_gating (bool): Toggles if feedback gating should be disabled. Feedback gating restricts submission of feedback (reporting a World or User) to people with the `system_feedback_access` Tag.. defaults to False  # noqa: E501
            disable_registration (bool): Toggles if new user account registration should be disabled. defaults to False  # noqa: E501
            disable_steam_networking (bool): Toggles if Steam Networking should be disabled. VRChat these days uses Photon Unity Networking (PUN) instead.. defaults to True  # noqa: E501
            disable_two_factor_auth (bool): Toggles if 2FA should be disabled.. defaults to False  # noqa: E501
            disable_udon (bool): Toggles if Udon should be universally disabled in-game.. defaults to False  # noqa: E501
            disable_upgrade_account (bool): Toggles if account upgrading \"linking with Steam/Oculus\" should be disabled.. defaults to False  # noqa: E501
            use_reliable_udp_for_voice (bool): Unknown. defaults to False  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            client_bps_ceiling (float): Unknown. [optional]  # noqa: E501
            client_disconnect_timeout (float): Unknown. [optional]  # noqa: E501
            client_reserved_player_bps (float): Unknown. [optional]  # noqa: E501
            client_sent_count_allowance (float): Unknown. [optional]  # noqa: E501
            disable_email (bool): Unknown. [optional] if omitted the server will use the default value of False  # noqa: E501
            disable_hello (bool): Unknown. [optional] if omitted the server will use the default value of False  # noqa: E501
        """

        disable_avatar_copying = kwargs.get('disable_avatar_copying', False)
        disable_avatar_gating = kwargs.get('disable_avatar_gating', False)
        disable_community_labs = kwargs.get('disable_community_labs', False)
        disable_community_labs_promotion = kwargs.get('disable_community_labs_promotion', False)
        disable_event_stream = kwargs.get('disable_event_stream', False)
        disable_feedback_gating = kwargs.get('disable_feedback_gating', False)
        disable_registration = kwargs.get('disable_registration', False)
        disable_steam_networking = kwargs.get('disable_steam_networking', True)
        disable_two_factor_auth = kwargs.get('disable_two_factor_auth', False)
        disable_udon = kwargs.get('disable_udon', False)
        disable_upgrade_account = kwargs.get('disable_upgrade_account', False)
        use_reliable_udp_for_voice = kwargs.get('use_reliable_udp_for_voice', False)
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.default_avatar = default_avatar
        self.deployment_group = deployment_group
        self.disable_avatar_copying = disable_avatar_copying
        self.disable_avatar_gating = disable_avatar_gating
        self.disable_community_labs = disable_community_labs
        self.disable_community_labs_promotion = disable_community_labs_promotion
        self.disable_event_stream = disable_event_stream
        self.disable_feedback_gating = disable_feedback_gating
        self.disable_registration = disable_registration
        self.disable_steam_networking = disable_steam_networking
        self.disable_two_factor_auth = disable_two_factor_auth
        self.disable_udon = disable_udon
        self.disable_upgrade_account = disable_upgrade_account
        self.download_urls = download_urls
        self.events = events
        self.home_world_id = home_world_id
        self.hub_world_id = hub_world_id
        self.moderation_query_period = moderation_query_period
        self.time_out_world_id = time_out_world_id
        self.tutorial_world_id = tutorial_world_id
        self.use_reliable_udp_for_voice = use_reliable_udp_for_voice
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
