import io
import os
import platform
import stat
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from typing import cast

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


def generate_kiota_py_client(root: Path):
    os_name = KIOTA_OS_NAMES.get(platform.system())
    if os_name is None:
        print("Unsupported operating system.")
        exit(1)

    machine = platform.machine().lower()
    arch_name = KIOTA_ARCH_NAMES.get(machine)
    if arch_name is None:
        print("Unsupported architecture.")
        exit(1)

    release_name = f"{os_name}-{arch_name}"
    # Detecting the Kiota version from a .csproj file so that it can be updated by automatic tool (e.g. Dependabot)
    version = cast(
        ET.Element,
        ET.parse(root / "kiota-version.csproj")  # noqa: S314
        .getroot()
        .find(".//*[@Include='Microsoft.OpenApi.Kiota.Builder']"),
    ).get("Version")
    print(f"Using Kiota version: {version}")

    tmpdir = root / f"kiota_tmp-{version}"
    if not tmpdir.exists():
        print(f"Kiota not found on {tmpdir}. Downloading Kiota release.")
        # Download the Kiota release archive
        url = f"https://github.com/microsoft/kiota/releases/download/v{version}/{release_name}.zip"
        print(f"Downloading Kiota from URL: {url}")
        response = requests.get(url, timeout=10)
        zip_archive = zipfile.ZipFile(io.BytesIO(response.content))
        tmpdir.mkdir(parents=True)
        zip_archive.extractall(tmpdir)
    else:
        print(
            "Using kiota already available on path if something goes wrong, please clean the local 'kiota_tmp' folder."
        )

    kiota_bin = tmpdir / "kiota"
    st = os.stat(kiota_bin)
    os.chmod(kiota_bin, st.st_mode | stat.S_IEXEC)

    openapi_doc = root / "model-registry.yaml"
    output = root / "src/model_registry"

    command = f"""
        {kiota_bin} generate \
            --language=python --openapi="{openapi_doc}" --output="{output}" \
            --class-name=ModelRegistryClient --namespace-name=model_registry \
            --clear-cache
        """
    print(f"Executing kiota command: {command}")

    os.system(command)
    print("Kiota client generation has been successful")


if __name__ == "__main__":
    py_root = Path(__file__).parent
    kiota_lock_file = py_root / "src/model_registry/kiota-lock.json"
    if not kiota_lock_file.exists():
        generate_kiota_py_client(py_root)
