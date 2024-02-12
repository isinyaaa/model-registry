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

from attrs import define, field

from .base import BaseResourceModel


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
    # state: ArtifactState = field(init=False, default=ArtifactState.UNKNOWN)


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
