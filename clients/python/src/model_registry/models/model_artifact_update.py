from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_artifact_update import BaseArtifactUpdate

from .base_artifact_update import BaseArtifactUpdate

@dataclass
class ModelArtifactUpdate(BaseArtifactUpdate):
    """
    An ML model artifact.
    """
    # Name of the model format.
    model_format_name: Optional[str] = None
    # Version of the model format.
    model_format_version: Optional[str] = None
    # Name of the service account with storage secret.
    service_account_name: Optional[str] = None
    # Storage secret name.
    storage_key: Optional[str] = None
    # Path for model in storage provided by `storageKey`.
    storage_path: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ModelArtifactUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModelArtifactUpdate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ModelArtifactUpdate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .base_artifact_update import BaseArtifactUpdate

        from .base_artifact_update import BaseArtifactUpdate

        fields: Dict[str, Callable[[Any], None]] = {
            "modelFormatName": lambda n : setattr(self, 'model_format_name', n.get_str_value()),
            "modelFormatVersion": lambda n : setattr(self, 'model_format_version', n.get_str_value()),
            "serviceAccountName": lambda n : setattr(self, 'service_account_name', n.get_str_value()),
            "storageKey": lambda n : setattr(self, 'storage_key', n.get_str_value()),
            "storagePath": lambda n : setattr(self, 'storage_path', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("modelFormatName", self.model_format_name)
        writer.write_str_value("modelFormatVersion", self.model_format_version)
        writer.write_str_value("serviceAccountName", self.service_account_name)
        writer.write_str_value("storageKey", self.storage_key)
        writer.write_str_value("storagePath", self.storage_path)
    

