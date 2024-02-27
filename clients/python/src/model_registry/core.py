"""Client for the model registry."""

from __future__ import annotations

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

from kiota_abstractions.authentication.anonymous_authentication_provider import (
    AnonymousAuthenticationProvider,
)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

from .exceptions import StoreException
from .model_registry_client import ModelRegistryClient
from .types import (
    FindOptions,
    ListOptions,
    ModelArtifact,
    ModelVersion,
    RegisteredModel,
    RequestOptions,
)

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from .api.model_registry.v1alpha3.v1alpha3_request_builder import (
        V1alpha3RequestBuilder,
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

    @asynccontextmanager
    async def get_client(self) -> AsyncIterator[V1alpha3RequestBuilder]:
        client = ModelRegistryClient(
            HttpxRequestAdapter(
                authentication_provider=AnonymousAuthenticationProvider(),
                base_url=self._server_address,
            )
        ).api.model_registry.v1alpha3
        try:
            yield client
        finally:
            pass

    async def upsert_registered_model(
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
        async with self.get_client() as client:
            if registered_model.id:
                logger.info("Updating registered model")
                rm = await client.registered_models.by_registeredmodel_id(
                    registered_model.id
                ).patch(registered_model.update(), RequestOptions())
            else:
                logger.info("Creating registered model")
                rm = await client.registered_models.post(
                    registered_model.create(), RequestOptions()
                )

            assert rm
            return RegisteredModel.from_dataclass(rm)

    async def get_registered_model_by_id(self, id: str) -> RegisteredModel | None:
        """Fetch a registered model by its ID.

        Args:
            id: Registered model ID.

        Returns:
            Registered model.
        """
        async with self.get_client() as client:
            rm = await client.registered_models.by_registeredmodel_id(id).get(
                RequestOptions()
            )
            if rm is not None:
                return RegisteredModel.from_dataclass(rm)
            return None

    async def get_registered_model_by_params(
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
        async with self.get_client() as client:
            if name is None and external_id is None:
                msg = "Either name or external_id must be provided"
                raise StoreException(msg)
            try:
                rm = await client.registered_model.get(
                    RequestOptions(
                        query_parameters=FindOptions(name=name, external_id=external_id)
                    )
                )
            except Exception as e:
                logger.warning(f"Failed to fetch registered model: {e}")
            else:
                if rm is not None:
                    return RegisteredModel.from_dataclass(rm)
            return None

    async def get_registered_models(
        self, options: ListOptions | None = None
    ) -> list[RegisteredModel]:
        """Fetch registered models.

        Args:
            options: Options for listing registered models.

        Returns:
            Registered models.
        """
        async with self.get_client() as client:
            models_rl = await client.registered_models.get(
                RequestOptions(query_parameters=options)
            )
            if models_rl and models_rl.items is not None:
                return [
                    RegisteredModel.from_dataclass(model) for model in models_rl.items
                ]
            return []

    async def upsert_model_version(
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
        async with self.get_client() as client:
            if model_version.id:
                logger.info("Updating model version")
                mv = await client.model_versions.by_modelversion_id(
                    model_version.id
                ).patch(model_version.update(), RequestOptions())
            else:
                logger.info("Creating model version")
                mv = await client.model_versions.post(
                    model_version.create(registered_model_id), RequestOptions()
                )
            assert mv
            return ModelVersion.from_dataclass(mv)

    async def get_model_version_by_id(
        self, model_version_id: str
    ) -> ModelVersion | None:
        """Fetch a model version by its ID.

        Args:
            model_version_id: Model version ID.

        Returns:
            Model version.
        """
        async with self.get_client() as client:
            mv = await client.model_versions.by_modelversion_id(model_version_id).get(
                RequestOptions()
            )
            if mv is not None:
                return ModelVersion.from_dataclass(mv)
            return None

    async def get_model_versions(
        self, registered_model_id: str, options: ListOptions | None = None
    ) -> list[ModelVersion]:
        """Fetch model versions by registered model ID.

        Args:
            registered_model_id: Registered model ID.
            options: Options for listing model versions.

        Returns:
            Model versions.
        """
        async with self.get_client() as client:
            versions_rl = await client.registered_models.by_registeredmodel_id(
                registered_model_id
            ).versions.get(RequestOptions(query_parameters=options))
            if versions_rl and versions_rl.items is not None:
                return [
                    ModelVersion.from_dataclass(model) for model in versions_rl.items
                ]
            return []

    async def get_model_version_by_params(
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
        async with self.get_client() as client:
            try:
                mv = await client.model_version.get(
                    RequestOptions(
                        query_parameters=FindOptions(
                            name=name,
                            external_id=external_id,
                            parent_resource_id=registered_model_id,
                        )
                    )
                )
            except Exception as e:
                logger.warning(f"Failed to fetch model version: {e}")
            else:
                if mv is not None:
                    return ModelVersion.from_dataclass(mv)
            return None

    async def upsert_model_artifact(
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
        async with self.get_client() as client:
            if model_artifact.id:
                logger.info("Updating model artifact")
                ma = await client.model_artifacts.by_modelartifact_id(
                    model_artifact.id
                ).patch(model_artifact.update(), RequestOptions())
            else:
                logger.info("Creating model artifact")
                art = await client.model_versions.by_modelversion_id(
                    model_version_id
                ).artifacts.post(
                    model_artifact.as_dataclass(),
                    RequestOptions(),
                )
                assert art
                ma = art.model_artifact
            assert ma
            return ModelArtifact.from_dataclass(ma)

    async def get_model_artifact_by_id(self, id: str) -> ModelArtifact | None:
        """Fetch a model artifact by its ID.

        Args:
            id: Model artifact ID.

        Returns:
            Model artifact.
        """
        async with self.get_client() as client:
            ma = await client.model_artifacts.by_modelartifact_id(id).get(
                RequestOptions()
            )
            if ma is not None:
                return ModelArtifact.from_dataclass(ma)
            return None

    async def get_model_artifact_by_params(
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
        async with self.get_client() as client:
            try:
                ma = await client.model_artifact.get(
                    RequestOptions(
                        query_parameters=FindOptions(
                            external_id=external_id, parent_resource_id=model_version_id
                        )
                    )
                )
            except Exception as e:
                logger.warning(f"Failed to fetch model artifact: {e}")
            else:
                if ma is not None:
                    return ModelArtifact.from_dataclass(ma)
            return None

    async def get_model_artifacts(
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
        async with self.get_client() as client:
            opts = RequestOptions(query_parameters=options)
            if model_version_id is not None:
                artifacts_rl = await client.model_versions.by_modelversion_id(
                    model_version_id
                ).artifacts.get(opts)
            else:
                artifacts_rl = await client.model_artifacts.get(opts)
            if artifacts_rl and artifacts_rl.items is not None:
                return [
                    ModelArtifact.from_dataclass(model) for model in artifacts_rl.items
                ]
            return []
