"""Constants for the pypetkit library."""

from enum import StrEnum

MIN_FEED_AMOUNT = 0
MAX_FEED_AMOUNT = 10
TOKEN_EXPIRATION_TIME = 3600
BLE_POLL_INTERVAL = 420
BLE_CONNECT_ATTEMPT = 4

RESULT_KEY = "result"
ERROR_KEY = "error"

# PetKit Models
D4H = "d4h"
D4SH = "d4sh"
T4 = "t4"
T5 = "t5"
T6 = "t6"
W5 = "w5"
CTW3 = "ctw3"


LITTER_BOX = [T4, T5, T6]
FEEDER = [D4H, D4SH]
WATER_FOUNTAIN = [W5, CTW3]


class PetkitURL(StrEnum):
    """Petkit URL constants"""

    REGION_SRV = "https://passport.petkt.com/v1/regionservers"


class Client(StrEnum):
    """Platform constants"""

    PLATFORM_TYPE = "android"
    OS_VERSION = "15.1"
    MODEL_NAME = "23127PN0CG"
    SOURCE = "app.petkit-android"


class Header(StrEnum):
    """Header constants"""

    ACCEPT = "*/*"
    ACCEPT_LANG = "en-US;q=1, it-US;q=0.9"
    ENCODING = "gzip, deflate"
    API_VERSION = "11.3.1"
    CONTENT_TYPE = "application/x-www-form-urlencoded"
    AGENT = "okhttp/3.12.11"
    CLIENT = f"{Client.PLATFORM_TYPE}({Client.OS_VERSION};{Client.MODEL_NAME})"
    TIMEZONE = "1.0"
    TIMEZONE_ID = "Europe/Paris"
    LOCALE = "en-US"
    IMG_VERSION = "1.0"
    HOUR = "24"


CLIENT_NFO = {
    "locale": Header.LOCALE.value,
    "name": Client.MODEL_NAME.value,
    "osVersion": Client.OS_VERSION.value,
    "platform": Client.PLATFORM_TYPE.value,
    "source": Client.SOURCE.value,
    "timezone": Header.TIMEZONE.value,
    "timezoneId": Header.TIMEZONE_ID.value,
    "version": Header.API_VERSION.value,
}


class PetkitEndpoint(StrEnum):
    """Petkit Endpoint constants"""

    LOGIN = "user/login"
    FAMILY_LIST = "group/family/list"
    REFRESH_HOME_V2 = "refreshHomeV2"
    DEVICE_DETAIL = "device_detail"
    DEVICE_DATA = "deviceData"
    GET_DEVICE_RECORD = "getDeviceRecord"
    GET_DEVICE_RECORD_RELEASE = "getDeviceRecordRelease"
    UPDATE_SETTING = "updateSettings"
