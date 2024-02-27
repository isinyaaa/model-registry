from enum import Enum

class ExecutionState(str, Enum):
    UNKNOWN = "UNKNOWN",
    NEW = "NEW",
    RUNNING = "RUNNING",
    COMPLETE = "COMPLETE",
    FAILED = "FAILED",
    CACHED = "CACHED",
    CANCELED = "CANCELED",

