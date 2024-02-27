from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.serialization.additional_data_holder import AdditionalDataHolder


@dataclass
class BaseResourceList(AdditionalDataHolder, Parsable):
    """List of BaseResource."""
    # Token to use to retrieve next page of results.
    next_page_token: str | None = None
    # Maximum number of resources to return in the result.
    page_size: int | None = None
    # Number of items in result list.
    size: int | None = None

    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode | None = None) -> BaseResourceList:
        """Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BaseResourceList.
        """
        if not parse_node:
            msg = "parse_node cannot be null."
            raise TypeError(msg)
        return BaseResourceList()

    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]].
        """
        fields: dict[str, Callable[[Any], None]] = {
            "nextPageToken": lambda n : setattr(self, "next_page_token", n.get_str_value()),
            "pageSize": lambda n : setattr(self, "page_size", n.get_int_value()),
            "size": lambda n : setattr(self, "size", n.get_int_value()),
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
        writer.write_str_value("nextPageToken", self.next_page_token)
        writer.write_int_value("pageSize", self.page_size)
        writer.write_int_value("size", self.size)


