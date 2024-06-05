package converter

import "github.com/kubeflow/model-registry/pkg/openapi"

// NOTE: methods must follow these patterns, otherwise tests could not find possible issues:
// Converters createEntity to entity: Convert<ENTITY>Create
// Converters updateEntity to entity: Convert<ENTITY>Update
// Converters override fields entity: OverrideNotEditableFor<ENTITY>

// goverter:converter
// goverter:output:file ./generated/openapi_converter.gen.go
// goverter:wrapErrors
// goverter:enum:unknown @error
// goverter:matchIgnoreCase
// goverter:useZeroValueOnPointerInconsistency
type OpenAPIConverter interface {
	// goverter:ignore Id CreateTimeSinceEpoch LastUpdateTimeSinceEpoch
	ConvertRegisteredModelCreate(source *openapi.RegisteredModelCreate) (*openapi.RegisteredModel, error)

	// goverter:ignore Id CreateTimeSinceEpoch LastUpdateTimeSinceEpoch Name
	ConvertRegisteredModelUpdate(source *openapi.RegisteredModelUpdate) (*openapi.RegisteredModel, error)

	// goverter:ignore Id CreateTimeSinceEpoch LastUpdateTimeSinceEpoch
	ConvertModelVersionCreate(source *openapi.ModelVersionCreate) (*openapi.ModelVersion, error)

	// goverter:ignore Id CreateTimeSinceEpoch LastUpdateTimeSinceEpoch Name RegisteredModelId
	ConvertModelVersionUpdate(source *openapi.ModelVersionUpdate) (*openapi.ModelVersion, error)

	// goverter:ignore Id CreateTimeSinceEpoch LastUpdateTimeSinceEpoch ArtifactType
	ConvertModelArtifactCreate(source *openapi.ModelArtifactCreate) (*openapi.ModelArtifact, error)

	// goverter:ignore Id CreateTimeSinceEpoch LastUpdateTimeSinceEpoch ArtifactType Name
	ConvertModelArtifactUpdate(source *openapi.ModelArtifactUpdate) (*openapi.ModelArtifact, error)

	// goverter:ignore Id CreateTimeSinceEpoch LastUpdateTimeSinceEpoch
	ConvertServingEnvironmentCreate(source *openapi.ServingEnvironmentCreate) (*openapi.ServingEnvironment, error)

	// goverter:ignore Id CreateTimeSinceEpoch LastUpdateTimeSinceEpoch Name
	ConvertServingEnvironmentUpdate(source *openapi.ServingEnvironmentUpdate) (*openapi.ServingEnvironment, error)

	// goverter:ignore Id CreateTimeSinceEpoch LastUpdateTimeSinceEpoch
	ConvertInferenceServiceCreate(source *openapi.InferenceServiceCreate) (*openapi.InferenceService, error)

	// goverter:ignore Id CreateTimeSinceEpoch LastUpdateTimeSinceEpoch Name RegisteredModelId ServingEnvironmentId
	ConvertInferenceServiceUpdate(source *openapi.InferenceServiceUpdate) (*openapi.InferenceService, error)

	// goverter:ignore Id CreateTimeSinceEpoch LastUpdateTimeSinceEpoch
	ConvertServeModelCreate(source *openapi.ServeModelCreate) (*openapi.ServeModel, error)

	// goverter:ignore Id CreateTimeSinceEpoch LastUpdateTimeSinceEpoch Name ModelVersionId
	ConvertServeModelUpdate(source *openapi.ServeModelUpdate) (*openapi.ServeModel, error)

	// Update all fields that ARE editable
	// goverter:default InitWithExisting
	// goverter:autoMap Update
	// goverter:ignore Id Name CreateTimeSinceEpoch LastUpdateTimeSinceEpoch
	OverrideEditableForRegisteredModel(source OpenapiUpdateWrapper[openapi.RegisteredModel]) (openapi.RegisteredModel, error)

	// Update all fields that ARE editable
	// goverter:default InitWithExisting
	// goverter:autoMap Update
	// goverter:ignore Id Name CreateTimeSinceEpoch LastUpdateTimeSinceEpoch RegisteredModelId
	OverrideEditableForModelVersion(source OpenapiUpdateWrapper[openapi.ModelVersion]) (openapi.ModelVersion, error)

	// Update all fields that ARE editable
	// goverter:default InitWithExisting
	// goverter:autoMap Update
	// goverter:ignore Id Name CreateTimeSinceEpoch LastUpdateTimeSinceEpoch
	OverrideEditableForDocArtifact(source OpenapiUpdateWrapper[openapi.DocArtifact]) (openapi.DocArtifact, error)

	// Update all fields that ARE editable
	// goverter:default InitWithExisting
	// goverter:autoMap Update
	// goverter:ignore Id Name CreateTimeSinceEpoch LastUpdateTimeSinceEpoch
	OverrideEditableForModelArtifact(source OpenapiUpdateWrapper[openapi.ModelArtifact]) (openapi.ModelArtifact, error)

	// Update all fields that ARE editable
	// goverter:default InitWithExisting
	// goverter:autoMap Update
	// goverter:ignore Id Name CreateTimeSinceEpoch LastUpdateTimeSinceEpoch
	OverrideEditableForServingEnvironment(source OpenapiUpdateWrapper[openapi.ServingEnvironment]) (openapi.ServingEnvironment, error)

	// Update all fields that ARE editable
	// goverter:default InitWithExisting
	// goverter:autoMap Update
	// goverter:ignore Id Name CreateTimeSinceEpoch LastUpdateTimeSinceEpoch RegisteredModelId
	OverrideEditableForInferenceService(source OpenapiUpdateWrapper[openapi.InferenceService]) (openapi.InferenceService, error)

	// Update all fields that ARE editable
	// goverter:default InitWithExisting
	// goverter:autoMap Update
	// goverter:ignore Id Name CreateTimeSinceEpoch LastUpdateTimeSinceEpoch ModelVersionId
	OverrideEditableForServeModel(source OpenapiUpdateWrapper[openapi.ServeModel]) (openapi.ServeModel, error)
}
