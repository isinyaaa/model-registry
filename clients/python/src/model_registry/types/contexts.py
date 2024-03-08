"""Context types for model registry.

Contexts group related Artifacts together.
They provide a way to organize and categorize components in a workflow.

Those types are used to map between proto types based on contexts and Python objects.

Todo:
    * Move part of the description to API Reference docs (#120).
"""

from __future__ import annotations

from attrs import define, field

from .base import BaseResourceModel


@define(slots=False)
class ModelVersion(BaseResourceModel):
    """Represents a model version.

    Attributes:
        model_name: Name of the model associated with this version.
        version: Version of the model.
        author: Author of the model version.
        description: Description of the object.
        external_id: Customizable ID. Has to be unique among instances of the same type.
        artifacts: Artifacts associated with this version.
        metadata: Metadata associated with this version.
    """

    model_name: str
    version: str
    author: str
    metadata: dict[str, ScalarType] = field(factory=dict)
    artifacts: list[BaseArtifact] = field(init=False, factory=list)

    _registered_model_id: str | None = field(init=False, default=None)

    def __attrs_post_init__(self) -> None:
        self.name = self.version


@define(slots=False)
class RegisteredModel(BaseResourceModel):
    """Represents a registered model.

    Attributes:
        name: Registered model name.
        description: Description of the object.
        external_id: Customizable ID. Has to be unique among instances of the same type.
    """

    name: str
    # state: RegisteredModelState = field(kw_only=True, default=RegisteredModelState.LIVE)
