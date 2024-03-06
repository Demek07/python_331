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
from pprint import pp, pprint

import sqlite3

from regex import F


CSV_PATH = "data/cards_tags.csv"
DB_PATH = "data/lesson_47.db"
OLD_DB_PATH = "data/lesson_45.db"


def get_data_from_csv(file_path: str) -> list:
    """
    Функция, которая позволяет получить данные из csv файла
    :param file_path: путь к csv файлу
    :return: List[Dict[str, Union[int, str]]]: список данных из csv файла
    """

    with open(file_path, "r", newline="", encoding="windows-1251") as file:
        reader = csv.DictReader(file, delimiter=";", lineterminator="\n")
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
    unique_json_string_list = parse_unique_data_by_key(
        data, key
    )  # {'["python", "питон", "язык_программирования"]'}

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
categories = parse_unique_data_by_key(data, "category")
row_tags = parse_unique_data_by_key(data, "tags")


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
# pprint(old_data)

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
        if int(row["CardID"]) == int(old_row[0]):
            row["question"] = old_row[1]
            row["answer"] = old_row[2]


# Делаем запрос на вставку данных в таблицу, с подзапросом на поиск ID категории
QUERY_ADD_CARDS = """
INSERT INTO Cards (Question, Answer, CategoryID)
SELECT ?, ?, CategoryID
FROM Categories
WHERE Name = ?;
"""

# Готовим данные для вставки
cards_data = [(row["question"], row["answer"], row["category"]) for row in data]

# Выполняем запрос
# execute_many_query(QUERY_ADD_CARDS, cards_data)


# ФОРМИРУЕМ МНОГИЕ-КО-МНОГИМ Карточки-Теги

# Шаг 1. Прочитать CSV файл (done)
# Шаг 2. Получить Теги

tags_mappint_query = "SELECT Name, TagID FROM Tags"
tags_mapping = get_data_from_db(tags_mappint_query, DB_PATH)

# Шаг 3. Подготовка данных
cards_tags_data = []

# Обходим данные из CSV файла
for row in data:
    card_id = row["CardID"]
    tags = json.loads(row["tags"])  # Преобразуем строку в список
    # В каждой строке CSV файла обходим теги
    for tag in tags:
        # В каждом теге ищем его ID
        for tag_row in tags_mapping:
            if tag_row[0] == tag:
                tag_id = int(tag_row[1])
                cards_tags_data.append((card_id, tag_id))


# pprint(cards_tags_data)

# Шаг 4. Готовим запрос
QUERY_ADD_CARDS_TAGS = "INSERT INTO CardTags (CardID, TagID) VALUES (?, ?);"

# Шаг 5. Выполняем запрос
# execute_many_query(QUERY_ADD_CARDS_TAGS, cards_tags_data)

# Шаг 6. Проверяем результат функция получения полной информации по карточке по ID
# Получаем полную информацию по карточке по ID


def get_card_details(card_id, db_path):
    """
    Получает детали карточки по ее ID из базы данных SQLite.

    :param card_id: Идентификатор карточки для поиска.
    :param db_path: Путь к файлу базы данных SQLite.
    :return: Словарь с деталями карточки.
    """
    query = """
    SELECT 
        Cards.CardID, 
        Cards.Question, 
        Cards.Answer, 
        Categories.Name AS CategoryName,
        GROUP_CONCAT(Tags.Name, ', ') AS Tags
    FROM 
        Cards
    LEFT JOIN 
        Categories ON Cards.CategoryID = Categories.CategoryID
    LEFT JOIN 
        CardTags ON Cards.CardID = CardTags.CardID
    LEFT JOIN 
        Tags ON CardTags.TagID = Tags.TagID
    WHERE 
        Cards.CardID = ?
    GROUP BY 
        Cards.CardID, Cards.Question, Cards.Answer, Categories.Name;
    """

    # Подключение к базе данных и выполнение запроса
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query, (card_id,))
        result = cursor.fetchone()

    # Проверка на случай, если результат не найден
    if not result:
        return None

    # Преобразование результата в словарь
    card_details = {
        "CardID": result[0],
        "Question": result[1],
        "Answer": result[2],
        "CategoryName": result[3],
        "Tags": result[4].split(", ") if result[4] else [],
    }

    return card_details


# Пример использования функции
card_id = 5
card_details = get_card_details(card_id, DB_PATH)
pprint(card_details, sort_dicts=False)
