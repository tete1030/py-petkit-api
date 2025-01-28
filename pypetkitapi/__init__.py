"""Pypetkit: A Python library for interfacing with PetKit"""

from .client import PetKitClient
from .command import (
    DeviceAction,
    DeviceCommand,
    FeederCommand,
    LBCommand,
    LitterCommand,
    PetCommand,
    PurMode,
)
from .const import (
    CTW3,
    D3,
    D4,
    D4H,
    D4S,
    D4SH,
    DEVICES_FEEDER,
    DEVICES_LITTER_BOX,
    DEVICES_PURIFIER,
    DEVICES_WATER_FOUNTAIN,
    FEEDER,
    FEEDER_MINI,
    FEEDER_WITH_CAMERA,
    K2,
    K3,
    LITTER_NO_CAMERA,
    LITTER_WITH_CAMERA,
    T3,
    T4,
    T5,
    T6,
    W5,
    MediaType,
    RecordType,
)
from .containers import Pet
from .exceptions import (
    PetkitAuthenticationUnregisteredEmailError,
    PetkitRegionalServerNotFoundError,
    PetkitSessionError,
    PetkitSessionExpiredError,
    PetkitTimeoutError,
    PypetkitError,
)
from .feeder_container import Feeder, RecordsItems
from .litter_container import Litter, LitterRecord, WorkState
from .media import DownloadDecryptMedia, MediaCloud, MediaFile, MediaManager
from .purifier_container import Purifier
from .water_fountain_container import WaterFountain

__version__ = "1.11.3"

__all__ = [
    "CTW3",
    "D3",
    "D4",
    "D4H",
    "D4S",
    "D4SH",
    "DEVICES_FEEDER",
    "DEVICES_LITTER_BOX",
    "DEVICES_PURIFIER",
    "DEVICES_WATER_FOUNTAIN",
    "FEEDER_WITH_CAMERA",
    "LITTER_WITH_CAMERA",
    "LITTER_NO_CAMERA",
    "DeviceAction",
    "DeviceCommand",
    "FEEDER",
    "FEEDER_MINI",
    "Feeder",
    "FeederCommand",
    "K2",
    "K3",
    "LBCommand",
    "Litter",
    "LitterCommand",
    "LitterRecord",
    "MediaManager",
    "DownloadDecryptMedia",
    "MediaCloud",
    "MediaFile",
    "MediaType",
    "Pet",
    "PetCommand",
    "PetKitClient",
    "PetkitAuthenticationUnregisteredEmailError",
    "PetkitRegionalServerNotFoundError",
    "PetkitSessionError",
    "PetkitSessionExpiredError",
    "PetkitTimeoutError",
    "PurMode",
    "Purifier",
    "PypetkitError",
    "RecordType",
    "RecordsItems",
    "T3",
    "T4",
    "T5",
    "T6",
    "W5",
    "WaterFountain",
    "WorkState",
]
