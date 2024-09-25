"""Model registry types.

Types are based on [ML Metadata](https://github.com/google/ml-metadata), with Pythonic class wrappers.
"""

from .artifacts import Artifact, ArtifactState, DocArtifact, ModelArtifact
from .base import SupportedTypes, validate_metadata
from .contexts import (
    ModelVersion,
    ModelVersionState,
    RegisteredModel,
    RegisteredModelState,
)
from .options import ListOptions
from .pager import Pager

__all__ = [
    # Base
    "SupportedTypes",
    "validate_metadata",
    # Artifacts
    "Artifact",
    "ArtifactState",
    "DocArtifact",
    "ModelArtifact",
    # Contexts
    "ModelVersion",
    "ModelVersionState",
    "RegisteredModel",
    "RegisteredModelState",
    # Options
    "ListOptions",
    # Pager
    "Pager",
]
