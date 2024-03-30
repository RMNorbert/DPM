from typing import List, Dict, Any
from argparse import Namespace
import argparse
import os
import sys
from filter.dataset_filterer import DatasetFilterer
from utils.configuration_provider import load_configuration

CONFIG: Dict[str, Any] = load_configuration('./configuration/filter_configuration.yaml')


def get_args() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(CONFIG['FILTER_TYPE_ARGUMENT'], type=str,
                        help=CONFIG['FILTER_TYPE_HELP'],
                        default=CONFIG['DEFAULT_FILTER_TYPE'])
    parser.add_argument(CONFIG['OUTPUT_ARGUMENT'], type=str,
                        help=CONFIG['OUTPUT_HELP'],
                        default=os.path.join(CONFIG['DEFAULT_OUTPUT_DIRECTORY'], CONFIG['DEFAULT_OUTPUT_FILE_NAME']))
    parser.add_argument(CONFIG['CSV_DATA_LIST_ARGUMENT'], type=str, nargs='+',
                        help=CONFIG['CSV_DATA_LIST_HELP'],
                        default=CONFIG['DEFAULT_CSV_DATA_LIST'])
    parser.add_argument(CONFIG['LABEL_DATA_LIST_ARGUMENT'], type=str, nargs='+',
                        help=CONFIG['LABEL_DATA_LIST_HELP'],
                        default=CONFIG['DEFAULT_LABEL_DATA_LIST'])
    return parser.parse_args()


def change_to_path(filename_list: List[str]) -> List[str]:
    try:
        return [os.path.join('/', filename) for filename in filename_list]
    except TypeError:
        sys.exit(CONFIG['ON_LOAD_ERROR_MESSAGE'])


def main():
    args: Namespace = get_args()

    output_directory: str = args.output
    csv_list: List[str] = change_to_path(args.csv_list)
    label_list: List[str] = args.label_list
    filter_type: str = args.filter_type

    df = DatasetFilterer(csv_file_path_list=csv_list,
                         searched_label_list=label_list,
                         image_list_file_path=output_directory)

    if filter_type == CONFIG['IMAGE_TYPE']:
        df.create_filtered_image_id_txt_file()
    elif filter_type == CONFIG['IMAGE_AND_LABEL_TYPE']:
        df.create_filtered_image_id_txt_file_with_label_txt_file()


if __name__ == '__main__':
    main()
