"""
Lesson 47
29.02.2024
"""
from typing import List, Union, Dict, Set

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

csv_list_list = [
    ['id', 'category', 'tags'],
    ['1', 'python', '["python", "питон", "язык_программирования"]'],
]

csv_list_dict = [
    {'id': '1', 'category': 'python', 'tags': '["python", "питон", "язык_программирования"]'},
]




def parse_unique_data_by_key(data: list, key: str) -> set:
    """
    Функция, которая позволяет получить уникальные значения из списка словарей по ключу
    :param data: List[Dict[str, Union[int, str]]]: список данных
    :param key: str: ключ
    :return: set: уникальные значения
    """
    return {row[key] for row in data}



def parse_tags_by_json_string(data: list, key: str) -> set:
    """
    Функция, которая позволяет получить уникальные значения из списка словарей по ключу
    :param data: List[Dict[str, Union[int, str]]]: список данных
    :param key: str: ключ
    :return: set: уникальные значения
    """
    unique_json_string_list = parse_unique_data_by_key(data, key) # {'["python", "питон", "язык_программирования"]'}

    # Сет для хранения уникальных значений
    result = set()
    # Обходим список уникальных JSON строк
    for json_string in unique_json_string_list:
        # Преобразуем строку в список
        data = json.loads(json_string)

        # Обновляем сет. Метод update() добавляет элементы из другой коллекции
        result.update(data)

    return result


# Тестирование 2х функций
# Получаем данные из csv файла
data = get_data_from_csv(CSV_PATH)
# Получаем уникальные категории
categories = parse_unique_data_by_key(data, 'category')
row_tags = parse_unique_data_by_key(data, 'tags')

# Обходим row_tags и преобразуем строку в список, каждый элемент которой вкладыавем в сет

set_tags = {tag for tag in {tag for row in row_tags for tag in json.loads(row)}} # Это работает, но оно излишнее
set_tags_2 = parse_tags_by_json_string(data, 'tags')
set_tag_3 = {tag for row in row_tags for tag in json.loads(row)}

# pprint(categories)
# pprint(row_tags)
# pprint(set_tags_2)
# pprint(data)
# pprint(set_tag_3)

print(len(set_tags), len(set_tags_2), len(set_tag_3))


def get_data_from_csv(file_path: str) -> List[Dict[str, Union[int, str]]]:
    """
    Читает CSV файл (Вариант от Дмитрия)
    :param file_path: путь к файлу
    :return: возвращает содержимое файла
    """
    data_dict = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            card_id = row['CardID']
            category = row['category']
            tags = json.loads(row['tags'])
            data_dict[card_id] = {'card_id': card_id, 'category': category, 'tags': tags}

    # print(data_dict.values())
    return list(data_dict.values())


def parse_unique_data_by_key(data: List[Dict[str, Union[int, str]]], key: str) -> Set[str]:
    """
    Получает уникальные значения из списка словарей по ключу (Вариант от Дмитрия)
    :param data:
    :param key:
    :return:
    """
    tags = []
    for row in data:
        tags = tags + row.get(key)
    return set(tags)



