"""Context types for model registry.

Contexts group related Artifacts together.
They provide a way to organize and categorize components in a workflow.

Those types are used to map between proto types based on contexts and Python objects.

Todo:
    * Move part of the description to API Reference docs (#120).
"""

from __future__ import annotations

from attrs import define, field

from ..models.model_version import ModelVersion as ModelVersionDataclass
from ..models.model_version_create import ModelVersionCreate
from ..models.model_version_state import ModelVersionState
from ..models.model_version_update import ModelVersionUpdate
from ..models.registered_model import RegisteredModel as RegisteredModelDataclass
from ..models.registered_model_create import RegisteredModelCreate
from ..models.registered_model_state import RegisteredModelState
from ..models.registered_model_update import RegisteredModelUpdate
from .base import BaseResourceModel


@define(slots=False)
class ModelVersion(BaseResourceModel):
    """Represents a model version.

    Attributes:
        name: Model version name.
        author: Author of the model version.
        description: Description of the object.
        external_id: Customizable ID. Has to be unique among instances of the same type.
        metadata: Metadata associated with this version.
    """

    name: str
    author: str
    metadata: dict[str, Any] = field(factory=dict)
    state: ModelVersionState = field(kw_only=True, default=ModelVersionState.LIVE)

    registered_model_id: str | None = field(kw_only=True, default=None)

    def create(self, registered_model_id: str, **kwargs) -> ModelVersionCreate:
        return ModelVersionCreate(
            name=self.name,
            description=self.description,
            external_id=self.external_id,
            state=self.state,
            author=self.author,
            registered_model_id=registered_model_id,
            **kwargs,
        )

    def update(self, **kwargs) -> ModelVersionUpdate:
        return ModelVersionUpdate(
            description=self.description,
            external_id=self.external_id,
            state=self.state,
            author=self.author,
            **kwargs,
        )

    def as_dataclass(self) -> ModelVersionDataclass:
        return ModelVersionDataclass(
            name=self.name,
            description=self.description,
            external_id=self.external_id,
            state=self.state,
            author=self.author,
            registered_model_id=self.registered_model_id,
            custom_properties=self.metadata,
            additional_data={
                "create_time_since_epoch": self.create_time_since_epoch,
                "last_update_time_since_epoch": self.last_update_time_since_epoch,
            },
        )


@define(slots=False)
class RegisteredModel(BaseResourceModel):
    """Represents a registered model.

    Attributes:
        name: Registered model name.
        description: Description of the object.
        external_id: Customizable ID. Has to be unique among instances of the same type.
    """

    name: str
    state: RegisteredModelState = field(kw_only=True, default=RegisteredModelState.LIVE)

    def create(self, **kwargs) -> RegisteredModelCreate:
        return RegisteredModelCreate(
            name=self.name,
            description=self.description,
            external_id=self.external_id,
            state=self.state,
            **kwargs,
        )

    def update(self, **kwargs) -> RegisteredModelUpdate:
        return RegisteredModelUpdate(
            description=self.description,
            external_id=self.external_id,
            state=self.state,
            **kwargs,
        )

    def as_dataclass(self) -> RegisteredModelDataclass:
        return RegisteredModelDataclass(
            name=self.name,
            description=self.description,
            external_id=self.external_id,
            state=self.state,
            create_time_since_epoch=self.create_time_since_epoch,
            last_update_time_since_epoch=self.last_update_time_since_epoch,
        )
