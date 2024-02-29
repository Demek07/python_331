"""
Lesson 47
29.02.2024
"""

"""
Функция 1. get_data_from_csv(file_path: str) -> List[Dict[str, Union[int, str]]]:
Функция 2. parse_unique_data_by_key(data: List[Dict[str, Union[int, str]]], key: str) -> Set[str]:
"""

import csv, json, sqlite3
from pprint import pprint

CSV_PATH = '../../data/cards_tags.csv'
DB_PATH = '../../data/lesson_47.db'
OLD_DB_PATH = '../../data/lesson_45.db'


def get_data_from_csv(file_path: str) -> list:
    """
    Функция, которая позволяет получить данные из csv файла
    :param file_path: путь к csv файлу
    :return: List[Dict[str, Union[int, str]]]: список данных из csv файла
    """

    with open(file_path, 'r', newline='', encoding='windows-1251') as file:
        reader = csv.DictReader(file, delimiter=';', lineterminator='\n')
        return list(reader)



def parse_unique_data_by_key(data: list, key: str) -> set:
    """
    Функция, которая позволяет получить уникальные значения из списка словарей по ключу
    :param data: List[Dict[str, Union[int, str]]]: список данных
    :param key: str: ключ
    :return: set: уникальные значения
    """
    return {row[key] for row in data}


