import os
import time

import pytest
from model_registry.core import ModelRegistryAPIClient

# from testcontainers.core.waiting_utils import wait_for_logs


@pytest.fixture(scope="session")
def mlmd_conn(request):
    model_registry_root_dir = model_registry_root(request)
    print(
        "Assuming this is the Model Registry root directory:", model_registry_root_dir
    )
    shared_volume = model_registry_root_dir / "test/config/ml-metadata"
    sqlite_db_file = shared_volume / "metadata.sqlite.db"
    if sqlite_db_file.exists():
        msg = f"The file {sqlite_db_file} already exists; make sure to cancel it before running these tests."
        raise FileExistsError(msg)
    # wait_for_logs(container, "Server listening on")
    os.system('docker container ls --format "table {{.ID}}\t{{.Names}}\t{{.Ports}}" -a')  # noqa governed test
    print("waited for logs and port")

    # this callback is needed in order to perform the container.stop()
    # removing this callback might result in mlmd container shutting down before the tests had chance to fully run,
    # and resulting in grpc connection resets.
    def teardown():
        # container.stop()
        print("teardown of plain_wrapper completed.")

    request.addfinalizer(teardown)  # noqa: PT021

    time.sleep(
        3
    )  # allowing some time for mlmd grpc to fully stabilize (is "spent" once per pytest session anyway)


def model_registry_root(request):
    return (request.config.rootpath / "../..").resolve()  # resolves to absolute path


@pytest.fixture()
def mr_api(request) -> ModelRegistryAPIClient:
    sqlite_db_file = (
        model_registry_root(request) / "test/config/ml-metadata/metadata.sqlite.db"
    )

    def teardown():
        try:
            os.remove(sqlite_db_file)
            print(f"Removed {sqlite_db_file} successfully.")
        except Exception as e:
            print(f"An error occurred while removing {sqlite_db_file}: {e}")
        print("plain_wrapper_after_each done.")

    request.addfinalizer(teardown)

    # return ModelRegistryAPIClient()


def wait_for_grpc(
    # container: DockerContainer,
    timeout=6,
    interval=2,
):
    start = time.time()
    while True:
        duration = time.time() - start
        results = None
        try:
            pass
        except Exception as e:
            print(e)
            # print("Container logs:\n", container.get_logs())
            print("Container not ready. Retrying...")
        if results is not None:
            return duration
        if timeout and duration > timeout:
            raise TimeoutError("wait_for_grpc not ready %.3f seconds" % timeout)
        time.sleep(interval)
