from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .doc_artifact import DocArtifact
    from .model_artifact import ModelArtifact

@dataclass
class Artifact(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes DocArtifact, ModelArtifact
    """
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Artifact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Artifact
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("artifactType").get_str_value()
        except AttributeError:
            mapping_value = None
        result = Artifact()
        if mapping_value and mapping_value.casefold() == "doc-artifact".casefold():
            from .doc_artifact import DocArtifact

            result.artifact_doc_artifact = DocArtifact()
        elif mapping_value and mapping_value.casefold() == "doc-artifact".casefold():
            from .doc_artifact import DocArtifact

            result.artifact_doc_artifact0 = DocArtifact()
        elif mapping_value and mapping_value.casefold() == "doc-artifact".casefold():
            from .doc_artifact import DocArtifact

            result.artifact_doc_artifact1 = DocArtifact()
        elif mapping_value and mapping_value.casefold() == "model-artifact".casefold():
            from .model_artifact import ModelArtifact

            result.artifact_model_artifact = ModelArtifact()
        elif mapping_value and mapping_value.casefold() == "model-artifact".casefold():
            from .model_artifact import ModelArtifact

            result.artifact_model_artifact0 = ModelArtifact()
        elif mapping_value and mapping_value.casefold() == "model-artifact".casefold():
            from .model_artifact import ModelArtifact

            result.artifact_model_artifact1 = ModelArtifact()
        elif mapping_value and mapping_value.casefold() == "doc-artifact".casefold():
            from .doc_artifact import DocArtifact

            result.doc_artifact = DocArtifact()
        elif mapping_value and mapping_value.casefold() == "model-artifact".casefold():
            from .model_artifact import ModelArtifact

            result.model_artifact = ModelArtifact()
        return result
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .doc_artifact import DocArtifact
        from .model_artifact import ModelArtifact

        if self.artifact_doc_artifact:
            return self.artifact_doc_artifact.get_field_deserializers()
        if self.artifact_doc_artifact0:
            return self.artifact_doc_artifact0.get_field_deserializers()
        if self.artifact_doc_artifact1:
            return self.artifact_doc_artifact1.get_field_deserializers()
        if self.artifact_model_artifact:
            return self.artifact_model_artifact.get_field_deserializers()
        if self.artifact_model_artifact0:
            return self.artifact_model_artifact0.get_field_deserializers()
        if self.artifact_model_artifact1:
            return self.artifact_model_artifact1.get_field_deserializers()
        if self.doc_artifact:
            return self.doc_artifact.get_field_deserializers()
        if self.model_artifact:
            return self.model_artifact.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        if self.artifact_doc_artifact:
            writer.write_object_value(None, self.artifact_doc_artifact)
        elif self.artifact_doc_artifact0:
            writer.write_object_value(None, self.artifact_doc_artifact0)
        elif self.artifact_doc_artifact1:
            writer.write_object_value(None, self.artifact_doc_artifact1)
        elif self.artifact_model_artifact:
            writer.write_object_value(None, self.artifact_model_artifact)
        elif self.artifact_model_artifact0:
            writer.write_object_value(None, self.artifact_model_artifact0)
        elif self.artifact_model_artifact1:
            writer.write_object_value(None, self.artifact_model_artifact1)
        elif self.doc_artifact:
            writer.write_object_value(None, self.doc_artifact)
        elif self.model_artifact:
            writer.write_object_value(None, self.model_artifact)
    

