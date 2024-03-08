from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Callable

from kiota_abstractions.serialization import ParseNode, SerializationWriter

if TYPE_CHECKING:
    from .base_resource_create import BaseResourceCreate

from .base_resource_create import BaseResourceCreate


@dataclass
class BaseResource(BaseResourceCreate):
    # Output only. Create time of the resource in millisecond since epoch.
    create_time_since_epoch: str | None = None
    # Output only. The unique server generated id of the resource.
    id: str | None = None
    # Output only. Last update time of the resource since epoch in millisecondsince epoch.
    last_update_time_since_epoch: str | None = None

    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode | None = None) -> BaseResource:
        """Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BaseResource.
        """
        if not parse_node:
            msg = "parse_node cannot be null."
            raise TypeError(msg)
        return BaseResource()

    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]].
        """
        fields: dict[str, Callable[[Any], None]] = {
            "createTimeSinceEpoch": lambda n : setattr(self, "create_time_since_epoch", n.get_str_value()),
            "id": lambda n : setattr(self, "id", n.get_str_value()),
            "lastUpdateTimeSinceEpoch": lambda n : setattr(self, "last_update_time_since_epoch", n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields

    def serialize(self,writer: SerializationWriter) -> None:
        """Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None.
        """
        if not writer:
            msg = "writer cannot be null."
            raise TypeError(msg)
        super().serialize(writer)


