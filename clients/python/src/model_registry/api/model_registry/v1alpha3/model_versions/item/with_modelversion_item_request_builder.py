from __future__ import annotations

from typing import TYPE_CHECKING, Any

from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.serialization import ParsableFactory

if TYPE_CHECKING:
    from ......models.model_version import ModelVersion
    from ......models.model_version_update import ModelVersionUpdate
    from .artifacts.artifacts_request_builder import ArtifactsRequestBuilder

class WithModelversionItemRequestBuilder(BaseRequestBuilder):
    """The REST endpoint/path used to get, update, and delete single instances of an `ModelVersion`. This path contains `GET`, `PUT`, and `DELETE` operations used to perform the get, update, and delete tasks, respectively."""
    def __init__(self,request_adapter: RequestAdapter, path_parameters: str | dict[str, Any]) -> None:
        """Instantiates a new WithModelversionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None.
        """
        super().__init__(request_adapter, "{+baseurl}/api/model_registry/v1alpha3/model_versions/{modelversionId}", path_parameters)

    async def get(self,request_configuration: RequestConfiguration | None = None) -> ModelVersion | None:
        """Gets the details of a single instance of a `ModelVersion`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ModelVersion].
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.error import Error

        error_mapping: dict[str, ParsableFactory] = {
            "401": Error,
            "404": Error,
            "500": Error,
        }
        if not self.request_adapter:
            msg = "Http core is null"
            raise Exception(msg)
        from ......models.model_version import ModelVersion

        return await self.request_adapter.send_async(request_info, ModelVersion, error_mapping)

    async def patch(self,body: ModelVersionUpdate | None = None, request_configuration: RequestConfiguration | None = None) -> ModelVersion | None:
        """Updates an existing `ModelVersion`.
        param body: Represents a ModelVersion belonging to a RegisteredModel.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ModelVersion].
        """
        if not body:
            msg = "body cannot be null."
            raise TypeError(msg)
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.error import Error

        error_mapping: dict[str, ParsableFactory] = {
            "400": Error,
            "401": Error,
            "404": Error,
            "500": Error,
        }
        if not self.request_adapter:
            msg = "Http core is null"
            raise Exception(msg)
        from ......models.model_version import ModelVersion

        return await self.request_adapter.send_async(request_info, ModelVersion, error_mapping)

    def to_get_request_information(self,request_configuration: RequestConfiguration | None = None) -> RequestInformation:
        """Gets the details of a single instance of a `ModelVersion`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation.
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info

    def to_patch_request_information(self,body: ModelVersionUpdate | None = None, request_configuration: RequestConfiguration | None = None) -> RequestInformation:
        """Updates an existing `ModelVersion`.
        param body: Represents a ModelVersion belonging to a RegisteredModel.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation.
        """
        if not body:
            msg = "body cannot be null."
            raise TypeError(msg)
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info

    def with_url(self,raw_url: str | None = None) -> WithModelversionItemRequestBuilder:
        """Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithModelversionItemRequestBuilder.
        """
        if not raw_url:
            msg = "raw_url cannot be null."
            raise TypeError(msg)
        return WithModelversionItemRequestBuilder(self.request_adapter, raw_url)

    @property
    def artifacts(self) -> ArtifactsRequestBuilder:
        """The REST endpoint/path used to list and create zero or more `Artifact` entities for a `ModelVersion`.  This path contains a `GET` and `POST` operation to perform the list and create tasks, respectively."""
        from .artifacts.artifacts_request_builder import ArtifactsRequestBuilder

        return ArtifactsRequestBuilder(self.request_adapter, self.path_parameters)


