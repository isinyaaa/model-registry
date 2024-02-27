from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_resource_create import BaseResourceCreate

from .base_resource_create import BaseResourceCreate

@dataclass
class ModelVersionCreate(BaseResourceCreate):
    """
    Represents a ModelVersion belonging to a RegisteredModel.
    """
    # ID of the `RegisteredModel` to which this version belongs.
    registered_model_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ModelVersionCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModelVersionCreate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ModelVersionCreate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .base_resource_create import BaseResourceCreate

        from .base_resource_create import BaseResourceCreate

        fields: Dict[str, Callable[[Any], None]] = {
            "registeredModelId": lambda n : setattr(self, 'registered_model_id', n.get_str_value()),
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
        writer.write_str_value("registeredModelId", self.registered_model_id)
    

