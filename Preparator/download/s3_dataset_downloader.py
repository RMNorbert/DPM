from boto3.resources.factory import ServiceResource
import sys
import boto3
import botocore
from download.download_helper import *
from util.utils import *
from concurrent.futures import Future

CONFIG: Dict[str, Any] = load_configuration(
    './configuration/s3_dataset_downloader_config.yaml')


class S3DatasetDownloader:
    def __init__(self):
        self.REGEX: str = f"{CONFIG['DATASET_VALIDATOR_REGEX']}"
        self.bucket: ServiceResource = None

    def download_s3_image(self, split: str, image_id: str, output_folder: STRING | BYTE) -> None:
        try:
            download_folder: STRING | BYTE = create_output_folder_if_not_exists(output_folder, split)
            self.bucket.download_file(f"{split}/{image_id}{CONFIG['DOWNLOAD_DATA_TYPE']}",
                                      os.path.join(f'{download_folder}',
                                                   f"{image_id}{CONFIG['DOWNLOAD_DATA_TYPE']}"))
        except botocore.exceptions.ClientError as exception:
            sys.exit(
                f"{CONFIG['ERROR_MESSAGE']}:{split}/{image_id}`: {str(exception)}")

    def download_s3_images_in_parallel(self,
                                       args: dict[str, Any],
                                       image_list: list[tuple[str, str]]) -> None:
        progress_bar = initialize_bar(len(image_list))
        with futures.ThreadPoolExecutor(
                max_workers=args['processes']) as executor:
            all_futures: list[Future] = [executor.submit(self.download_s3_image, split, image_id, args['output_folder'])
                                         for (split, image_id) in image_list]
            update_progress_bar(all_futures, progress_bar)

        progress_bar.close()

    def download_all_s3_images(self, args: dict[str, Any]) -> None:
        try:
            self.bucket = boto3.resource('s3',
                                         config=botocore.config.Config(signature_version=botocore.UNSIGNED)).Bucket(
                args['bucket_name'])
            image_list: list[tuple[str, str]] = list(
                validate_image_list(self.REGEX, read_image_list_file(args['image_list'])))

            self.download_s3_images_in_parallel(
                args, image_list)
        except ValueError as exception:
            sys.exit(str(exception))
