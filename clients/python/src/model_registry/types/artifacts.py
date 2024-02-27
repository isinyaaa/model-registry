"""Artifact types for model registry.

Artifacts represent pieces of data.
This could be datasets, models, metrics, or any other piece of data produced or consumed by an
execution, such as an experiment run.

Those types are used to map between proto types based on artifacts and Python objects.

Todo:
    * Move part of the description to API Reference docs (#120).
"""

from __future__ import annotations

from abc import ABC
from typing import TypeVar

from attrs import define, field

from ..models.artifact_state import ArtifactState
from ..models.model_artifact import ModelArtifact as ModelArtifactDataclass
from ..models.model_artifact_create import ModelArtifactCreate
from ..models.model_artifact_update import ModelArtifactUpdate
from .base import BaseResourceModel, Parsable

ArtifactResource = TypeVar("ArtifactResource", bound="BaseArtifactModel")


@define(slots=False)
class BaseArtifactModel(BaseResourceModel, ABC):
    """Abstract base class for all artifacts.

    Attributes:
        name: Name of the artifact.
        uri: URI of the artifact.
        state: State of the artifact.
    """

    name: str
    uri: str
    state: ArtifactState = field(kw_only=True, default=ArtifactState.UNKNOWN)

    @classmethod
    def from_dataclass(cls: type[ArtifactResource], dataclass: Parsable) -> ArtifactResource:
        """Create a new object from a dataclass."""
        items = dataclass.__dict__
        items.pop("artifact_type", None)
        return super().from_dataclass(dataclass)


@define(slots=False, auto_attribs=True)
class ModelArtifact(BaseArtifactModel):
    """Represents a Model.

    Attributes:
        name: Name of the model.
        uri: URI of the model.
        description: Description of the object.
        external_id: Customizable ID. Has to be unique among instances of the same type.
        model_format_name: Name of the model format.
        model_format_version: Version of the model format.
        storage_key: Storage secret name.
        storage_path: Storage path of the model.
        service_account_name: Name of the service account with storage secret.
    """

    # TODO: this could be an enum of valid formats
    model_format_name: str | None = field(kw_only=True, default=None)
    model_format_version: str | None = field(kw_only=True, default=None)
    storage_key: str | None = field(kw_only=True, default=None)
    storage_path: str | None = field(kw_only=True, default=None)
    service_account_name: str | None = field(kw_only=True, default=None)

    # _model_version_id: str | None = field(init=False, default=None)

    def create(self, **kwargs) -> ModelArtifactCreate:
        return ModelArtifactCreate(
            name=self.name,
            description=self.description,
            external_id=self.external_id,
            state=self.state,
            uri=self.uri,
            model_format_name=self.model_format_name,
            model_format_version=self.model_format_version,
            storage_key=self.storage_key,
            storage_path=self.storage_path,
            service_account_name=self.service_account_name,
            **kwargs,
        )

    def update(self, **kwargs) -> ModelArtifactUpdate:
        return ModelArtifactUpdate(
            description=self.description,
            external_id=self.external_id,
            state=self.state,
            uri=self.uri,
            model_format_name=self.model_format_name,
            model_format_version=self.model_format_version,
            storage_key=self.storage_key,
            storage_path=self.storage_path,
            service_account_name=self.service_account_name,
            **kwargs,
        )

    def as_dataclass(self) -> ModelArtifactDataclass:
        """Return the current object as a dataclass."""
        return ModelArtifactDataclass(
            name=self.name,
            uri=self.uri,
            description=self.description,
            external_id=self.external_id,
            model_format_name=self.model_format_name,
            model_format_version=self.model_format_version,
            storage_key=self.storage_key,
            storage_path=self.storage_path,
            service_account_name=self.service_account_name,
            additional_data={
                "create_time_since_epoch": self.create_time_since_epoch,
                "last_update_time_since_epoch": self.last_update_time_since_epoch,
            },
        )
