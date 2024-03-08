from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Callable

from kiota_abstractions.serialization import (
    AdditionalDataHolder,
    Parsable,
    ParseNode,
    SerializationWriter,
)

if TYPE_CHECKING:
    from .base_resource_update_custom_properties import (
        BaseResourceUpdate_customProperties,
    )

@dataclass
class BaseResourceUpdate(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # User provided custom properties which are not defined by its type.
    custom_properties: BaseResourceUpdate_customProperties | None = None
    # An optional description about the resource.
    description: str | None = None
    # The external id that come from the clients’ system. This field is optional.If set, it must be unique among all resources within a database instance.
    external_id: str | None = None

    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode | None = None) -> BaseResourceUpdate:
        """Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BaseResourceUpdate.
        """
        if not parse_node:
            msg = "parse_node cannot be null."
            raise TypeError(msg)
        return BaseResourceUpdate()

    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]].
        """
        from .base_resource_update_custom_properties import (
            BaseResourceUpdate_customProperties,
        )

        fields: dict[str, Callable[[Any], None]] = {
            "customProperties": lambda n : setattr(self, "custom_properties", n.get_object_value(BaseResourceUpdate_customProperties)),
            "description": lambda n : setattr(self, "description", n.get_str_value()),
            "externalId": lambda n : setattr(self, "external_id", n.get_str_value()),
        }
        return fields

    def serialize(self,writer: SerializationWriter) -> None:
        """Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None.
        """
        if not writer:
            msg = "writer cannot be null."
            raise TypeError(msg)
        writer.write_object_value("customProperties", self.custom_properties)
        writer.write_str_value("description", self.description)
        writer.write_str_value("externalId", self.external_id)
        writer.write_additional_data_value(self.additional_data)


