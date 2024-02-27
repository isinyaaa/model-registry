from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_resource_update import BaseResourceUpdate
    from .inference_service_state import InferenceServiceState

from .base_resource_update import BaseResourceUpdate

@dataclass
class InferenceServiceUpdate(BaseResourceUpdate):
    """
    An `InferenceService` entity in a `ServingEnvironment` represents a deployed `ModelVersion` from a `RegisteredModel` created by Model Serving.
    """
    from .inference_service_state import InferenceServiceState

    # - DEPLOYED: A state indicating that the `InferenceService` should be deployed.- UNDEPLOYED: A state indicating that the `InferenceService` should be un-deployed.The state indicates the desired state of inference service.See the associated `ServeModel` for the actual status of service deployment action.
    desired_state: Optional[InferenceServiceState] = InferenceServiceState("DEPLOYED")
    # ID of the `ModelVersion` to serve. If it's unspecified, then the latest `ModelVersion` by creation order will be served.
    model_version_id: Optional[str] = None
    # Model runtime.
    runtime: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InferenceServiceUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InferenceServiceUpdate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InferenceServiceUpdate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .base_resource_update import BaseResourceUpdate
        from .inference_service_state import InferenceServiceState

        from .base_resource_update import BaseResourceUpdate
        from .inference_service_state import InferenceServiceState

        fields: Dict[str, Callable[[Any], None]] = {
            "desiredState": lambda n : setattr(self, 'desired_state', n.get_enum_value(InferenceServiceState)),
            "modelVersionId": lambda n : setattr(self, 'model_version_id', n.get_str_value()),
            "runtime": lambda n : setattr(self, 'runtime', n.get_str_value()),
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
        writer.write_enum_value("desiredState", self.desired_state)
        writer.write_str_value("modelVersionId", self.model_version_id)
        writer.write_str_value("runtime", self.runtime)
    

