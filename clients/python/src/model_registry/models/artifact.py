from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable

from kiota_abstractions.serialization import (
    ComposedTypeWrapper,
    Parsable,
    ParseNode,
    SerializationWriter,
)

from .doc_artifact import DocArtifact
from .model_artifact import ModelArtifact

if TYPE_CHECKING:
    pass

@dataclass
class Artifact(ComposedTypeWrapper, Parsable):
    """Composed type wrapper for classes DocArtifact, ModelArtifact."""
    doc_artifact: DocArtifact | None = None
    model_artifact: ModelArtifact | None = None

    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode | None = None) -> Artifact:
        """Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Artifact.
        """
        if not parse_node:
            msg = "parse_node cannot be null."
            raise TypeError(msg)
        try:
            mapping_value = parse_node.get_child_node("artifactType").get_str_value()
        except AttributeError:
            mapping_value = None
        result = Artifact()
        if mapping_value and mapping_value.casefold() == "doc-artifact".casefold():
            result.doc_artifact = DocArtifact()
        elif mapping_value and mapping_value.casefold() == "model-artifact".casefold():
            result.model_artifact = ModelArtifact()
        return result

    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]].
        """
        if self.doc_artifact:
            return self.doc_artifact.get_field_deserializers()
        if self.model_artifact:
            return self.model_artifact.get_field_deserializers()
        return {}

    def serialize(self,writer: SerializationWriter) -> None:
        """Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None.
        """
        if not writer:
            msg = "writer cannot be null."
            raise TypeError(msg)
        if self.doc_artifact:
            writer.write_object_value(None, self.doc_artifact)
        elif self.model_artifact:
            writer.write_object_value(None, self.model_artifact)

