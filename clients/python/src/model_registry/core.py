"""Client for the model registry."""

from __future__ import annotations

from .types import (
    ListOptions,
    ModelArtifact,
    ModelVersion,
    RegisteredModel,
)


class ModelRegistryAPIClient:
    """Model registry API."""

    def __init__(
        self,
        server_address: str,
    ):
        """Constructor.

        Args:
            server_address: Server address.
        """
        self._server_address = server_address

    def upsert_registered_model(
        self, registered_model: RegisteredModel
    ) -> RegisteredModel:
        """Upsert a registered model.

        Updates or creates a registered model on the server.
        This updates the registered_model instance passed in with new data from the servers.

        Args:
            registered_model: Registered model.

        Returns:
            ID of the registered model.
        """
        pass

    def get_registered_model_by_id(self, id: str) -> RegisteredModel | None:
        """Fetch a registered model by its ID.

        Args:
            id: Registered model ID.

        Returns:
            Registered model.
        """
        pass

    def get_registered_model_by_params(
        self, name: str | None = None, external_id: str | None = None
    ) -> RegisteredModel | None:
        """Fetch a registered model by its name or external ID.

        Args:
            name: Registered model name.
            external_id: Registered model external ID.

        Returns:
            Registered model.

        Raises:
            StoreException: If neither name nor external ID is provided.
        """
        pass

    def get_registered_models(
        self, options: ListOptions | None = None
    ) -> list[RegisteredModel]:
        """Fetch registered models.

        Args:
            options: Options for listing registered models.

        Returns:
            Registered models.
        """
        pass

    def upsert_model_version(
        self, model_version: ModelVersion, registered_model_id: str
    ) -> ModelVersion:
        """Upsert a model version.

        Updates or creates a model version on the server.
        This updates the model_version instance passed in with new data from the servers.

        Args:
            model_version: Model version to upsert.
            registered_model_id: ID of the registered model this version will be associated to.

        Returns:
            ID of the model version.
        """
        pass

    def get_model_version_by_id(self, model_version_id: str) -> ModelVersion | None:
        """Fetch a model version by its ID.

        Args:
            model_version_id: Model version ID.

        Returns:
            Model version.
        """
        pass

    def get_model_versions(
        self, registered_model_id: str, options: ListOptions | None = None
    ) -> list[ModelVersion]:
        """Fetch model versions by registered model ID.

        Args:
            registered_model_id: Registered model ID.
            options: Options for listing model versions.

        Returns:
            Model versions.
        """
        pass

    def get_model_version_by_params(
        self,
        registered_model_id: str | None = None,
        name: str | None = None,
        external_id: str | None = None,
    ) -> ModelVersion | None:
        """Fetch a model version by associated parameters.

        Either fetches by using external ID or by using registered model ID and version.

        Args:
            registered_model_id: Registered model ID.
            name: Model version name.
            external_id: Model version external ID.

        Returns:
            Model version.

        Raises:
            StoreException: If neither external ID nor registered model ID and version is provided.
        """
        pass

    def upsert_model_artifact(
        self, model_artifact: ModelArtifact, model_version_id: str
    ) -> ModelArtifact:
        """Upsert a model artifact.

        Updates or creates a model artifact on the server.
        This updates the model_artifact instance passed in with new data from the servers.

        Args:
            model_artifact: Model artifact to upsert.
            model_version_id: ID of the model version this artifact will be associated to.

        Returns:
            ID of the model artifact.

        Raises:
            StoreException: If the model version already has a model artifact.
        """
        pass

    def get_model_artifact_by_id(self, id: str) -> ModelArtifact | None:
        """Fetch a model artifact by its ID.

        Args:
            id: Model artifact ID.

        Returns:
            Model artifact.
        """
        pass

    def get_model_artifact_by_params(
        self, model_version_id: str | None = None, external_id: str | None = None
    ) -> ModelArtifact | None:
        """Fetch a model artifact either by external ID or by the ID of its associated model version.

        Args:
            model_version_id: ID of the associated model version.
            external_id: Model artifact external ID.

        Returns:
            Model artifact.

        Raises:
            StoreException: If neither external ID nor model version ID is provided.
        """
        pass

    def get_model_artifacts(
        self,
        model_version_id: str | None = None,
        options: ListOptions | None = None,
    ) -> list[ModelArtifact]:
        """Fetches model artifacts.

        Args:
            model_version_id: ID of the associated model version.
            options: Options for listing model artifacts.

        Returns:
            Model artifacts.
        """
        pass
