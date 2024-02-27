"""Base types for model registry."""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import TypeVar

from attrs import define, field
from kiota_abstractions.serialization import Parsable

logger = logging.getLogger(__name__)

Resource = TypeVar("Resource", bound="BaseResourceModel")


@define(slots=False, init=False)
class BaseResourceModel(ABC):
    """Abstract base type for protos.

    This is a type defining common functionality for all types representing Model Registry protos,
    such as Artifacts, Contexts, and Executions.

    Attributes:
        id: Protobuf object ID. Auto-assigned when put on the server.
        name: Name of the object.
        description: Description of the object.
        external_id: Customizable ID. Has to be unique among instances of the same type.
        create_time_since_epoch: Seconds elapsed since object creation time, measured against epoch.
        last_update_time_since_epoch: Seconds elapsed since object last update time, measured against epoch.
    """

    name: str
    id: str | None = field(kw_only=True, default=None)
    description: str | None = field(kw_only=True, default=None)
    external_id: str | None = field(kw_only=True, default=None)
    create_time_since_epoch: str | None = field(kw_only=True, default=None)
    last_update_time_since_epoch: str | None = field(kw_only=True, default=None)

    @abstractmethod
    def create(self, **kwargs) -> Parsable:
        """Get a *Create object for the current object."""

    @abstractmethod
    def update(self, **kwargs) -> Parsable:
        """Get a *Update object for the current object."""

    @classmethod
    def from_dataclass(cls: type[Resource], dataclass: Parsable) -> Resource:
        """Create a new object from a dataclass."""
        logger.debug(f"Creating new object from dataclass: {dataclass}")
        items = dataclass.__dict__
        additional_fields = items.pop("additional_data", None)
        if additional_fields:
            logger.debug(
                f"Appending additional fields into dataclass: {additional_fields}"
            )
            items.update(additional_fields)
        custom_properties = items.pop("custom_properties", None)
        if custom_properties:
            props_dict = custom_properties.__dict__
            custom_additional_fields = props_dict.pop("additional_data", None)
            if custom_additional_fields:
                items.update(custom_additional_fields)
                logger.debug(
                    f"Appending additional fields from custom properties into dataclass: {custom_additional_fields}"
                )
            logger.debug(f"Appending custom properties into dataclass: {props_dict}")
            items.update(props_dict)

        logger.debug(f"Gathered the following data: {items}")
        return cls(**items)

    @abstractmethod
    def as_dataclass(self) -> Parsable:
        """Return the object as a dataclass."""


class BaseOptions:
    """Base options for model registry API calls."""

    def to_camel_case(self, snake_str: str) -> str:
        """Convert a snake_case string to camelCase."""
        components = snake_str.split("_")
        return components[0] + "".join(x.title() for x in components[1:])

    def get_query_parameter(self, original_name: str) -> str:
        """Get the query parameter name from a snake_case field name."""
        return self.to_camel_case(original_name)
