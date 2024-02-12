import io
import os
import platform
import stat
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

import requests

KIOTA_OS_NAMES = {"Windows": "win", "Darwin": "osx", "Linux": "linux"}
KIOTA_ARCH_NAMES = {
    "x86_64": "x64",
    "amd64": "x64",
    "i386": "x86",
    "x86": "x86",
    "x86_64": "x64",
    "amd64": "x64",
    "aarch64": "arm64",
    "arm64": "arm64",
}


def generate_kiota_client_files(setup_kwargs):
    kiota_os_name = KIOTA_OS_NAMES.get(platform.system(), None)
    if kiota_os_name is None:
        print("Unsupported operating system.")
        exit(1)

    machine = platform.machine().lower()
    kiota_arch_name = KIOTA_ARCH_NAMES.get(machine)
    if kiota_arch_name is None:
        print("Unsupported architecture.")
        exit(1)

    kiota_release_name = f"{kiota_os_name}-{kiota_arch_name}.zip"
    # Detecting the Kiota version from a .csproj file so that it can be updated by automatic tool (e.g. Dependabot)
    kiota_version = (
        ET.parse(os.path.join(sys.path[0], "kiota-version.csproj"))
        .getroot()
        .find(".//*[@Include='Microsoft.OpenApi.Kiota.Builder']")
        .get("Version")
    )
    print(f"Using Kiota version: {kiota_version}")
    # Download the Kiota release archive
    url = f"https://github.com/microsoft/kiota/releases/download/v{kiota_version}/{kiota_release_name}"

    tmpdir = os.path.join(sys.path[0], "kiota_tmp", kiota_version)
    if not os.path.exists(tmpdir):
        print(f"Downloading Kiota from URL: {url}")
        response = requests.get(url)
        zip_archive = zipfile.ZipFile(io.BytesIO(response.content))
        os.makedirs(tmpdir)
        zip_archive.extractall(tmpdir)
    else:
        print(
            "Using kiota already available on path if something goes wrong, please clean the local 'kiota_tmp' folder."
        )

    kiota_bin = os.path.join(tmpdir, "kiota")
    st = os.stat(kiota_bin)
    os.chmod(kiota_bin, st.st_mode | stat.S_IEXEC)

    openapi_doc = Path(__file__).parent.joinpath("model-registry.yaml")
    output = Path(__file__).parent.joinpath("src", "model_registry")

    command = f'{kiota_bin} generate --language=python --openapi="{openapi_doc}" --output="{output}" --class-name=ModelRegistryClient --namespace-name=model_registry --clear-cache'
    print(f"Executing kiota command: {command}")

    os.system(command)
    print("Kiota client generation has been successful")
    return setup_kwargs


if __name__ == "__main__":
    if not os.path.exists(
        os.path.join(sys.path[0], "src", "model_registry", "kiota-lock.json")
    ):
        generate_kiota_client_files({})
