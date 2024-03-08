from __future__ import annotations

from typing import TYPE_CHECKING, Any

from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.request_adapter import RequestAdapter

if TYPE_CHECKING:
    from .model_registry.model_registry_request_builder import (
        Model_registryRequestBuilder,
    )

class ApiRequestBuilder(BaseRequestBuilder):
    """Builds and executes requests for operations under /api."""
    def __init__(self,request_adapter: RequestAdapter, path_parameters: str | dict[str, Any]) -> None:
        """Instantiates a new ApiRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None.
        """
        super().__init__(request_adapter, "{+baseurl}/api", path_parameters)

    @property
    def model_registry(self) -> Model_registryRequestBuilder:
        """The model_registry property."""
        from .model_registry.model_registry_request_builder import (
            Model_registryRequestBuilder,
        )

        return Model_registryRequestBuilder(self.request_adapter, self.path_parameters)


