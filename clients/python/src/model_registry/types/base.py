"""Base types for model registry."""

from __future__ import annotations

import base64
import json
import typing as t
from abc import ABC, abstractmethod
from collections.abc import Mapping, Sequence

from pydantic import BaseModel, ConfigDict

from mr_openapi.models.metadata_value import MetadataValue

SupportedTypes = t.Union[bool, int, float, str, list, dict]


def validate_metadata(
    meta: Mapping[str, SupportedTypes] | Sequence[SupportedTypes],
) -> bool:
    """Validate metadata.

    Checks if the metadata is a valid dictionary of supported types.
    """
    vals = meta if isinstance(meta, Sequence) else meta.values()
    for v in vals:
        if isinstance(v, (list, dict)):
            return validate_metadata(v)
        if not isinstance(v, t.get_args(SupportedTypes)):
            return False
    return True


class BaseResourceModel(BaseModel, ABC):
    """Abstract base type for protos.

    This is a type defining common functionality for all types representing Model Registry resources,
    such as Artifacts, Contexts, and Executions.

    Attributes:
        id: Object ID. Auto-assigned when put on the server.
        name: Name of the object.
        description: Description of the object.
        external_id: Customizable ID. Has to be unique among instances of the same type.
        create_time_since_epoch: Seconds elapsed since object creation time, measured against epoch.
        last_update_time_since_epoch: Seconds elapsed since object last update time, measured against epoch.
    """

    model_config = ConfigDict(protected_namespaces=())

    id: str | None = None
    description: str | None = None
    external_id: str | None = None
    create_time_since_epoch: str | None = None
    last_update_time_since_epoch: str | None = None
    custom_properties: Mapping[str, SupportedTypes] | None = None

    @abstractmethod
    def create(self, **kwargs) -> t.Any:
        """Convert the object to a create request."""

    @abstractmethod
    def update(self, **kwargs) -> t.Any:
        """Convert the object to an update request."""

    @classmethod
    @abstractmethod
    def from_basemodel(cls, source: t.Any) -> t.Any:
        """Create a new object from a BaseModel object."""

    def _map_custom_properties(
        self,
    ) -> dict[str, MetadataValue] | None:
        """Map properties from Python to proto.

        Args:
            py_props: Python properties.
            mlmd_props: Proto properties, will be modified in place.
        """
        if not self.custom_properties:
            return None

        def get_meta_value(v: SupportedTypes) -> MetadataValue:
            if isinstance(v, float):
                meta_type = "double"
            elif isinstance(v, str):
                meta_type = "string"
            elif isinstance(v, (list, dict)):
                meta_type = "struct"
                if isinstance(v, list):
                    v = {str(i): x for i, x in enumerate(v)}
                v = base64.b64encode(  # encode as base64
                    json.dumps(v).encode()  # dump to json then encode as bytes
                ).decode()  # decode to string (keeping base64 encoding)
            else:
                meta_type = type(v).__name__.lower()
                v = str(v) if isinstance(v, int) and not isinstance(v, bool) else v
            return MetadataValue.from_dict(
                {
                    f"{meta_type}_value": v,
                    "metadataType": f"Metadata{meta_type.capitalize()}Value",
                }
            )

        dest = {}
        for key, value in self.custom_properties.items():
            if value is None:
                continue
            dest[key] = get_meta_value(value)
        return dest

    @classmethod
    def _unmap_custom_properties(
        cls, custom_properties: dict[str, MetadataValue]
    ) -> dict[str, SupportedTypes]:
        def get_meta_value(meta: t.Any) -> SupportedTypes:
            type_name = meta.metadata_type[8:-5].lower()
            # Metadata type names are in the format Metadata<Type>Value
            v = getattr(meta, f"{type_name}_value")
            if type_name == "int":
                return int(v)
            if type_name == "struct":
                data = t.cast(dict[str, t.Any], json.loads(base64.b64decode(v)))
                if all(k.isdigit() for k in data):
                    return list(data.values())
                return data
            return v

        return {
            name: value
            for name, meta_value in custom_properties.items()
            if isinstance(
                value := get_meta_value(meta_value.actual_instance),
                t.get_args(SupportedTypes),
            )
        }

    def _props_as_dict(
        self, exclude: Sequence[str] | None = None, alias: bool = False
    ) -> dict[str, t.Any]:
        exclude = exclude or []
        return {
            k: getattr(self, k)
            for k in self.model_json_schema(alias).get("properties", {})
            if k not in exclude
        }
