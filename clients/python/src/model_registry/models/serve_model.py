from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from kiota_abstractions.serialization import (
    AdditionalDataHolder,
    Parsable,
    ParseNode,
    SerializationWriter,
)


@dataclass
class ServeModel(AdditionalDataHolder, Parsable):
    """An ML model serving action."""
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # ID of the `ModelVersion` that was served in `InferenceService`.
    model_version_id: str | None = None

    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode | None = None) -> ServeModel:
        """Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServeModel.
        """
        if not parse_node:
            msg = "parse_node cannot be null."
            raise TypeError(msg)
        return ServeModel()

    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]].
        """
        fields: dict[str, Callable[[Any], None]] = {
            "modelVersionId": lambda n : setattr(self, "model_version_id", n.get_str_value()),
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
        writer.write_str_value("modelVersionId", self.model_version_id)
        writer.write_additional_data_value(self.additional_data)


