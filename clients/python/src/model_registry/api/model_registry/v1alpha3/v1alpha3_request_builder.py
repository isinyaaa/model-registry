from __future__ import annotations

from typing import TYPE_CHECKING, Any

from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.request_adapter import RequestAdapter

if TYPE_CHECKING:
    from .inference_service.inference_service_request_builder import (
        Inference_serviceRequestBuilder,
    )
    from .inference_services.inference_services_request_builder import (
        Inference_servicesRequestBuilder,
    )
    from .model_artifact.model_artifact_request_builder import (
        Model_artifactRequestBuilder,
    )
    from .model_artifacts.model_artifacts_request_builder import (
        Model_artifactsRequestBuilder,
    )
    from .model_version.model_version_request_builder import Model_versionRequestBuilder
    from .model_versions.model_versions_request_builder import (
        Model_versionsRequestBuilder,
    )
    from .registered_model.registered_model_request_builder import (
        Registered_modelRequestBuilder,
    )
    from .registered_models.registered_models_request_builder import (
        Registered_modelsRequestBuilder,
    )
    from .serving_environment.serving_environment_request_builder import (
        Serving_environmentRequestBuilder,
    )
    from .serving_environments.serving_environments_request_builder import (
        Serving_environmentsRequestBuilder,
    )

class V1alpha3RequestBuilder(BaseRequestBuilder):
    """Builds and executes requests for operations under /api/model_registry/v1alpha3."""
    def __init__(self,request_adapter: RequestAdapter, path_parameters: str | dict[str, Any]) -> None:
        """Instantiates a new V1alpha3RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None.
        """
        super().__init__(request_adapter, "{+baseurl}/api/model_registry/v1alpha3", path_parameters)

    @property
    def inference_service(self) -> Inference_serviceRequestBuilder:
        """The REST endpoint/path used to list and create zero or more `InferenceService` entities.  This path contains a `GET` and `POST` operation to perform the list and create tasks, respectively."""
        from .inference_service.inference_service_request_builder import (
            Inference_serviceRequestBuilder,
        )

        return Inference_serviceRequestBuilder(self.request_adapter, self.path_parameters)

    @property
    def inference_services(self) -> Inference_servicesRequestBuilder:
        """The REST endpoint/path used to list and create zero or more `InferenceService` entities.  This path contains a `GET` and `POST` operation to perform the list and create tasks, respectively."""
        from .inference_services.inference_services_request_builder import (
            Inference_servicesRequestBuilder,
        )

        return Inference_servicesRequestBuilder(self.request_adapter, self.path_parameters)

    @property
    def model_artifact(self) -> Model_artifactRequestBuilder:
        """The REST endpoint/path used to search for a `ModelArtifact` entity.  This path contains a `GET` operation to perform the find task."""
        from .model_artifact.model_artifact_request_builder import (
            Model_artifactRequestBuilder,
        )

        return Model_artifactRequestBuilder(self.request_adapter, self.path_parameters)

    @property
    def model_artifacts(self) -> Model_artifactsRequestBuilder:
        """The REST endpoint/path used to list and create zero or more `ModelArtifact` entities.  This path contains a `GET` and `POST` operation to perform the list and create tasks, respectively."""
        from .model_artifacts.model_artifacts_request_builder import (
            Model_artifactsRequestBuilder,
        )

        return Model_artifactsRequestBuilder(self.request_adapter, self.path_parameters)

    @property
    def model_version(self) -> Model_versionRequestBuilder:
        """The REST endpoint/path used to search for a `ModelVersion` entity.  This path contains a `GET` operation to perform the find task."""
        from .model_version.model_version_request_builder import (
            Model_versionRequestBuilder,
        )

        return Model_versionRequestBuilder(self.request_adapter, self.path_parameters)

    @property
    def model_versions(self) -> Model_versionsRequestBuilder:
        """The REST endpoint/path used to list and create zero or more `ModelVersion` entities.  This path contains a `GET` and `POST` operation to perform the list and create tasks, respectively."""
        from .model_versions.model_versions_request_builder import (
            Model_versionsRequestBuilder,
        )

        return Model_versionsRequestBuilder(self.request_adapter, self.path_parameters)

    @property
    def registered_model(self) -> Registered_modelRequestBuilder:
        """The REST endpoint/path used to search for a `RegisteredModel` entity.  This path contains a `GET` operation to perform the find task."""
        from .registered_model.registered_model_request_builder import (
            Registered_modelRequestBuilder,
        )

        return Registered_modelRequestBuilder(self.request_adapter, self.path_parameters)

    @property
    def registered_models(self) -> Registered_modelsRequestBuilder:
        """The REST endpoint/path used to list and create zero or more `RegisteredModel` entities.  This path contains a `GET` and `POST` operation to perform the list and create tasks, respectively."""
        from .registered_models.registered_models_request_builder import (
            Registered_modelsRequestBuilder,
        )

        return Registered_modelsRequestBuilder(self.request_adapter, self.path_parameters)

    @property
    def serving_environment(self) -> Serving_environmentRequestBuilder:
        """The REST endpoint/path used to search for a `ServingEnvironment` entity.  This path contains a `GET` operation to perform the find task."""
        from .serving_environment.serving_environment_request_builder import (
            Serving_environmentRequestBuilder,
        )

        return Serving_environmentRequestBuilder(self.request_adapter, self.path_parameters)

    @property
    def serving_environments(self) -> Serving_environmentsRequestBuilder:
        """The REST endpoint/path used to list and create zero or more `ServingEnvironment` entities.  This path contains a `GET` and `POST` operation to perform the list and create tasks, respectively."""
        from .serving_environments.serving_environments_request_builder import (
            Serving_environmentsRequestBuilder,
        )

        return Serving_environmentsRequestBuilder(self.request_adapter, self.path_parameters)


