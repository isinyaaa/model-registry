from enum import Enum

class ModelVersionState(str, Enum):
    LIVE = "LIVE",
    ARCHIVED = "ARCHIVED",

