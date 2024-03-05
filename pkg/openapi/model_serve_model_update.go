/*
Model Registry REST API

REST API for Model Registry to create and manage ML model metadata

API version: v1alpha2
*/

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package openapi

import (
	"encoding/json"
)

// checks if the ServeModelUpdate type satisfies the MappedNullable interface at compile time
var _ MappedNullable = &ServeModelUpdate{}

// ServeModelUpdate An ML model serving action.
type ServeModelUpdate struct {
	LastKnownState *ExecutionState `json:"lastKnownState,omitempty"`
	// User provided custom properties which are not defined by its type.
	CustomProperties *map[string]MetadataValue `json:"customProperties,omitempty"`
	// An optional description about the resource.
	Description *string `json:"description,omitempty"`
	// The external id that come from the clients’ system. This field is optional. If set, it must be unique among all resources within a database instance.
	ExternalId *string `json:"externalId,omitempty"`
}

// NewServeModelUpdate instantiates a new ServeModelUpdate object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewServeModelUpdate() *ServeModelUpdate {
	this := ServeModelUpdate{}
	var lastKnownState ExecutionState = EXECUTIONSTATE_UNKNOWN
	this.LastKnownState = &lastKnownState
	return &this
}

// NewServeModelUpdateWithDefaults instantiates a new ServeModelUpdate object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewServeModelUpdateWithDefaults() *ServeModelUpdate {
	this := ServeModelUpdate{}
	var lastKnownState ExecutionState = EXECUTIONSTATE_UNKNOWN
	this.LastKnownState = &lastKnownState
	return &this
}

// GetLastKnownState returns the LastKnownState field value if set, zero value otherwise.
func (o *ServeModelUpdate) GetLastKnownState() ExecutionState {
	if o == nil || IsNil(o.LastKnownState) {
		var ret ExecutionState
		return ret
	}
	return *o.LastKnownState
}

// GetLastKnownStateOk returns a tuple with the LastKnownState field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ServeModelUpdate) GetLastKnownStateOk() (*ExecutionState, bool) {
	if o == nil || IsNil(o.LastKnownState) {
		return nil, false
	}
	return o.LastKnownState, true
}

// HasLastKnownState returns a boolean if a field has been set.
func (o *ServeModelUpdate) HasLastKnownState() bool {
	if o != nil && !IsNil(o.LastKnownState) {
		return true
	}

	return false
}

// SetLastKnownState gets a reference to the given ExecutionState and assigns it to the LastKnownState field.
func (o *ServeModelUpdate) SetLastKnownState(v ExecutionState) {
	o.LastKnownState = &v
}

// GetCustomProperties returns the CustomProperties field value if set, zero value otherwise.
func (o *ServeModelUpdate) GetCustomProperties() map[string]MetadataValue {
	if o == nil || IsNil(o.CustomProperties) {
		var ret map[string]MetadataValue
		return ret
	}
	return *o.CustomProperties
}

// GetCustomPropertiesOk returns a tuple with the CustomProperties field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ServeModelUpdate) GetCustomPropertiesOk() (*map[string]MetadataValue, bool) {
	if o == nil || IsNil(o.CustomProperties) {
		return nil, false
	}
	return o.CustomProperties, true
}

// HasCustomProperties returns a boolean if a field has been set.
func (o *ServeModelUpdate) HasCustomProperties() bool {
	if o != nil && !IsNil(o.CustomProperties) {
		return true
	}

	return false
}

// SetCustomProperties gets a reference to the given map[string]MetadataValue and assigns it to the CustomProperties field.
func (o *ServeModelUpdate) SetCustomProperties(v map[string]MetadataValue) {
	o.CustomProperties = &v
}

// GetDescription returns the Description field value if set, zero value otherwise.
func (o *ServeModelUpdate) GetDescription() string {
	if o == nil || IsNil(o.Description) {
		var ret string
		return ret
	}
	return *o.Description
}

// GetDescriptionOk returns a tuple with the Description field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ServeModelUpdate) GetDescriptionOk() (*string, bool) {
	if o == nil || IsNil(o.Description) {
		return nil, false
	}
	return o.Description, true
}

// HasDescription returns a boolean if a field has been set.
func (o *ServeModelUpdate) HasDescription() bool {
	if o != nil && !IsNil(o.Description) {
		return true
	}

	return false
}

// SetDescription gets a reference to the given string and assigns it to the Description field.
func (o *ServeModelUpdate) SetDescription(v string) {
	o.Description = &v
}

// GetExternalId returns the ExternalId field value if set, zero value otherwise.
func (o *ServeModelUpdate) GetExternalId() string {
	if o == nil || IsNil(o.ExternalId) {
		var ret string
		return ret
	}
	return *o.ExternalId
}

// GetExternalIdOk returns a tuple with the ExternalId field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ServeModelUpdate) GetExternalIdOk() (*string, bool) {
	if o == nil || IsNil(o.ExternalId) {
		return nil, false
	}
	return o.ExternalId, true
}

// HasExternalId returns a boolean if a field has been set.
func (o *ServeModelUpdate) HasExternalId() bool {
	if o != nil && !IsNil(o.ExternalId) {
		return true
	}

	return false
}

// SetExternalId gets a reference to the given string and assigns it to the ExternalId field.
func (o *ServeModelUpdate) SetExternalId(v string) {
	o.ExternalId = &v
}

func (o ServeModelUpdate) MarshalJSON() ([]byte, error) {
	toSerialize, err := o.ToMap()
	if err != nil {
		return []byte{}, err
	}
	return json.Marshal(toSerialize)
}

func (o ServeModelUpdate) ToMap() (map[string]interface{}, error) {
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
	return toSerialize, nil
}

type NullableServeModelUpdate struct {
	value *ServeModelUpdate
	isSet bool
}

func (v NullableServeModelUpdate) Get() *ServeModelUpdate {
	return v.value
}

func (v *NullableServeModelUpdate) Set(val *ServeModelUpdate) {
	v.value = val
	v.isSet = true
}

func (v NullableServeModelUpdate) IsSet() bool {
	return v.isSet
}

func (v *NullableServeModelUpdate) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableServeModelUpdate(val *ServeModelUpdate) *NullableServeModelUpdate {
	return &NullableServeModelUpdate{value: val, isSet: true}
}

func (v NullableServeModelUpdate) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableServeModelUpdate) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}
