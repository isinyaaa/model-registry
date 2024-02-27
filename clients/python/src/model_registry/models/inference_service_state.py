from enum import Enum

class InferenceServiceState(str, Enum):
    DEPLOYED = "DEPLOYED",
    UNDEPLOYED = "UNDEPLOYED",

