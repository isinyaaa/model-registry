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

// checks if the ModelVersion type satisfies the MappedNullable interface at compile time
var _ MappedNullable = &ModelVersion{}

// ModelVersion Represents a ModelVersion belonging to a RegisteredModel.
type ModelVersion struct {
	// User provided custom properties which are not defined by its type.
	CustomProperties *map[string]MetadataValue `json:"customProperties,omitempty"`
	// An optional description about the resource.
	Description *string `json:"description,omitempty"`
	// The external id that come from the clients’ system. This field is optional. If set, it must be unique among all resources within a database instance.
	ExternalId *string `json:"externalId,omitempty"`
	// The client provided name of the artifact. This field is optional. If set, it must be unique among all the artifacts of the same artifact type within a database instance and cannot be changed once set.
	Name  *string            `json:"name,omitempty"`
	State *ModelVersionState `json:"state,omitempty"`
	// Name of the author.
	Author *string `json:"author,omitempty"`
	// Output only. The unique server generated id of the resource.
	Id *string `json:"id,omitempty"`
	// Output only. Create time of the resource in millisecond since epoch.
	CreateTimeSinceEpoch *string `json:"createTimeSinceEpoch,omitempty"`
	// Output only. Last update time of the resource since epoch in millisecond since epoch.
	LastUpdateTimeSinceEpoch *string `json:"lastUpdateTimeSinceEpoch,omitempty"`
}

// NewModelVersion instantiates a new ModelVersion object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewModelVersion() *ModelVersion {
	this := ModelVersion{}
	var state ModelVersionState = MODELVERSIONSTATE_LIVE
	this.State = &state
	return &this
}

// NewModelVersionWithDefaults instantiates a new ModelVersion object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewModelVersionWithDefaults() *ModelVersion {
	this := ModelVersion{}
	var state ModelVersionState = MODELVERSIONSTATE_LIVE
	this.State = &state
	return &this
}

// GetCustomProperties returns the CustomProperties field value if set, zero value otherwise.
func (o *ModelVersion) GetCustomProperties() map[string]MetadataValue {
	if o == nil || IsNil(o.CustomProperties) {
		var ret map[string]MetadataValue
		return ret
	}
	return *o.CustomProperties
}

// GetCustomPropertiesOk returns a tuple with the CustomProperties field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ModelVersion) GetCustomPropertiesOk() (*map[string]MetadataValue, bool) {
	if o == nil || IsNil(o.CustomProperties) {
		return nil, false
	}
	return o.CustomProperties, true
}

// HasCustomProperties returns a boolean if a field has been set.
func (o *ModelVersion) HasCustomProperties() bool {
	if o != nil && !IsNil(o.CustomProperties) {
		return true
	}

	return false
}

// SetCustomProperties gets a reference to the given map[string]MetadataValue and assigns it to the CustomProperties field.
func (o *ModelVersion) SetCustomProperties(v map[string]MetadataValue) {
	o.CustomProperties = &v
}

// GetDescription returns the Description field value if set, zero value otherwise.
func (o *ModelVersion) GetDescription() string {
	if o == nil || IsNil(o.Description) {
		var ret string
		return ret
	}
	return *o.Description
}

// GetDescriptionOk returns a tuple with the Description field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ModelVersion) GetDescriptionOk() (*string, bool) {
	if o == nil || IsNil(o.Description) {
		return nil, false
	}
	return o.Description, true
}

// HasDescription returns a boolean if a field has been set.
func (o *ModelVersion) HasDescription() bool {
	if o != nil && !IsNil(o.Description) {
		return true
	}

	return false
}

// SetDescription gets a reference to the given string and assigns it to the Description field.
func (o *ModelVersion) SetDescription(v string) {
	o.Description = &v
}

// GetExternalId returns the ExternalId field value if set, zero value otherwise.
func (o *ModelVersion) GetExternalId() string {
	if o == nil || IsNil(o.ExternalId) {
		var ret string
		return ret
	}
	return *o.ExternalId
}

// GetExternalIdOk returns a tuple with the ExternalId field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ModelVersion) GetExternalIdOk() (*string, bool) {
	if o == nil || IsNil(o.ExternalId) {
		return nil, false
	}
	return o.ExternalId, true
}

// HasExternalId returns a boolean if a field has been set.
func (o *ModelVersion) HasExternalId() bool {
	if o != nil && !IsNil(o.ExternalId) {
		return true
	}

	return false
}

// SetExternalId gets a reference to the given string and assigns it to the ExternalId field.
func (o *ModelVersion) SetExternalId(v string) {
	o.ExternalId = &v
}

// GetName returns the Name field value if set, zero value otherwise.
func (o *ModelVersion) GetName() string {
	if o == nil || IsNil(o.Name) {
		var ret string
		return ret
	}
	return *o.Name
}

// GetNameOk returns a tuple with the Name field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ModelVersion) GetNameOk() (*string, bool) {
	if o == nil || IsNil(o.Name) {
		return nil, false
	}
	return o.Name, true
}

// HasName returns a boolean if a field has been set.
func (o *ModelVersion) HasName() bool {
	if o != nil && !IsNil(o.Name) {
		return true
	}

	return false
}

// SetName gets a reference to the given string and assigns it to the Name field.
func (o *ModelVersion) SetName(v string) {
	o.Name = &v
}

// GetState returns the State field value if set, zero value otherwise.
func (o *ModelVersion) GetState() ModelVersionState {
	if o == nil || IsNil(o.State) {
		var ret ModelVersionState
		return ret
	}
	return *o.State
}

