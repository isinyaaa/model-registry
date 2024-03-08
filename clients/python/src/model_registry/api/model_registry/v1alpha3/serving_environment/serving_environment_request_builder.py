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
    from .....models.serving_environment import ServingEnvironment

class Serving_environmentRequestBuilder(BaseRequestBuilder):
    """The REST endpoint/path used to search for a `ServingEnvironment` entity.  This path contains a `GET` operation to perform the find task."""
    def __init__(self,request_adapter: RequestAdapter, path_parameters: str | dict[str, Any]) -> None:
        """Instantiates a new Serving_environmentRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None.
        """
        super().__init__(request_adapter, "{+baseurl}/api/model_registry/v1alpha3/serving_environment{?externalId*,name*}", path_parameters)

    async def get(self,request_configuration: RequestConfiguration | None = None) -> ServingEnvironment | None:
        """Finds a `ServingEnvironment` entity that matches query parameters.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ServingEnvironment].
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.error import Error

        error_mapping: dict[str, ParsableFactory] = {
            "401": Error,
            "404": Error,
            "500": Error,
        }
        if not self.request_adapter:
            msg = "Http core is null"
            raise Exception(msg)
        from .....models.serving_environment import ServingEnvironment

        return await self.request_adapter.send_async(request_info, ServingEnvironment, error_mapping)

    def to_get_request_information(self,request_configuration: RequestConfiguration | None = None) -> RequestInformation:
        """Finds a `ServingEnvironment` entity that matches query parameters.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation.
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info

    def with_url(self,raw_url: str | None = None) -> Serving_environmentRequestBuilder:
        """Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: Serving_environmentRequestBuilder.
        """
        if not raw_url:
            msg = "raw_url cannot be null."
            raise TypeError(msg)
        return Serving_environmentRequestBuilder(self.request_adapter, raw_url)

    @dataclass
    class Serving_environmentRequestBuilderGetQueryParameters:
        """Finds a `ServingEnvironment` entity that matches query parameters."""
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
            if original_name == "name":
                return "name"
            return original_name

        # External ID of entity to search.
        external_id: str | None = None

        # Name of entity to search.
        name: str | None = None



