from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Callable

from kiota_abstractions.serialization import ParseNode, SerializationWriter

if TYPE_CHECKING:
    from .base_artifact_create import BaseArtifactCreate

from .base_artifact_create import BaseArtifactCreate


@dataclass
class ModelArtifactCreate(BaseArtifactCreate):
    """An ML model artifact."""

    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode | None = None) -> ModelArtifactCreate:
        """Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModelArtifactCreate.
        """
        if not parse_node:
            msg = "parse_node cannot be null."
            raise TypeError(msg)
        return ModelArtifactCreate()

    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]].
        """
        fields: dict[str, Callable[[Any], None]] = {
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


