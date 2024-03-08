from enum import Enum


class OrderByField(str, Enum):
    CREATE_TIME = "CREATE_TIME",
    LAST_UPDATE_TIME = "LAST_UPDATE_TIME",
    Id = "Id",

