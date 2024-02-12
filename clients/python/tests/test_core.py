"""Tests for user facing model registry APIs."""

import pytest
from model_registry.core import ModelRegistryAPIClient
from model_registry.types import ModelArtifact, ModelVersion, RegisteredModel


def test_insert_registered_model(mr_api: ModelRegistryAPIClient):
    registered_model = RegisteredModel("test rm")
    rm = mr_api.upsert_registered_model(registered_model)
    assert rm.id
    assert rm.name == registered_model.name
    assert rm.external_id is None
    assert rm.description is None
    assert rm.create_time_since_epoch
    assert rm.last_update_time_since_epoch


def test_update_registered_model(mr_api: ModelRegistryAPIClient):
    registered_model = RegisteredModel("updated rm")
    rm = mr_api.upsert_registered_model(registered_model)
    last_update = rm.last_update_time_since_epoch
    rm.description = "lorem ipsum"
    rm = mr_api.upsert_registered_model(rm)

    assert rm.description == "lorem ipsum"
    assert rm.last_update_time_since_epoch != last_update


@pytest.fixture(scope="module")
def registered_model(mr_api: ModelRegistryAPIClient) -> RegisteredModel:
    return mr_api.upsert_registered_model(
        RegisteredModel("registered", external_id="mr id")
    )


def test_get_registered_model_by_id(
    mr_api: ModelRegistryAPIClient,
    registered_model: RegisteredModel,
):
    assert (rm := mr_api.get_registered_model_by_id(str(registered_model.id)))
    assert rm == registered_model


def test_get_registered_model_by_name(
    mr_api: ModelRegistryAPIClient,
    registered_model: RegisteredModel,
):
    assert (rm := mr_api.get_registered_model_by_params(name=registered_model.name))
    assert rm == registered_model


def test_get_registered_model_by_external_id(
    mr_api: ModelRegistryAPIClient,
    registered_model: RegisteredModel,
):
    assert (
        rm := mr_api.get_registered_model_by_params(
            external_id=registered_model.external_id
        )
    )
    assert rm == registered_model


def test_get_registered_models(
    mr_api: ModelRegistryAPIClient, registered_model: RegisteredModel
):
    registered_model.name += "2"
    rm2 = mr_api.upsert_registered_model(registered_model)

    rms = mr_api.get_registered_models()
    assert [registered_model, rm2] == rms


def test_insert_model_version(
    mr_api: ModelRegistryAPIClient,
    registered_model: RegisteredModel,
):
    model_version = ModelVersion("test version", "test author")
    mv = mr_api.upsert_model_version(model_version, str(registered_model.id))
    assert mv.id
    assert mv.name == model_version.name
    assert mv.registered_model_id is None
    assert mv.external_id is None
    assert mv.description is None
    assert mv.create_time_since_epoch
    assert mv.last_update_time_since_epoch
    assert mv.author == model_version.author


def test_update_model_version(
    mr_api: ModelRegistryAPIClient, registered_model: RegisteredModel
):
    model_version = ModelVersion("updated mv", "test author")
    mv = mr_api.upsert_model_version(model_version, str(registered_model.id))
    last_update = mv.last_update_time_since_epoch
    mv.description = "lorem ipsum"
    mv = mr_api.upsert_model_version(mv, str(registered_model.id))

    assert mv.description == "lorem ipsum"
    assert mv.last_update_time_since_epoch != last_update


@pytest.fixture(scope="module")
def model_version(
    mr_api: ModelRegistryAPIClient, registered_model: RegisteredModel
) -> ModelVersion:
    return mr_api.upsert_model_version(
        ModelVersion("version", "author", external_id="mv id"),
        str(registered_model.id),
    )


def test_get_model_version_by_id(
    mr_api: ModelRegistryAPIClient, model_version: ModelVersion
):
    assert (mv := mr_api.get_model_version_by_id(str(model_version.id)))
    assert mv == model_version


def test_get_model_version_by_name(
    mr_api: ModelRegistryAPIClient,
    registered_model: RegisteredModel,
    model_version: ModelVersion,
):
    assert (
        mv := mr_api.get_model_version_by_params(
            registered_model_id=str(registered_model.id), name=model_version.name
        )
    )
    assert mv == model_version


def test_get_model_version_by_external_id(
    mr_api: ModelRegistryAPIClient, model_version: ModelVersion
):
    assert (
        mv := mr_api.get_model_version_by_params(external_id=model_version.external_id)
    )
    assert mv == model_version


def test_get_model_versions(
    mr_api: ModelRegistryAPIClient,
    registered_model: RegisteredModel,
    model_version: ModelVersion,
):
    model_version.name += "2"
    mv2 = mr_api.upsert_model_version(model_version, str(registered_model.id))

    mvs = mr_api.get_model_versions(str(registered_model.id))
    assert [model_version, mv2] == mvs


def test_insert_model_artifact(
    mr_api: ModelRegistryAPIClient,
    model_version: ModelVersion,
):
    ma = mr_api.upsert_model_artifact(
        ModelArtifact("model", "uri"), str(model_version.id)
    )
    assert ma.id
    assert ma.name == "model"
    assert ma.uri == "uri"
    assert ma.description is None
    assert ma.external_id is None
    assert ma.create_time_since_epoch
    assert ma.last_update_time_since_epoch
    assert ma.model_format_name
    assert ma.model_format_version
    assert ma.storage_key
    assert ma.storage_path
    assert ma.service_account_name


def test_update_model_artifact(
    mr_api: ModelRegistryAPIClient, model_version: ModelVersion
):
    model = ModelArtifact("model", "uri")
    ma = mr_api.upsert_model_artifact(model, str(model_version.id))
    last_update = ma.last_update_time_since_epoch
    ma.description = "lorem ipsum"
    ma = mr_api.upsert_model_artifact(ma, str(model_version.id))

    assert ma.description == "lorem ipsum"
    assert ma.last_update_time_since_epoch != last_update


def model(
    mr_api: ModelRegistryAPIClient,
    model_version: ModelVersion,
) -> ModelArtifact:
    return mr_api.upsert_model_artifact(
        ModelArtifact("model", "uri", external_id="ma id"), str(model_version.id)
    )


def test_get_model_artifact_by_id(mr_api: ModelRegistryAPIClient, model: ModelArtifact):
    assert (ma := mr_api.get_model_artifact_by_id(str(model.id)))
    assert ma == model


def test_get_model_artifact_by_model_version_id(
    mr_api: ModelRegistryAPIClient, model_version: ModelVersion, model: ModelArtifact
):
    assert (
        ma := mr_api.get_model_artifact_by_params(
            model_version_id=str(model_version.id)
        )
    )
    assert ma == model


def test_get_model_artifact_by_external_id(
    mr_api: ModelRegistryAPIClient, model: ModelArtifact
):
    assert (ma := mr_api.get_model_artifact_by_params(external_id=model.external_id))
    assert ma == model


def test_get_all_model_artifacts(
    mr_api: ModelRegistryAPIClient, model_version: ModelVersion, model: ModelArtifact
):
    model.name += "2"
    ma2 = mr_api.upsert_model_artifact(model, str(model_version.id))

    mas = mr_api.get_model_artifacts()
    assert [model, ma2] == mas


def test_get_model_artifacts_by_mv_id(
    mr_api: ModelRegistryAPIClient, model_version: ModelVersion, model: ModelArtifact
):
    model.name = "model2"
    ma2 = mr_api.upsert_model_artifact(model, str(model_version.id))

    mas = mr_api.get_model_artifacts(str(model_version.id))
    assert [model, ma2] == mas
