/*
Model Registry REST API

REST API for Model Registry to create and manage ML model metadata

API version: v1alpha3
*/

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package openapi

import (
	"encoding/json"
)

// checks if the ServeModel type satisfies the MappedNullable interface at compile time
var _ MappedNullable = &ServeModel{}

// ServeModel An ML model serving action.
type ServeModel struct {
	LastKnownState *ExecutionState `json:"lastKnownState,omitempty"`
	// User provided custom properties which are not defined by its type.
	CustomProperties *map[string]MetadataValue `json:"customProperties,omitempty"`
	// An optional description about the resource.
	Description *string `json:"description,omitempty"`
	// The external id that come from the clients’ system. This field is optional. If set, it must be unique among all resources within a database instance.
	ExternalId *string `json:"externalId,omitempty"`
	// The client provided name of the artifact. This field is optional. If set, it must be unique among all the artifacts of the same artifact type within a database instance and cannot be changed once set.
	Name *string `json:"name,omitempty"`
	// Output only. The unique server generated id of the resource.
	Id *string `json:"id,omitempty"`
	// Output only. Create time of the resource in millisecond since epoch.
	CreateTimeSinceEpoch *string `json:"createTimeSinceEpoch,omitempty"`
	// Output only. Last update time of the resource since epoch in millisecond since epoch.
	LastUpdateTimeSinceEpoch *string `json:"lastUpdateTimeSinceEpoch,omitempty"`
	// ID of the `ModelVersion` that was served in `InferenceService`.
	ModelVersionId string `json:"modelVersionId"`
}

// NewServeModel instantiates a new ServeModel object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewServeModel(modelVersionId string) *ServeModel {
	this := ServeModel{}
	var lastKnownState ExecutionState = EXECUTIONSTATE_UNKNOWN
	this.LastKnownState = &lastKnownState
	this.ModelVersionId = modelVersionId
	return &this
}

// NewServeModelWithDefaults instantiates a new ServeModel object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewServeModelWithDefaults() *ServeModel {
	this := ServeModel{}
	var lastKnownState ExecutionState = EXECUTIONSTATE_UNKNOWN
	this.LastKnownState = &lastKnownState
	return &this
}

// GetLastKnownState returns the LastKnownState field value if set, zero value otherwise.
func (o *ServeModel) GetLastKnownState() ExecutionState {
	if o == nil || IsNil(o.LastKnownState) {
		var ret ExecutionState
		return ret
	}
	return *o.LastKnownState
}

// GetLastKnownStateOk returns a tuple with the LastKnownState field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ServeModel) GetLastKnownStateOk() (*ExecutionState, bool) {
	if o == nil || IsNil(o.LastKnownState) {
		return nil, false
	}
	return o.LastKnownState, true
}

// HasLastKnownState returns a boolean if a field has been set.
func (o *ServeModel) HasLastKnownState() bool {
	if o != nil && !IsNil(o.LastKnownState) {
		return true
	}

	return false
}

// SetLastKnownState gets a reference to the given ExecutionState and assigns it to the LastKnownState field.
func (o *ServeModel) SetLastKnownState(v ExecutionState) {
	o.LastKnownState = &v
}

// GetCustomProperties returns the CustomProperties field value if set, zero value otherwise.
func (o *ServeModel) GetCustomProperties() map[string]MetadataValue {
	if o == nil || IsNil(o.CustomProperties) {
		var ret map[string]MetadataValue
		return ret
	}
	return *o.CustomProperties
}

// GetCustomPropertiesOk returns a tuple with the CustomProperties field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ServeModel) GetCustomPropertiesOk() (*map[string]MetadataValue, bool) {
	if o == nil || IsNil(o.CustomProperties) {
		return nil, false
	}
	return o.CustomProperties, true
}

// HasCustomProperties returns a boolean if a field has been set.
func (o *ServeModel) HasCustomProperties() bool {
	if o != nil && !IsNil(o.CustomProperties) {
		return true
	}

	return false
}

// SetCustomProperties gets a reference to the given map[string]MetadataValue and assigns it to the CustomProperties field.
func (o *ServeModel) SetCustomProperties(v map[string]MetadataValue) {
	o.CustomProperties = &v
}

