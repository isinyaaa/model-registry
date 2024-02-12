import os
import time
from pathlib import Path

import pytest
from model_registry.core import ModelRegistryAPIClient
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs


@pytest.fixture(scope="session")
def repo_root(request) -> Path:
    root = request.config.rootpath.parent.parent
    print("Assuming this is the Model Registry root directory:", root)
    return root


# ruff: noqa: PT021 supported
@pytest.fixture(scope="session")
def mr_container(request, repo_root: Path) -> DockerContainer:
    shared_volume = repo_root / "test/config/ml-metadata"
    sqlite_db_file = shared_volume / "metadata.sqlite.db"
    if sqlite_db_file.exists():
        msg = f"The file {sqlite_db_file} already exists; make sure to cancel it before running these tests."
        raise FileExistsError(msg)
    container = DockerContainer("gcr.io/tfx-oss-public/ml_metadata_store_server:1.14.0")
    container.with_exposed_ports(8080)
    container.with_volume_mapping(
        shared_volume,
        "/tmp/shared",  # noqa: S108
        "rw",
    )
    container.with_env(
        "METADATA_STORE_SERVER_CONFIG_FILE",
        "/tmp/shared/conn_config.pb",  # noqa: S108
    )
    container.start()
    wait_for_logs(container, "Server listening on")
    os.system('docker container ls --format "table {{.ID}}\t{{.Names}}\t{{.Ports}}" -a')  # noqa governed test
    print("waited for logs and port")

    # this callback is needed in order to perform the container.stop()
    # removing this callback might result in mlmd container shutting down before the tests had chance to fully run,
    # and resulting in grpc connection resets.
    def teardown():
        container.stop()
        print("teardown of plain_wrapper completed.")

    request.addfinalizer(teardown)

    time.sleep(
        3
    )  # allowing some time for mlmd grpc to fully stabilize (is "spent" once per pytest session anyway)

    return container


@pytest.fixture(scope="session")
def mr_api(
    request,
    repo_root: Path,
    mr_container: DockerContainer,
) -> ModelRegistryAPIClient:
    sqlite_db_file = repo_root / "test/config/ml-metadata/metadata.sqlite.db"
    store = ModelRegistryAPIClient(int(container.get_exposed_port(8080)))

    def teardown():
        try:
            os.remove(sqlite_db_file)
            print(f"Removed {sqlite_db_file} successfully.")
        except Exception as e:
            print(f"An error occurred while removing {sqlite_db_file}: {e}")
        print("plain_wrapper_after_each done.")

    request.addfinalizer(teardown)

    return store


@pytest.fixture()
def mr_api(store_wrapper: MLMDStore) -> ModelRegistryAPIClient:
    mr = object.__new__(ModelRegistryAPIClient)
    mr._store = store_wrapper
    return mr


def poll_for_ready(
    container: DockerContainer,
    timeout: float = 6.0,
    interval: float = 0.5,
):
    start = time.time()
    while True:
        duration = time.time() - start
        results = None
        try:
            pass
        except Exception as e:
            print(e)
            print("Container logs:\n", container.get_logs())
            print("Container not ready. Retrying...")
        else:
            if results is not None:
                return duration
            if timeout and duration > timeout:
                msg = f"container not ready after timeout: {timeout}s"
                raise TimeoutError(msg)
        time.sleep(interval)
