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
        name: Model version name.
        author: Author of the model version.
        description: Description of the object.
        external_id: Customizable ID. Has to be unique among instances of the same type.
        metadata: Metadata associated with this version.
    """

    name: str
    author: str
    metadata: dict[str, Any] = field(factory=dict)
    # state: ModelVersionState = field(kw_only=True, default=ModelVersionState.LIVE)

    registered_model_id: str | None = field(kw_only=True, default=None)


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
