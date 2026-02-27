from weaponDetection.config_schemas.config_schema import Config
from weaponDetection.utils.config_utils import get_config
from weaponDetection.utils.data_utils import initialize_dvc, initialize_dvc_storage, make_new_data_version
from weaponDetection.utils.utils import get_logger
from pathlib import Path


@get_config(config_path="../configs", config_name="config")
def version_data(config: Config) -> None:

    initialize_dvc()

    initialize_dvc_storage(config.dvc_remote_name, config.dvc_remote_url)

    make_new_data_version(config.dvc_raw_data_folder, config.dvc_remote_name)


if __name__ == "__main__":
    version_data()  # type: ignore
