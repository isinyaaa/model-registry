from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from kiota_abstractions.api_error import APIError
from kiota_abstractions.serialization import (
    ParseNode,
    SerializationWriter,
)


@dataclass
class Error(APIError):
    """Error code and message."""
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Error code
    code: str | None = None
    # Error message
    message: str | None = None

    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode | None = None) -> Error:
        """Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Error.
        """
        if not parse_node:
            msg = "parse_node cannot be null."
            raise TypeError(msg)
        return Error()

    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]].
        """
        fields: dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, "code", n.get_str_value()),
            "message": lambda n : setattr(self, "message", n.get_str_value()),
        }
        return fields

    def serialize(self,writer: SerializationWriter) -> None:
        """Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None.
        """
        if not writer:
            msg = "writer cannot be null."
            raise TypeError(msg)
        writer.write_str_value("code", self.code)
        writer.write_str_value("message", self.message)
        writer.write_additional_data_value(self.additional_data)

    @property
    def primary_message(self) -> str:
        """The primary error message."""
        return super().message

