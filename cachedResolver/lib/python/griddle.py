import requests
import zipfile
import tempfile
from typing import Any


BASE_URL = "http://127.0.0.1:8000"


def get_asset_json(asset_name: str) -> list:
    endpoint = "/api/v1/assets/"
    url = f"{BASE_URL}{endpoint}"
    params = {
        "search": asset_name,
        "keywords": "",
        "sort": "name_dsc",
        "offset": 0
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {}


def download_asset(asset_name: str) -> str:
    asset = get_asset_json(asset_name)
    if not asset:
        return ""

    asset = asset[0]
    uuid = asset['id']
    versions = f"{BASE_URL}/api/v1/assets/{uuid}/versions"
    params = {"sort": "desc"}
    response = requests.get(versions, params=params)

    if response.status_code == 200:
        semver = response.json()[0]['semver']
    else:
        return ""

    download = f"{BASE_URL}/api/v1/assets/{uuid}/versions/{semver}/file"

    # Create a persistent temporary directory
    temp_dir = tempfile.mkdtemp()

    with requests.get(download, stream=True) as r:
        r.raise_for_status()
        zip_path = f"{temp_dir}/asset.zip"
        with open(zip_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    # Unzip the file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)

    return temp_dir  # Return the path to the temporary directory


if __name__ == '__main__':
    temp_dir = download_asset("sushi")
    if (temp_dir):
        print(f"Files extracted to: {temp_dir}")
        print(f"{temp_dir}\sushi.usda")
    else:
        print("Extraction failed.")
