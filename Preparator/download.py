from typing import Dict, Any
from argparse import Namespace
import argparse
from download.s3_dataset_downloader import S3DatasetDownloader
from download.dataset_downloader import DatasetDownloader
from util.utils import load_configuration

CONFIG: Dict[str, Any] = load_configuration(
    'configuration/download_configuration.yaml')


def get_args() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(CONFIG['DATASET_ID_PROVIDING_ARGUMENT'], type=str,
                        default=CONFIG['DEFAULT_DATASET_ID_SOURCE'],
                        help=(CONFIG['DATASET_ID_ARGUMENT_HELP']))
    parser.add_argument(CONFIG['PARALLEL_PROCESS_ARGUMENT'], type=int,
                        default=CONFIG['DEFAULT_PARALLEL_PROCESSES'],
                        help=CONFIG['PARALLEL_PROCESS_HELP'])
    parser.add_argument(CONFIG['OUTPUT_ARGUMENT'], type=str,
                        default=CONFIG['DEFAULT_OUTPUT_FOLDER'],
                        help=CONFIG['OUTPUT_HELP'])
    parser.add_argument(CONFIG['REQUEST_TYPE_ARGUMENT'], type=str,
                        default=CONFIG['DEFAULT_REQUEST_TYPE'],
                        help=CONFIG['REQUEST_TYPE_HELP'])
    parser.add_argument(CONFIG['BUCKET_NAME_ARGUMENT'], type=str,
                        default=CONFIG['DEFAULT_BUCKET_NAME'],
                        help=CONFIG['BUCKET_NAME_HELP'])
    return parser.parse_args()


def main():
    args: Namespace = get_args()
    if args.request is not None:
        if args.request:
            downloader = DatasetDownloader()
            downloader.download_all_images(vars(args))
        elif not args.request:
            downloader = S3DatasetDownloader()
            downloader.download_all_s3_images(vars(args))


if __name__ == '__main__':
    main()
