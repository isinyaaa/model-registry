from enum import Enum

class RegisteredModelState(str, Enum):
    LIVE = "LIVE",
    ARCHIVED = "ARCHIVED",

