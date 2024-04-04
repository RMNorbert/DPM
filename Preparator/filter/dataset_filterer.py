import csv
from typing import List, Dict, Any
import os
from util.utils import *

CONFIG: Dict[str, Any] = load_configuration(
    './configuration/dataset_filter_configuration.yaml')


class DatasetFilterer:
    def __init__(self, csv_file_path_list: List[str], searched_label_list: List[str], image_list_file_path: str):
        self.csv_file_path_list: List[str] = csv_file_path_list
        self.searched_label_list: List[str] = searched_label_list
        self.image_list_file_path: str = image_list_file_path
        self.image_list_file_list: List[str] = []
        self.dataset_subset_list: List[str] = CONFIG['DATASET_SUBSET']

    @staticmethod
    def get_transformed_label_info(label_name, x_min, x_max, y_min, y_max) -> str:
        x1, x2, y1, y2 = float(x_min), float(x_max), float(y_min), float(y_max)
        xc, yc = (x1 + x2) / 2, (y1 + y2) / 2
        w, h = x2 - x1, y2 - y1
        return '{} {} {} {} {}\n'.format(label_name, xc, yc, w, h)

    def create_filtered_image_id_txt_file(self) -> None:
        try:
            for i, filename in enumerate(self.csv_file_path_list):
                with open(filename, 'r') as f:
                    for line in f:
                        image_id, _, label_name, _, x_min, x_max, y_min, y_max, _, _, _, _, _ = line.split(',')[
                            :13]
                        if label_name in self.searched_label_list and image_id not in self.image_list_file_list:
                            self.image_list_file_list.append(image_id)
                            with open(self.image_list_file_path, 'a') as fw:
                                fw.write(
                                    '{}/{}\n'.format(self.dataset_subset_list[i], image_id))
                                print(
                                    CONFIG['IMAGE_INFORMATION_MESSAGE'], image_id)
        except TypeError as exception:
            print(CONFIG['ERROR_MESSAGE_PREFIX'], exception)

    def create_filtered_image_id_txt_file_with_label_txt_file(self) -> None:
        for i, filename in enumerate(self.csv_file_path_list):
            with open(filename, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    try:
                        image_id, _, label_name, _, x_min, x_max, y_min, y_max, _, _, _, _, _ = row[
                            :13]
                        if label_name in self.searched_label_list and image_id not in self.image_list_file_list:
                            self.image_list_file_list.append(image_id)
                            image_info = '{}/{}\n'.format(
                                self.dataset_subset_list[i], image_id)
                            with open(self.image_list_file_path, 'a') as image_list_file:
                                image_list_file.write(image_info)
                                curr_img_label = os.path.join(
                                    '{}'.format(CONFIG['STORAGE_MAIN_FOLDER']),
                                    '{}{}{}.txt'.format(self.dataset_subset_list[i],
                                                        CONFIG['LABEL_STORAGE_FOLDER'],
                                                        image_id))
                                print(
                                    CONFIG['IMAGE_INFORMATION_MESSAGE'], image_id)

                                with open(curr_img_label, 'a') as label_file:
                                    label_file.write(self.get_transformed_label_info(
                                        label_name, x_min, x_max, y_min, y_max))
                                    print(
                                        CONFIG['LABEL_INFORMATION_MESSAGE'], image_id)

                    except Exception as e:
                        print(CONFIG['ERROR_MESSAGE_PREFIX'], e)
