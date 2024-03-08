from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Callable

from kiota_abstractions.serialization import ParseNode, SerializationWriter

if TYPE_CHECKING:
    from .base_resource_update import BaseResourceUpdate
    from .model_version_state import ModelVersionState

from .base_resource_update import BaseResourceUpdate


@dataclass
class ModelVersionUpdate(BaseResourceUpdate):
    """Represents a ModelVersion belonging to a RegisteredModel."""
    from .model_version_state import ModelVersionState

    # - LIVE: A state indicating that the `ModelVersion` exists- ARCHIVED: A state indicating that the `ModelVersion` has been archived.
    state: ModelVersionState | None = ModelVersionState("LIVE")
    # Name of the author.
    author: str | None = None

    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode | None = None) -> ModelVersionUpdate:
        """Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModelVersionUpdate.
        """
        if not parse_node:
            msg = "parse_node cannot be null."
            raise TypeError(msg)
        return ModelVersionUpdate()

    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]].
        """
        from .model_version_state import ModelVersionState

        fields: dict[str, Callable[[Any], None]] = {
            "author": lambda n : setattr(self, "author", n.get_str_value()),
            "state": lambda n : setattr(self, "state", n.get_enum_value(ModelVersionState)),
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
        writer.write_str_value("author", self.author)
        writer.write_enum_value("state", self.state)


