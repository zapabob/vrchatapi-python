# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from vrchatapi.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from vrchatapi.model.api_config import APIConfig
from vrchatapi.model.api_event_config import APIEventConfig
from vrchatapi.model.api_health import APIHealth
from vrchatapi.model.add_favorite_request import AddFavoriteRequest
from vrchatapi.model.avatar import Avatar
from vrchatapi.model.avatar_id import AvatarID
from vrchatapi.model.avatar_unity_package_url_object import AvatarUnityPackageUrlObject
from vrchatapi.model.create_avatar_request import CreateAvatarRequest
from vrchatapi.model.create_file_request import CreateFileRequest
from vrchatapi.model.create_file_version_request import CreateFileVersionRequest
from vrchatapi.model.create_world_request import CreateWorldRequest
from vrchatapi.model.current_user import CurrentUser
from vrchatapi.model.deployment_group import DeploymentGroup
from vrchatapi.model.developer_type import DeveloperType
from vrchatapi.model.download_url_list import DownloadURLList
from vrchatapi.model.dynamic_content_row import DynamicContentRow
from vrchatapi.model.error import Error
from vrchatapi.model.favorite import Favorite
from vrchatapi.model.favorite_group import FavoriteGroup
from vrchatapi.model.favorite_group_id import FavoriteGroupID
from vrchatapi.model.favorite_group_visibility import FavoriteGroupVisibility
from vrchatapi.model.favorite_id import FavoriteID
from vrchatapi.model.favorite_type import FavoriteType
from vrchatapi.model.file import File
from vrchatapi.model.file_data import FileData
from vrchatapi.model.file_id import FileID
from vrchatapi.model.file_status import FileStatus
from vrchatapi.model.file_upload_url import FileUploadURL
from vrchatapi.model.file_version import FileVersion
from vrchatapi.model.file_version_upload_status import FileVersionUploadStatus
from vrchatapi.model.finish_file_data_upload_request import FinishFileDataUploadRequest
from vrchatapi.model.friend_status import FriendStatus
from vrchatapi.model.info_push import InfoPush
from vrchatapi.model.info_push_data import InfoPushData
from vrchatapi.model.info_push_data_article import InfoPushDataArticle
from vrchatapi.model.info_push_data_article_content import InfoPushDataArticleContent
from vrchatapi.model.info_push_data_clickable import InfoPushDataClickable
from vrchatapi.model.instance import Instance
from vrchatapi.model.instance_id import InstanceID
from vrchatapi.model.instance_platforms import InstancePlatforms
from vrchatapi.model.instance_type import InstanceType
from vrchatapi.model.invite_message import InviteMessage
from vrchatapi.model.invite_message_id import InviteMessageID
from vrchatapi.model.invite_message_type import InviteMessageType
from vrchatapi.model.invite_request import InviteRequest
from vrchatapi.model.invite_response import InviteResponse
from vrchatapi.model.license import License
from vrchatapi.model.license_action import LicenseAction
from vrchatapi.model.license_group import LicenseGroup
from vrchatapi.model.license_group_id import LicenseGroupID
from vrchatapi.model.license_type import LicenseType
from vrchatapi.model.limited_unity_package import LimitedUnityPackage
from vrchatapi.model.limited_user import LimitedUser
from vrchatapi.model.limited_world import LimitedWorld
from vrchatapi.model.mime_type import MIMEType
from vrchatapi.model.moderate_user_request import ModerateUserRequest
from vrchatapi.model.notification import Notification
from vrchatapi.model.notification_type import NotificationType
from vrchatapi.model.past_display_name import PastDisplayName
from vrchatapi.model.permission import Permission
from vrchatapi.model.permission_id import PermissionID
from vrchatapi.model.player_moderation import PlayerModeration
from vrchatapi.model.player_moderation_id import PlayerModerationID
from vrchatapi.model.player_moderation_type import PlayerModerationType
from vrchatapi.model.public_announcement import PublicAnnouncement
from vrchatapi.model.region import Region
from vrchatapi.model.release_status import ReleaseStatus
from vrchatapi.model.response import Response
from vrchatapi.model.subscription import Subscription
from vrchatapi.model.subscription_period import SubscriptionPeriod
from vrchatapi.model.success import Success
from vrchatapi.model.tag import Tag
from vrchatapi.model.transaction import Transaction
from vrchatapi.model.transaction_agreement import TransactionAgreement
from vrchatapi.model.transaction_id import TransactionID
from vrchatapi.model.transaction_status import TransactionStatus
from vrchatapi.model.transaction_steam_info import TransactionSteamInfo
from vrchatapi.model.transaction_steam_wallet_info import TransactionSteamWalletInfo
from vrchatapi.model.two_factor_auth_code import TwoFactorAuthCode
from vrchatapi.model.unity_package import UnityPackage
from vrchatapi.model.unity_package_id import UnityPackageID
from vrchatapi.model.update_avatar_request import UpdateAvatarRequest
from vrchatapi.model.update_favorite_group_request import UpdateFavoriteGroupRequest
from vrchatapi.model.update_invite_message_request import UpdateInviteMessageRequest
from vrchatapi.model.update_user_request import UpdateUserRequest
from vrchatapi.model.update_world_request import UpdateWorldRequest
from vrchatapi.model.user import User
from vrchatapi.model.user_exists import UserExists
from vrchatapi.model.user_state import UserState
from vrchatapi.model.user_status import UserStatus
from vrchatapi.model.user_subscription import UserSubscription
from vrchatapi.model.verify2_fa_result import Verify2FAResult
from vrchatapi.model.verify_auth_token_result import VerifyAuthTokenResult
from vrchatapi.model.world import World
from vrchatapi.model.world_id import WorldID
from vrchatapi.model.world_metadata import WorldMetadata
from vrchatapi.model.world_publish_status import WorldPublishStatus
