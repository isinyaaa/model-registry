import asyncio
import logging
import os
import time
from pathlib import Path

import pytest
import requests
from model_registry.core import ModelRegistryAPIClient
from testcontainers.compose import DockerCompose
from testcontainers.core.waiting_utils import wait_for_logs

logger = logging.getLogger("model_registry")
logger.setLevel(logging.DEBUG)


# workaround: https://stackoverflow.com/a/72104554
@pytest.fixture(scope="session", autouse=True)
def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()

    try:
        yield loop
    finally:
        loop.close()


@pytest.fixture(scope="session")
def repo_root(request) -> Path:
    root = request.config.rootpath.parent.parent
    print("Assuming this is the Model Registry root directory:", root)
    return root


# ruff: noqa: PT021 supported
@pytest.fixture(scope="session")
def mr_compose(request, repo_root: Path) -> DockerCompose:
    shared_volume = repo_root / "test/config/ml-metadata"
    sqlite_db_file = shared_volume / "metadata.sqlite.db"
    if sqlite_db_file.exists():
        msg = f"The file {sqlite_db_file} already exists; make sure to cancel it before running these tests."
        raise FileExistsError(msg)

    compose = DockerCompose(
        repo_root,
        "docker-compose-local.yaml",
    )
    compose.start()
    wait_for_logs(compose, "Server listening on")
    os.system('docker container ls --format "table {{.ID}}\t{{.Names}}\t{{.Ports}}" -a')  # noqa governed test

    # this callback is needed in order to perform the container.stop()
    # removing this callback might result in mlmd container shutting down before the tests had chance to fully run,
    # and resulting in grpc connection resets.
    def teardown():
        print(compose.get_logs()[0])
        compose.stop()
        try:
            os.remove(sqlite_db_file)
            print(f"Removed {sqlite_db_file} successfully.")
        except Exception as e:
            print(f"An error occurred while removing {sqlite_db_file}: {e}")
        print("teardown of plain_wrapper completed.")

    request.addfinalizer(teardown)

    time.sleep(
        3
    )  # allowing some time for mlmd grpc to fully stabilize (is "spent" once per pytest session anyway)

    return compose


@pytest.fixture(scope="session")
def mr_api(
    mr_compose: DockerCompose,
) -> ModelRegistryAPIClient:
    # because the server network mode is set to "host", it's as if the server is running on the host machine
    server_address = "http://localhost:8080"
    # mr_compose can't tell us service names, so we have to hardcode it
    poll_for_ready(
        mr_compose,
        f"{server_address}/api/model_registry/v1alpha2",
    )

    return ModelRegistryAPIClient(server_address)


def poll_for_ready(
    compose: DockerCompose,
    route: str,
    timeout: float = 6.0,
    interval: float = 0.5,
):
    start = time.time()
    while True:
        duration = time.time() - start
        try:
            response = requests.get(route, timeout=0.001)
        except requests.exceptions.ConnectionError as e:
            print(e)
            print("Container logs:\n", compose.get_logs())
            print("Container not ready. Retrying...")
        else:
            if response is not None:
                return duration
            if timeout and duration > timeout:
                msg = f"endpoint {route} not ready after timeout: {timeout}s"
                raise TimeoutError(msg)
        time.sleep(interval)
