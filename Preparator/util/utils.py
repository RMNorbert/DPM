import yaml, os
from typing import Dict, Any, Final

STRING: Final = str
BYTE: Final = bytes


def load_configuration(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)


def create_output_folder_if_not_exists(default_folder: STRING | BYTE, sub_folder: str) -> STRING | BYTE:
    try:
        folder: STRING | BYTE = os.path.join(default_folder, sub_folder)
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder
    except OSError as e:
        print(f"An error occurred{e}")