from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from kiota_abstractions.serialization import (
    AdditionalDataHolder,
    Parsable,
    ParseNode,
    SerializationWriter,
)

from .base_artifact import BaseArtifact
from .model_artifact_create import ModelArtifactCreate


@dataclass
class ModelArtifact(BaseArtifact, ModelArtifactCreate, AdditionalDataHolder, Parsable):
    """An ML model artifact."""
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The artifactType property
    artifact_type: str | None = "model-artifact"

    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode | None = None) -> ModelArtifact:
        """Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModelArtifact.
        """
        if not parse_node:
            msg = "parse_node cannot be null."
            raise TypeError(msg)
        return ModelArtifact()

    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]].
        """
        fields: dict[str, Callable[[Any], None]] = {
            "artifactType": lambda n: setattr(self, "artifact_type", n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields

    def serialize(self, writer: SerializationWriter) -> None:
        """Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None.
        """
        if not writer:
            msg = "writer cannot be null."
            raise TypeError(msg)
        super().serialize(writer)
        writer.write_str_value("artifactType", self.artifact_type)
        writer.write_additional_data_value(self.additional_data)
