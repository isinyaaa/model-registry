from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Callable

from kiota_abstractions.serialization import ParseNode, SerializationWriter

if TYPE_CHECKING:
    from .base_resource_update import BaseResourceUpdate
    from .registered_model_state import RegisteredModelState

from .base_resource_update import BaseResourceUpdate


@dataclass
class RegisteredModelUpdate(BaseResourceUpdate):
    """A registered model in model registry. A registered model has ModelVersion children."""
    from .registered_model_state import RegisteredModelState

    # - LIVE: A state indicating that the `RegisteredModel` exists- ARCHIVED: A state indicating that the `RegisteredModel` has been archived.
    state: RegisteredModelState | None = RegisteredModelState("LIVE")

    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode | None = None) -> RegisteredModelUpdate:
        """Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RegisteredModelUpdate.
        """
        if not parse_node:
            msg = "parse_node cannot be null."
            raise TypeError(msg)
        return RegisteredModelUpdate()

    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]].
        """
        from .registered_model_state import RegisteredModelState

        fields: dict[str, Callable[[Any], None]] = {
            "state": lambda n : setattr(self, "state", n.get_enum_value(RegisteredModelState)),
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
        writer.write_enum_value("state", self.state)


