from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.serialization import ParsableFactory

if TYPE_CHECKING:
    from .......models.artifact import Artifact
    from .......models.base_resource_list import BaseResourceList
    from .......models.order_by_field import OrderByField
    from .......models.sort_order import SortOrder

class ArtifactsRequestBuilder(BaseRequestBuilder):
    """The REST endpoint/path used to list and create zero or more `Artifact` entities for a `ModelVersion`.  This path contains a `GET` and `POST` operation to perform the list and create tasks, respectively."""
    def __init__(self,request_adapter: RequestAdapter, path_parameters: str | dict[str, Any]) -> None:
        """Instantiates a new ArtifactsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None.
        """
        super().__init__(request_adapter, "{+baseurl}/api/model_registry/v1alpha3/model_versions/{modelversionId}/artifacts{?externalId*,name*,nextPageToken*,orderBy*,pageSize*,sortOrder*}", path_parameters)

    async def get(self,request_configuration: RequestConfiguration | None = None) -> BaseResourceList | None:
        """List all artifacts associated with the `ModelVersion`
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BaseResourceList].
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.error import Error

        error_mapping: dict[str, ParsableFactory] = {
            "401": Error,
            "404": Error,
            "500": Error,
        }
        if not self.request_adapter:
            msg = "Http core is null"
            raise Exception(msg)
        from .......models.base_resource_list import BaseResourceList

        return await self.request_adapter.send_async(request_info, BaseResourceList, error_mapping)

    async def post(self,body: Artifact | None = None, request_configuration: RequestConfiguration | None = None) -> Artifact | None:
        """Creates a new instance of an Artifact if needed and associates it with `ModelVersion`.
        param body: A metadata Artifact Entity.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Artifact].
        """
        if not body:
            msg = "body cannot be null."
            raise TypeError(msg)
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .......models.error import Error

        error_mapping: dict[str, ParsableFactory] = {
            "400": Error,
            "401": Error,
            "404": Error,
            "500": Error,
        }
        if not self.request_adapter:
            msg = "Http core is null"
            raise Exception(msg)
        from .......models.artifact import Artifact

        return await self.request_adapter.send_async(request_info, Artifact, error_mapping)

    def to_get_request_information(self,request_configuration: RequestConfiguration | None = None) -> RequestInformation:
        """List all artifacts associated with the `ModelVersion`
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation.
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info

    def to_post_request_information(self,body: Artifact | None = None, request_configuration: RequestConfiguration | None = None) -> RequestInformation:
        """Creates a new instance of an Artifact if needed and associates it with `ModelVersion`.
        param body: A metadata Artifact Entity.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation.
        """
        if not body:
            msg = "body cannot be null."
            raise TypeError(msg)
        request_info = RequestInformation(Method.POST, "{+baseurl}/api/model_registry/v1alpha3/model_versions/{modelversionId}/artifacts", self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info

    def with_url(self,raw_url: str | None = None) -> ArtifactsRequestBuilder:
        """Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ArtifactsRequestBuilder.
        """
        if not raw_url:
            msg = "raw_url cannot be null."
            raise TypeError(msg)
        return ArtifactsRequestBuilder(self.request_adapter, raw_url)

    @dataclass
    class ArtifactsRequestBuilderGetQueryParameters:
        """List all artifacts associated with the `ModelVersion`."""
        def get_query_parameter(self,original_name: str | None = None) -> str:
            """Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str.
            """
            if not original_name:
                msg = "original_name cannot be null."
                raise TypeError(msg)
            if original_name == "external_id":
                return "externalId"
            if original_name == "next_page_token":
                return "nextPageToken"
            if original_name == "order_by":
                return "orderBy"
            if original_name == "page_size":
                return "pageSize"
            if original_name == "sort_order":
                return "sortOrder"
            if original_name == "name":
                return "name"
            return original_name

        # External ID of entity to search.
        external_id: str | None = None

        # Name of entity to search.
        name: str | None = None

        # Token to use to retrieve next page of results.
        next_page_token: str | None = None

        # Specifies the order by criteria for listing entities.
        order_by: OrderByField | None = None

        # Number of entities in each page.
        page_size: str | None = None

        # Specifies the sort order for listing entities, defaults to ASC.
        sort_order: SortOrder | None = None



