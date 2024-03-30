from typing import List, Dict, Any
import os
import sys
from utils.configuration_provider import load_configuration

CONFIG: Dict[str, Any] = load_configuration(
    './configuration/dataset_filter_configuration.yaml')


class DatasetFilterer:
    def __init__(self, csv_file_path_list: List[str], searched_label_list: List[str], image_list_file_path: str):
        self.csv_file_path_list: List[str] = csv_file_path_list
        self.searched_label_list: List[str] = searched_label_list
        self.image_list_file_path: str = image_list_file_path
        self.image_list_file_list: List[str] = []
        self.dataset_subset_list: List[str] = CONFIG['DATASET_SUBSET']

    def create_filtered_image_id_txt_file(self) -> None:
        try:
            for i, filename in enumerate(self.csv_file_path_list):
                with open(filename, 'r') as f:
                    line = f.readline()
                    while len(line) != 0:
                        image_id, _, label_name, _, x_min, x_max, y_min, y_max, _, _, _, _, _ = line.split(',')[
                            :13]
                        if label_name in self.searched_label_list and image_id not in self.image_list_file_list:
                            self.image_list_file_list.append(image_id)
                            with open(self.image_list_file_path, 'a') as fw:
                                fw.write(
                                    '{}/{}\n'.format(self.dataset_subset_list[i], image_id))
                                print(
                                    CONFIG['IMAGE_INFORMATION_MESSAGE'], image_id)
                        line = f.readline()

                    f.close()

        except TypeError as exception:
            sys.exit(str(exception))

    def create_filtered_image_id_txt_file_with_label_txt_file(self) -> None:
        try:
            for i, filename in enumerate(self.csv_file_path_list):
                with open(filename, 'r') as f:
                    line = f.readline()
                    while len(line) != 0:
                        image_id, _, label_name, _, x_min, x_max, y_min, y_max, _, _, _, _, _ = line.split(',')[
                            :13]
                        if label_name in self.searched_label_list and image_id not in self.image_list_file_list:
                            self.image_list_file_list.append(image_id)
                            with open(self.image_list_file_path, 'a') as fw:
                                fw.write(
                                    '{}/{}\n'.format(self.dataset_subset_list[i], image_id))
                                curr_img_label: str = os.path.join('./data/label/{}',
                                                                   '{}.txt'.format(self.dataset_subset_list[i],
                                                                                   image_id))
                                print(
                                    CONFIG['IMAGE_INFORMATION_MESSAGE'], image_id)
                                with open(curr_img_label, 'a') as lw:
                                    lw.write('{} {} {} {} {}\n'.format(
                                        label_name, x_min, x_max, y_min, y_max))
                                    print(
                                        CONFIG['LABEL_INFORMATION_MESSAGE'], image_id)
                        line = f.readline()

                    f.close()

        except TypeError as exception:
            sys.exit(str(exception))