// GetStateOk returns a tuple with the State field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ModelVersion) GetStateOk() (*ModelVersionState, bool) {
	if o == nil || IsNil(o.State) {
		return nil, false
	}
	return o.State, true
}

// HasState returns a boolean if a field has been set.
func (o *ModelVersion) HasState() bool {
	if o != nil && !IsNil(o.State) {
		return true
	}

	return false
}

// SetState gets a reference to the given ModelVersionState and assigns it to the State field.
func (o *ModelVersion) SetState(v ModelVersionState) {
	o.State = &v
}

// GetAuthor returns the Author field value if set, zero value otherwise.
func (o *ModelVersion) GetAuthor() string {
	if o == nil || IsNil(o.Author) {
		var ret string
		return ret
	}
	return *o.Author
}

// GetAuthorOk returns a tuple with the Author field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ModelVersion) GetAuthorOk() (*string, bool) {
	if o == nil || IsNil(o.Author) {
		return nil, false
	}
	return o.Author, true
}

// HasAuthor returns a boolean if a field has been set.
func (o *ModelVersion) HasAuthor() bool {
	if o != nil && !IsNil(o.Author) {
		return true
	}

	return false
}

// SetAuthor gets a reference to the given string and assigns it to the Author field.
func (o *ModelVersion) SetAuthor(v string) {
	o.Author = &v
}

// GetId returns the Id field value if set, zero value otherwise.
func (o *ModelVersion) GetId() string {
	if o == nil || IsNil(o.Id) {
		var ret string
		return ret
	}
	return *o.Id
}

// GetIdOk returns a tuple with the Id field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ModelVersion) GetIdOk() (*string, bool) {
	if o == nil || IsNil(o.Id) {
		return nil, false
	}
	return o.Id, true
}

// HasId returns a boolean if a field has been set.
func (o *ModelVersion) HasId() bool {
	if o != nil && !IsNil(o.Id) {
		return true
	}

	return false
}

// SetId gets a reference to the given string and assigns it to the Id field.
func (o *ModelVersion) SetId(v string) {
	o.Id = &v
}

// GetCreateTimeSinceEpoch returns the CreateTimeSinceEpoch field value if set, zero value otherwise.
func (o *ModelVersion) GetCreateTimeSinceEpoch() string {
	if o == nil || IsNil(o.CreateTimeSinceEpoch) {
		var ret string
		return ret
	}
	return *o.CreateTimeSinceEpoch
}

// GetCreateTimeSinceEpochOk returns a tuple with the CreateTimeSinceEpoch field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ModelVersion) GetCreateTimeSinceEpochOk() (*string, bool) {
	if o == nil || IsNil(o.CreateTimeSinceEpoch) {
		return nil, false
	}
	return o.CreateTimeSinceEpoch, true
}

// HasCreateTimeSinceEpoch returns a boolean if a field has been set.
func (o *ModelVersion) HasCreateTimeSinceEpoch() bool {
	if o != nil && !IsNil(o.CreateTimeSinceEpoch) {
		return true
	}

	return false
}

// SetCreateTimeSinceEpoch gets a reference to the given string and assigns it to the CreateTimeSinceEpoch field.
func (o *ModelVersion) SetCreateTimeSinceEpoch(v string) {
	o.CreateTimeSinceEpoch = &v
}

// GetLastUpdateTimeSinceEpoch returns the LastUpdateTimeSinceEpoch field value if set, zero value otherwise.
func (o *ModelVersion) GetLastUpdateTimeSinceEpoch() string {
	if o == nil || IsNil(o.LastUpdateTimeSinceEpoch) {
		var ret string
		return ret
	}
	return *o.LastUpdateTimeSinceEpoch
}

// GetLastUpdateTimeSinceEpochOk returns a tuple with the LastUpdateTimeSinceEpoch field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *ModelVersion) GetLastUpdateTimeSinceEpochOk() (*string, bool) {
	if o == nil || IsNil(o.LastUpdateTimeSinceEpoch) {
		return nil, false
	}
	return o.LastUpdateTimeSinceEpoch, true
}

// HasLastUpdateTimeSinceEpoch returns a boolean if a field has been set.
func (o *ModelVersion) HasLastUpdateTimeSinceEpoch() bool {
	if o != nil && !IsNil(o.LastUpdateTimeSinceEpoch) {
		return true
	}

	return false
}

// SetLastUpdateTimeSinceEpoch gets a reference to the given string and assigns it to the LastUpdateTimeSinceEpoch field.
func (o *ModelVersion) SetLastUpdateTimeSinceEpoch(v string) {
	o.LastUpdateTimeSinceEpoch = &v
}

func (o ModelVersion) MarshalJSON() ([]byte, error) {
	toSerialize, err := o.ToMap()
	if err != nil {
		return []byte{}, err
	}
	return json.Marshal(toSerialize)
}

func (o ModelVersion) ToMap() (map[string]interface{}, error) {
	toSerialize := map[string]interface{}{}
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
	if !IsNil(o.State) {
		toSerialize["state"] = o.State
	}
	if !IsNil(o.Author) {
		toSerialize["author"] = o.Author
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
	return toSerialize, nil
}

type NullableModelVersion struct {
	value *ModelVersion
	isSet bool
}

func (v NullableModelVersion) Get() *ModelVersion {
	return v.value
}

func (v *NullableModelVersion) Set(val *ModelVersion) {
	v.value = val
	v.isSet = true
}

func (v NullableModelVersion) IsSet() bool {
	return v.isSet
}

func (v *NullableModelVersion) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableModelVersion(val *ModelVersion) *NullableModelVersion {
	return &NullableModelVersion{value: val, isSet: true}
}

func (v NullableModelVersion) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableModelVersion) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}