// GetDescription returns the Description field value if set, zero value otherwise.
func (o *ServeModel) GetDescription() string {
	if o == nil || IsNil(o.Description) {
		var ret string
		return ret
	}
	return *o.Description
}

// GetDescriptionOk returns a tuple with the Description field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ServeModel) GetDescriptionOk() (*string, bool) {
	if o == nil || IsNil(o.Description) {
		return nil, false
	}
	return o.Description, true
}

// HasDescription returns a boolean if a field has been set.
func (o *ServeModel) HasDescription() bool {
	if o != nil && !IsNil(o.Description) {
		return true
	}

	return false
}

// SetDescription gets a reference to the given string and assigns it to the Description field.
func (o *ServeModel) SetDescription(v string) {
	o.Description = &v
}

// GetExternalId returns the ExternalId field value if set, zero value otherwise.
func (o *ServeModel) GetExternalId() string {
	if o == nil || IsNil(o.ExternalId) {
		var ret string
		return ret
	}
	return *o.ExternalId
}

// GetExternalIdOk returns a tuple with the ExternalId field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ServeModel) GetExternalIdOk() (*string, bool) {
	if o == nil || IsNil(o.ExternalId) {
		return nil, false
	}
	return o.ExternalId, true
}

// HasExternalId returns a boolean if a field has been set.
func (o *ServeModel) HasExternalId() bool {
	if o != nil && !IsNil(o.ExternalId) {
		return true
	}

	return false
}

// SetExternalId gets a reference to the given string and assigns it to the ExternalId field.
func (o *ServeModel) SetExternalId(v string) {
	o.ExternalId = &v
}

// GetName returns the Name field value if set, zero value otherwise.
func (o *ServeModel) GetName() string {
	if o == nil || IsNil(o.Name) {
		var ret string
		return ret
	}
	return *o.Name
}

// GetNameOk returns a tuple with the Name field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ServeModel) GetNameOk() (*string, bool) {
	if o == nil || IsNil(o.Name) {
		return nil, false
	}
	return o.Name, true
}

// HasName returns a boolean if a field has been set.
func (o *ServeModel) HasName() bool {
	if o != nil && !IsNil(o.Name) {
		return true
	}

	return false
}

// SetName gets a reference to the given string and assigns it to the Name field.
func (o *ServeModel) SetName(v string) {
	o.Name = &v
}

// GetId returns the Id field value if set, zero value otherwise.
func (o *ServeModel) GetId() string {
	if o == nil || IsNil(o.Id) {
		var ret string
		return ret
	}
	return *o.Id
}

// GetIdOk returns a tuple with the Id field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ServeModel) GetIdOk() (*string, bool) {
	if o == nil || IsNil(o.Id) {
		return nil, false
	}
	return o.Id, true
}

// HasId returns a boolean if a field has been set.
func (o *ServeModel) HasId() bool {
	if o != nil && !IsNil(o.Id) {
		return true
	}

	return false
}

// SetId gets a reference to the given string and assigns it to the Id field.
func (o *ServeModel) SetId(v string) {
	o.Id = &v
}

// GetCreateTimeSinceEpoch returns the CreateTimeSinceEpoch field value if set, zero value otherwise.
func (o *ServeModel) GetCreateTimeSinceEpoch() string {
	if o == nil || IsNil(o.CreateTimeSinceEpoch) {
		var ret string
		return ret
	}
	return *o.CreateTimeSinceEpoch
}

// GetCreateTimeSinceEpochOk returns a tuple with the CreateTimeSinceEpoch field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ServeModel) GetCreateTimeSinceEpochOk() (*string, bool) {
	if o == nil || IsNil(o.CreateTimeSinceEpoch) {
		return nil, false
	}
	return o.CreateTimeSinceEpoch, true
}

// HasCreateTimeSinceEpoch returns a boolean if a field has been set.
func (o *ServeModel) HasCreateTimeSinceEpoch() bool {
	if o != nil && !IsNil(o.CreateTimeSinceEpoch) {
		return true
	}

	return false
}

