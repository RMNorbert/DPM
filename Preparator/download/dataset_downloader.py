import sys
from requests import Response, get
from download.download_helper import *
from utils.configuration_provider import load_configuration
from concurrent.futures import Future

CONFIG = load_configuration(
    './configuration/dataset_downloader_configuration.yaml')


class DatasetDownloader:
    def __init__(self):
        self.REGEX: str = fr"{CONFIG['DATASET_VALIDATOR_REGEX']}"
        self.DRIVE_PREFIX: str = CONFIG['DRIVE_PREFIX']

    def download_image(self, split: str, image_id: str, download_folder: STRING | BYTE) -> None:
        response: Response = get(self.DRIVE_PREFIX + image_id)
        filename: str = os.path.join(
            f"{download_folder}/{split}", f"{image_id}{CONFIG['DOWNLOAD_DATA_TYPE']}")
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)

    def download_images_in_parallel(self,
                                    args: dict[str, Any],
                                    output_folder: STRING | BYTE,
                                    image_list: list[tuple[str, str]]) -> None:
        progress_bar: tqdm = initialize_bar(len(image_list))
        with futures.ThreadPoolExecutor(
                max_workers=args['processes']) as executor:
            all_futures: list[Future] = [executor.submit(self.download_image, split, image_id, output_folder)
                                         for (split, image_id) in image_list]
            update_progress_bar(all_futures, progress_bar)

        progress_bar.close()

    def download_all_images(self, args: dict[str, Any]) -> None:
        try:
            output_folder: STRING | BYTE = create_output_folder_if_not_exists(
                args['output_folder'])
            image_list: list[tuple[str, str]] = list(
                validate_image_list(self.REGEX, read_image_list_file(args['image_list'])))
            self.download_images_in_parallel(args, output_folder, image_list)
        except ValueError as exception:
            sys.exit(str(exception))
