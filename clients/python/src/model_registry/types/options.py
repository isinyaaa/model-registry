"""Options for listing objects.

Provides a thin wrappers around the options classes defined in the MLMD Py lib.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic

from kiota_abstractions.base_request_configuration import (
    QueryParameters,
    RequestConfiguration,
)
from kiota_abstractions.headers_collection import HeadersCollection

from ..models.order_by_field import OrderByField
from ..models.sort_order import SortOrder
from .base import BaseOptions


@dataclass
class ListOptions(BaseOptions):
    """Options for listing objects.

    Attributes:
        next_page_token: Token to use to retrieve next page of results.
        order_by: Field to order by.
        page_size: Number of entities in each page.
        sort_order: Sort order. Defaults to ASC.
    """

    next_page_token: str | None = None
    order_by: OrderByField | None = None
    page_size: str | None = None
    sort_order: SortOrder | None = None


@dataclass
class FindOptions(BaseOptions):
    """Options for finding an object.

    Attributes:
        external_id: External ID of entity to search.
        name: Name of entity to search.
        parent_resource_id: ID of the parent resource to use for search.
    """

    external_id: str | None = None
    name: str | None = None
    parent_resource_id: str | None = None


@dataclass
class RequestOptions(RequestConfiguration, Generic[QueryParameters]):
    """Options for making requests."""

    query_parameters: QueryParameters | None = None
    headers: HeadersCollection = HeadersCollection()

    def __post_init__(self):
        self.headers.add("Content-Type", "application/json")
        self.headers.add("accept", "application/json")
