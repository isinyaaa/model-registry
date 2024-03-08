from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Callable

from kiota_abstractions.serialization import ParseNode, SerializationWriter

if TYPE_CHECKING:
    from .base_resource_update import BaseResourceUpdate
    from .inference_service_state import InferenceServiceState

from .base_resource_update import BaseResourceUpdate


@dataclass
class InferenceServiceUpdate(BaseResourceUpdate):
    """An `InferenceService` entity in a `ServingEnvironment` represents a deployed `ModelVersion` from a `RegisteredModel` created by Model Serving."""
    from .inference_service_state import InferenceServiceState

    # - DEPLOYED: A state indicating that the `InferenceService` should be deployed.- UNDEPLOYED: A state indicating that the `InferenceService` should be un-deployed.The state indicates the desired state of inference service.See the associated `ServeModel` for the actual status of service deployment action.
    desired_state: InferenceServiceState | None = InferenceServiceState("DEPLOYED")
    # ID of the `ModelVersion` to serve. If it's unspecified, then the latest `ModelVersion` by creation order will be served.
    model_version_id: str | None = None
    # Model runtime.
    runtime: str | None = None

    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode | None = None) -> InferenceServiceUpdate:
        """Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InferenceServiceUpdate.
        """
        if not parse_node:
            msg = "parse_node cannot be null."
            raise TypeError(msg)
        return InferenceServiceUpdate()

    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]].
        """
        from .inference_service_state import InferenceServiceState

        fields: dict[str, Callable[[Any], None]] = {
            "desiredState": lambda n : setattr(self, "desired_state", n.get_enum_value(InferenceServiceState)),
            "modelVersionId": lambda n : setattr(self, "model_version_id", n.get_str_value()),
            "runtime": lambda n : setattr(self, "runtime", n.get_str_value()),
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
        writer.write_enum_value("desiredState", self.desired_state)
        writer.write_str_value("modelVersionId", self.model_version_id)
        writer.write_str_value("runtime", self.runtime)


