from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .inference_service_update import InferenceServiceUpdate

from .inference_service_update import InferenceServiceUpdate

@dataclass
class InferenceServiceCreate(InferenceServiceUpdate):
    """
    An `InferenceService` entity in a `ServingEnvironment` represents a deployed `ModelVersion` from a `RegisteredModel` created by Model Serving.
    """
    # ID of the `RegisteredModel` to serve.
    registered_model_id: Optional[str] = None
    # ID of the parent `ServingEnvironment` for this `InferenceService` entity.
    serving_environment_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InferenceServiceCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InferenceServiceCreate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InferenceServiceCreate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .inference_service_update import InferenceServiceUpdate

        from .inference_service_update import InferenceServiceUpdate

        fields: Dict[str, Callable[[Any], None]] = {
            "registeredModelId": lambda n : setattr(self, 'registered_model_id', n.get_str_value()),
            "servingEnvironmentId": lambda n : setattr(self, 'serving_environment_id', n.get_str_value()),
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
        writer.write_str_value("servingEnvironmentId", self.serving_environment_id)
    

