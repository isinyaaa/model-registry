from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.serialization import ParsableFactory

if TYPE_CHECKING:
    from .....models.base_resource_list import BaseResourceList
    from .....models.model_artifact import ModelArtifact
    from .....models.model_artifact_create import ModelArtifactCreate
    from .....models.order_by_field import OrderByField
    from .....models.sort_order import SortOrder
    from .item.with_modelartifact_item_request_builder import (
        WithModelartifactItemRequestBuilder,
    )

class Model_artifactsRequestBuilder(BaseRequestBuilder):
    """The REST endpoint/path used to list and create zero or more `ModelArtifact` entities.  This path contains a `GET` and `POST` operation to perform the list and create tasks, respectively."""
    def __init__(self,request_adapter: RequestAdapter, path_parameters: str | dict[str, Any]) -> None:
        """Instantiates a new Model_artifactsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None.
        """
        super().__init__(request_adapter, "{+baseurl}/api/model_registry/v1alpha3/model_artifacts{?nextPageToken*,orderBy*,pageSize*,sortOrder*}", path_parameters)

    def by_modelartifact_id(self,modelartifact_id: str) -> WithModelartifactItemRequestBuilder:
        """The REST endpoint/path used to get, update, and delete single instances of an `ModelArtifact`. This path contains `GET`, `PUT`, and `DELETE` operations used to perform the get, update, and delete tasks, respectively.
        param modelartifact_id: A unique identifier for a `ModelArtifact`.
        Returns: WithModelartifactItemRequestBuilder.
        """
        if not modelartifact_id:
            msg = "modelartifact_id cannot be null."
            raise TypeError(msg)
        from .item.with_modelartifact_item_request_builder import (
            WithModelartifactItemRequestBuilder,
        )

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["modelartifactId"] = modelartifact_id
        return WithModelartifactItemRequestBuilder(self.request_adapter, url_tpl_params)

    async def get(self,request_configuration: RequestConfiguration | None = None) -> BaseResourceList | None:
        """Gets a list of all `ModelArtifact` entities.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BaseResourceList].
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.error import Error

        error_mapping: dict[str, ParsableFactory] = {
            "400": Error,
            "401": Error,
            "404": Error,
            "500": Error,
        }
        if not self.request_adapter:
            msg = "Http core is null"
            raise Exception(msg)
        from .....models.base_resource_list import BaseResourceList

        return await self.request_adapter.send_async(request_info, BaseResourceList, error_mapping)

    async def post(self,body: ModelArtifactCreate | None = None, request_configuration: RequestConfiguration | None = None) -> ModelArtifact | None:
        """Creates a new instance of a `ModelArtifact`.
        param body: An ML model artifact.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ModelArtifact].
        """
        if not body:
            msg = "body cannot be null."
            raise TypeError(msg)
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.error import Error

        error_mapping: dict[str, ParsableFactory] = {
            "400": Error,
            "401": Error,
            "500": Error,
        }
        if not self.request_adapter:
            msg = "Http core is null"
            raise Exception(msg)
        from .....models.model_artifact import ModelArtifact

        return await self.request_adapter.send_async(request_info, ModelArtifact, error_mapping)

    def to_get_request_information(self,request_configuration: RequestConfiguration | None = None) -> RequestInformation:
        """Gets a list of all `ModelArtifact` entities.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation.
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info

    def to_post_request_information(self,body: ModelArtifactCreate | None = None, request_configuration: RequestConfiguration | None = None) -> RequestInformation:
        """Creates a new instance of a `ModelArtifact`.
        param body: An ML model artifact.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation.
        """
        if not body:
            msg = "body cannot be null."
            raise TypeError(msg)
        request_info = RequestInformation(Method.POST, "{+baseurl}/api/model_registry/v1alpha3/model_artifacts", self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info

    def with_url(self,raw_url: str | None = None) -> Model_artifactsRequestBuilder:
        """Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: Model_artifactsRequestBuilder.
        """
        if not raw_url:
            msg = "raw_url cannot be null."
            raise TypeError(msg)
        return Model_artifactsRequestBuilder(self.request_adapter, raw_url)

    @dataclass
    class Model_artifactsRequestBuilderGetQueryParameters:
        """Gets a list of all `ModelArtifact` entities."""
        def get_query_parameter(self,original_name: str | None = None) -> str:
            """Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str.
            """
            if not original_name:
                msg = "original_name cannot be null."
                raise TypeError(msg)
            if original_name == "next_page_token":
                return "nextPageToken"
            if original_name == "order_by":
                return "orderBy"
            if original_name == "page_size":
                return "pageSize"
            if original_name == "sort_order":
                return "sortOrder"
            return original_name

        # Token to use to retrieve next page of results.
        next_page_token: str | None = None

        # Specifies the order by criteria for listing entities.
        order_by: OrderByField | None = None

        # Number of entities in each page.
        page_size: str | None = None

        # Specifies the sort order for listing entities, defaults to ASC.
        sort_order: SortOrder | None = None



