"""
Привет!

Это будет продолжение урока №47
На нем мы сделали следующие вещи

1. Прочитали данные из csv файла
2. Получили уникальные категории и теги
3. Записали данные в БД
---
Добавил функцию которая делает множественный запрос через executemany)
Убрал уникальность для вопросов (выяснили, что это не нужно)
"""


import csv
import json
from pprint import pprint

import sqlite3


CSV_PATH = 'data/cards_tags.csv'
DB_PATH = 'data/lesson_47.db'
OLD_DB_PATH = 'data/lesson_45.db'



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


QUERY_ADD_TAGS = "INSERT INTO Tags (Name) VALUES (?);"
QUERY_ADD_CATEGORIES = "INSERT INTO Categories (Name) VALUES (?);"


def execute_many_query(query: str, data_for_execute: list):
    """
    Функция, которая позволяет выполнить множественный запрос
    :param query: str: запрос
    :param data_for_execute: list: данные для выполнения запроса
    :return: None
    """
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.executemany(query, data_for_execute)


# Добавляем теги
# tags_data = [(tag,) for tag in row_tags]
# execute_many_query(QUERY_ADD_TAGS, tags_data)

# Добавляем категории
# categories_data = [(category,) for category in categories]
# execute_many_query(QUERY_ADD_CATEGORIES, categories_data)


def get_data_from_db(query: str, db_path: str) -> list:
    """
    Функция, которая позволяет получить данные из БД
    :param query: str: запрос
    :return: List[Dict[str, Union[int, str]]]: список данных
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()


# Получаем данные из старой БД
old_data = get_data_from_db("SELECT CardID, question, answer FROM Cards", OLD_DB_PATH)
pprint(old_data)

"""
Пример CSV

 {'CardID': '449',
  'category': 'SQL',
  'tags': '["курсор", "база_данных", "работа_с_записями", "declare", "open", '
          '"fetch", "close", "deallocate", "sql"]'},
"""

# Расширяем data (добавляем вопросы и ответы)
for row in data:
    for old_row in old_data:
        if int(row['CardID']) == int(old_row[0]):
            row['question'] = old_row[1]
            row['answer'] = old_row[2]


# Делаем запрос на вставку данных в таблицу, с подзапросом на поиск ID категории
QUERY_ADD_CARDS = """
INSERT INTO Cards (Question, Answer, CategoryID)
SELECT ?, ?, CategoryID
FROM Categories
WHERE Name = ?;
"""

# Готовим данные для вставки
cards_data = [(row['question'], row['answer'], row['category']) for row in data]

# Выполняем запрос
execute_many_query(QUERY_ADD_CARDS, cards_data)


# 