import yaml
from typing import Dict, Any


def load_configuration(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)
