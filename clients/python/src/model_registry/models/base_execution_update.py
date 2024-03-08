from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Callable

from kiota_abstractions.serialization import ParseNode, SerializationWriter

if TYPE_CHECKING:
    from .base_resource_update import BaseResourceUpdate
    from .execution_state import ExecutionState

from .base_resource_update import BaseResourceUpdate


@dataclass
class BaseExecutionUpdate(BaseResourceUpdate):
    from .execution_state import ExecutionState

    # The state of the Execution. The state transitions are  NEW -> RUNNING -> COMPLETE | CACHED | FAILED | CANCELEDCACHED means the execution is skipped due to cached results.CANCELED means the execution is skipped due to precondition not met. It isdifferent from CACHED in that a CANCELED execution will not have any eventassociated with it. It is different from FAILED in that there is nounexpected error happened and it is regarded as a normal state.See also: ml-metadata Execution.State
    last_known_state: ExecutionState | None = ExecutionState("UNKNOWN")

    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode | None = None) -> BaseExecutionUpdate:
        """Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BaseExecutionUpdate.
        """
        if not parse_node:
            msg = "parse_node cannot be null."
            raise TypeError(msg)
        return BaseExecutionUpdate()

    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]].
        """
        from .execution_state import ExecutionState

        fields: dict[str, Callable[[Any], None]] = {
            "lastKnownState": lambda n : setattr(self, "last_known_state", n.get_enum_value(ExecutionState)),
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
        writer.write_enum_value("lastKnownState", self.last_known_state)


