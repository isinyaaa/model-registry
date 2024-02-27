from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.error import Error
    from ......models.inference_service import InferenceService
    from ......models.inference_service_update import InferenceServiceUpdate
    from .model.model_request_builder import ModelRequestBuilder
    from .serves.serves_request_builder import ServesRequestBuilder
    from .version.version_request_builder import VersionRequestBuilder

class WithInferenceserviceItemRequestBuilder(BaseRequestBuilder):
    """
    The REST endpoint/path used to get, update, and delete single instances of an `InferenceService`. This path contains `GET`, `PUT`, and `DELETE` operations used to perform the get, update, and delete tasks, respectively.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new WithInferenceserviceItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/model_registry/v1alpha3/inference_services/{inferenceserviceId}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[InferenceService]:
        """
        Gets the details of a single instance of a `InferenceService`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[InferenceService]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.error import Error

        error_mapping: Dict[str, ParsableFactory] = {
            "401": Error,
            "404": Error,
            "500": Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.inference_service import InferenceService

        return await self.request_adapter.send_async(request_info, InferenceService, error_mapping)
    
    async def patch(self,body: Optional[InferenceServiceUpdate] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[InferenceService]:
        """
        Updates an existing `InferenceService`.
        param body: An `InferenceService` entity in a `ServingEnvironment` represents a deployed `ModelVersion` from a `RegisteredModel` created by Model Serving.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[InferenceService]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.error import Error

        error_mapping: Dict[str, ParsableFactory] = {
            "400": Error,
            "401": Error,
            "404": Error,
            "500": Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.inference_service import InferenceService

        return await self.request_adapter.send_async(request_info, InferenceService, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Gets the details of a single instance of a `InferenceService`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[InferenceServiceUpdate] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Updates an existing `InferenceService`.
        param body: An `InferenceService` entity in a `ServingEnvironment` represents a deployed `ModelVersion` from a `RegisteredModel` created by Model Serving.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> WithInferenceserviceItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithInferenceserviceItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return WithInferenceserviceItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def model(self) -> ModelRequestBuilder:
        """
        The REST endpoint/path used to list the `RegisteredModel` entity for an `InferenceService`.  This path contains a `GET` operation to perform the get task.
        """
        from .model.model_request_builder import ModelRequestBuilder

        return ModelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def serves(self) -> ServesRequestBuilder:
        """
        The REST endpoint/path used to list and create zero or more `ServeModel` entities for a `InferenceService`.  This path contains a `GET` and `POST` operation to perform the list and create tasks, respectively.
        """
        from .serves.serves_request_builder import ServesRequestBuilder

        return ServesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def version(self) -> VersionRequestBuilder:
        """
        The REST endpoint/path used to get the current `ModelVersion` entity for a `InferenceService`. This path contains a `GET` operation to perform the get task.
        """
        from .version.version_request_builder import VersionRequestBuilder

        return VersionRequestBuilder(self.request_adapter, self.path_parameters)
    

