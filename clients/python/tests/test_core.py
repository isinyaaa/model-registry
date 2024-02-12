"""Tests for user facing model registry APIs."""

import pytest
from model_registry.core import ModelRegistryAPIClient
from model_registry.types import ModelArtifact, ModelVersion, RegisteredModel


@pytest.fixture()
def model() -> ModelArtifact:
    return ModelArtifact("model", "uri", external_id="ma id")


@pytest.fixture()
def model_version() -> ModelVersion:
    return ModelVersion("version", "author", external_id="mv id")


@pytest.fixture()
def registered_model() -> RegisteredModel:
    return RegisteredModel("registered", external_id="mr id")


# TODO: should we test insert/update separately?
def test_upsert_registered_model(
    mr_api: ModelRegistryAPIClient, registered_model: RegisteredModel
):
    assert mr_api.upsert_registered_model(registered_model)


def test_get_registered_model_by_id(
    mr_api: ModelRegistryAPIClient,
    registered_model: RegisteredModel,
):
    mr_api.upsert_registered_model(registered_model)
    assert (rm := mr_api.get_registered_model_by_id(registered_model.id))
    assert rm == registered_model


def test_get_registered_model_by_name(
    mr_api: ModelRegistryAPIClient,
    registered_model: RegisteredModel,
):
    mr_api.upsert_registered_model(registered_model)
    assert (rm := mr_api.get_registered_model_by_params(name=registered_model.name))
    assert rm == registered_model


def test_get_registered_model_by_external_id(
    mr_api: ModelRegistryAPIClient,
    registered_model: RegisteredModel,
):
    mr_api.upsert_registered_model(registered_model)
    assert (
        rm := mr_api.get_registered_model_by_params(
            external_id=registered_model.external_id
        )
    )
    assert rm == registered_model


def test_get_registered_models(
    mr_api: ModelRegistryAPIClient, registered_model: RegisteredModel
):
    rm1 = mr_api.upsert_registered_model(registered_model)
    registered_model.name += "2"
    rm2 = mr_api.upsert_registered_model(registered_model)

    rms = mr_api.get_registered_models()
    assert [rm1, rm2] == rms


def test_upsert_model_version(
    mr_api: ModelRegistryAPIClient,
    model_version: ModelVersion,
):
    assert mr_api.upsert_model_version(model_version, "1")


def test_get_model_version_by_id(
    mr_api: ModelRegistryAPIClient, model_version: ModelVersion
):
    mv = mr_api.upsert_model_version(model_version, "1")
    assert (new_mv := mr_api.get_model_version_by_id(mv.id))
    assert new_mv == mv


def test_get_model_version_by_name(
    mr_api: ModelRegistryAPIClient,
    model_version: ModelVersion,
):
    mv = mr_api.upsert_model_version(model_version, "1")
    assert (
        new_mv := mr_api.get_model_version_by_params(
            registered_model_id="1", version=model_version.name
        )
    )
    assert new_mv == mv


def test_get_model_version_by_external_id(
    mr_api: ModelRegistryAPIClient, model_version: ModelVersion
):
    mv = mr_api.upsert_model_version(model_version, "1")
    assert (
        new_mv := mr_api.get_model_version_by_params(
            external_id=model_version.external_id
        )
    )
    assert new_mv == mv


def test_get_model_versions(
    mr_api: ModelRegistryAPIClient,
    model_version: ModelVersion,
):
    mv1 = mr_api.upsert_model_version(model_version, "1")
    model_version.name += "2"
    mv2 = mr_api.upsert_model_version(model_version, "1")

    mvs = mr_api.get_model_versions("1")
    assert [mv1, mv2] == mvs


def test_upsert_model_artifact(
    mr_api: ModelRegistryAPIClient,
    model: ModelArtifact,
):
    assert mr_api.upsert_model_artifact(model, "1")


def test_get_model_artifact_by_id(mr_api: ModelRegistryAPIClient, model: ModelArtifact):
    ma = mr_api.upsert_model_artifact(model, "1")
    assert (new_ma := mr_api.get_model_artifact_by_id(model.id))
    assert new_ma == ma


def test_get_model_artifact_by_model_version_id(
    mr_api: ModelRegistryAPIClient, model_version: ModelVersion, model: ModelArtifact
):
    ma = mr_api.upsert_model_artifact(model, "1")
    assert (new_ma := mr_api.get_model_artifact_by_params(model_version_id="1"))
    assert new_ma == ma


def test_get_model_artifact_by_external_id(
    mr_api: ModelRegistryAPIClient, model: ModelArtifact
):
    ma = mr_api.upsert_model_artifact(model, "1")
    assert (
        new_ma := mr_api.get_model_artifact_by_params(external_id=model.external_id)
    )
    assert new_ma == ma


def test_get_all_model_artifacts(
    mr_api: ModelRegistryAPIClient, model_version: ModelVersion, model: ModelArtifact
):
    ma1 = mr_api.upsert_model_artifact(model, str(model_version.id))
    model.name += "2"
    ma2 = mr_api.upsert_model_artifact(model, str(model_version.id))

    mas = mr_api.get_model_artifacts()
    assert [ma1, ma2] == mas


def test_get_model_artifacts_by_mv_id(
    mr_api: ModelRegistryAPIClient, model_version: ModelVersion, model: ModelArtifact
):
    ma1 = mr_api.upsert_model_artifact(model, model_version.id)
    model.name += "2"
    ma2 = mr_api.upsert_model_artifact(model, model_version.id)

    mas = mr_api.get_model_artifacts(model_version.id)
    assert [ma1, ma2] == mas
