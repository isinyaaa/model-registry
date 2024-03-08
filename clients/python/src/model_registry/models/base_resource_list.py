from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .serving_environment_list import ServingEnvironmentList

from .serving_environment_list import ServingEnvironmentList

@dataclass
class BaseResourceList(ServingEnvironmentList):
    """
    List of InferenceServices.
    """
    # Token to use to retrieve next page of results.
    next_page_token: Optional[str] = None
    # Maximum number of resources to return in the result.
    page_size: Optional[int] = None
    # Number of items in result list.
    size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BaseResourceList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BaseResourceList
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BaseResourceList()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .serving_environment_list import ServingEnvironmentList

        from .serving_environment_list import ServingEnvironmentList

        fields: Dict[str, Callable[[Any], None]] = {
            "nextPageToken": lambda n : setattr(self, 'next_page_token', n.get_str_value()),
            "pageSize": lambda n : setattr(self, 'page_size', n.get_int_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
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
        writer.write_str_value("nextPageToken", self.next_page_token)
        writer.write_int_value("pageSize", self.page_size)
        writer.write_int_value("size", self.size)
    

