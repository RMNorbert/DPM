import re
from typing import Dict, Any, Generator
from tqdm import tqdm
from concurrent import futures

from util.utils import *

CONFIG: Dict[str, Any] = load_configuration(
    './configuration/download_helper_configuration.yaml')


def parse_image_list(regex: str, image: str) -> Generator[tuple[str, str], Any, None]:
    split, image_id = re.match(regex, image).groups()
    yield split, image_id


def validate_image_list(regex: str, image_list) -> Generator[tuple[str, str], Any, Any]:
    for line_number, image in enumerate(image_list):
        try:
            yield from parse_image_list(regex, image)
        except (ValueError, AttributeError):
            raise ValueError(
                f'ERROR in line {line_number}. The value of "{image}" is not recognized. ')


def read_image_list_file(image_list_file: str) -> Generator[str, str, None]:
    with open(image_list_file, 'r') as f:
        for line in f:
            yield line.strip().replace(CONFIG['ORIGINAL_IMAGE_TYPE'], CONFIG['NEW_IMAGE_NEW_TYPE'])


def initialize_bar(number_of_files: int) -> tqdm:
    return tqdm(total=number_of_files, desc=CONFIG['DOWNLOAD_BAR_DESCRIPTION'], leave=True)


def update_progress_bar(all_futures: list, bar: tqdm) -> None:
    for future in futures.as_completed(all_futures):
        future.result()
        bar.update(CONFIG['DOWNLOAD_BAR_UPDATE_SPEED'])