// SetCreateTimeSinceEpoch gets a reference to the given string and assigns it to the CreateTimeSinceEpoch field.
func (o *ServeModel) SetCreateTimeSinceEpoch(v string) {
	o.CreateTimeSinceEpoch = &v
}

// GetLastUpdateTimeSinceEpoch returns the LastUpdateTimeSinceEpoch field value if set, zero value otherwise.
func (o *ServeModel) GetLastUpdateTimeSinceEpoch() string {
	if o == nil || IsNil(o.LastUpdateTimeSinceEpoch) {
		var ret string
		return ret
	}
	return *o.LastUpdateTimeSinceEpoch
}

// GetLastUpdateTimeSinceEpochOk returns a tuple with the LastUpdateTimeSinceEpoch field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ServeModel) GetLastUpdateTimeSinceEpochOk() (*string, bool) {
	if o == nil || IsNil(o.LastUpdateTimeSinceEpoch) {
		return nil, false
	}
	return o.LastUpdateTimeSinceEpoch, true
}

// HasLastUpdateTimeSinceEpoch returns a boolean if a field has been set.
func (o *ServeModel) HasLastUpdateTimeSinceEpoch() bool {
	if o != nil && !IsNil(o.LastUpdateTimeSinceEpoch) {
		return true
	}

	return false
}

// SetLastUpdateTimeSinceEpoch gets a reference to the given string and assigns it to the LastUpdateTimeSinceEpoch field.
func (o *ServeModel) SetLastUpdateTimeSinceEpoch(v string) {
	o.LastUpdateTimeSinceEpoch = &v
}

// GetModelVersionId returns the ModelVersionId field value
func (o *ServeModel) GetModelVersionId() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.ModelVersionId
}

// GetModelVersionIdOk returns a tuple with the ModelVersionId field value
// and a boolean to check if the value has been set.
func (o *ServeModel) GetModelVersionIdOk() (*string, bool) {
	if o == nil {
		return nil, false
	}
	return &o.ModelVersionId, true
}

// SetModelVersionId sets field value
func (o *ServeModel) SetModelVersionId(v string) {
	o.ModelVersionId = v
}

func (o ServeModel) MarshalJSON() ([]byte, error) {
	toSerialize, err := o.ToMap()
	if err != nil {
		return []byte{}, err
	}
	return json.Marshal(toSerialize)
}

func (o ServeModel) ToMap() (map[string]interface{}, error) {
	toSerialize := map[string]interface{}{}
	if !IsNil(o.LastKnownState) {
		toSerialize["lastKnownState"] = o.LastKnownState
	}
	if !IsNil(o.CustomProperties) {
		toSerialize["customProperties"] = o.CustomProperties
	}
	if !IsNil(o.Description) {
		toSerialize["description"] = o.Description
	}
	if !IsNil(o.ExternalId) {
		toSerialize["externalId"] = o.ExternalId
	}
	if !IsNil(o.Name) {
		toSerialize["name"] = o.Name
	}
	if !IsNil(o.Id) {
		toSerialize["id"] = o.Id
	}
	if !IsNil(o.CreateTimeSinceEpoch) {
		toSerialize["createTimeSinceEpoch"] = o.CreateTimeSinceEpoch
	}
	if !IsNil(o.LastUpdateTimeSinceEpoch) {
		toSerialize["lastUpdateTimeSinceEpoch"] = o.LastUpdateTimeSinceEpoch
	}
	toSerialize["modelVersionId"] = o.ModelVersionId
	return toSerialize, nil
}

type NullableServeModel struct {
	value *ServeModel
	isSet bool
}

func (v NullableServeModel) Get() *ServeModel {
	return v.value
}

func (v *NullableServeModel) Set(val *ServeModel) {
	v.value = val
	v.isSet = true
}

func (v NullableServeModel) IsSet() bool {
	return v.isSet
}

func (v *NullableServeModel) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableServeModel(val *ServeModel) *NullableServeModel {
	return &NullableServeModel{value: val, isSet: true}
}

func (v NullableServeModel) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableServeModel) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}
