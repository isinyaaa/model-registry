"""Base types for model registry."""

from __future__ import annotations

from abc import ABC

from attrs import define, field


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
