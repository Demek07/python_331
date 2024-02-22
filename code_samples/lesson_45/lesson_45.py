"""
# TODO Почему добавилась карточка с user_id = 2 когда в таблице юзеров такого id нет?
# Чем по факту является DATETIME в sqlite? Почему этого нет в документации но есть в SQLitestudio
conn.execute("PRAGMA foreign_keys = ON;") - включает поддержку внешних ключей

Lesson 45
22.02.2024

1. Знакомство с Sqlite3
2. import sqlite3
3. Основные объекты sqlite3
- Objects: Connection, Cursor
4. Основные методы объектов sqlite3
- Methods:
connect() - создает подключение к БД
cursor() - объект курсора для выполнения запросов
executescript() - выполнение нескольких запросов (разделенных точкой с запятой)
execute() - выполнение одного запроса
fetchone() - получение одной строки (если их больше - вернет первую)
fetchall() - получение всех строк


-- Создаем таблицу с карточками
CREATE TABLE Cards (
    CardID INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    user_id INTEGER DEFAULT(1),
    upload_date DATETIME DEFAULT(datetime('now')),
    views INTEGER DEFAULT(0),
    adds INTEGER DEFAULT(0),
    FOREIGN KEY (user_id) REFERENCES Users(UserID)
);
"""

# Импортируем модуль sqlite3
import sqlite3

DB_PATH = '../../data/lesson_45.db'
SQL_SCRIPT_PATH = 'lesson_45.sql'

CARDS = [
    ('Пайтон или Питон?', 'Пайтон', 1),
    ('Жава Скрипт или Джаба Скрипт?', 'Джава Скрипт!', 2),
]

"""
Три варианта выполнения запросов:
1. cursor.execute() - выполнение одного запроса
2. cursor.executemany() - выполнение одного запроса много раз
3. cursor.executescript() - выполнение нескольких запросов (разделенных точкой с запятой)
"""


# Функция с использованием контекстоного менеджера для работы с базой данных
def read_sql_script(db_path: str, query: str):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()


def read_sql_script(file_path: str) -> str:
    """
    Читает SQL скрипт из файла
    :param file_path: путь к файлу
    :return: содержимое файла
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def execute_sql_script(cursor: sqlite3.Cursor, conn: sqlite3.Connection, sql_script: str):
    """
    Выполняет SQL скрипт
    :param cursor: курсор
    :param sql_script: SQL скрипт
    """
    cursor.executescript(sql_script)
    conn.commit()


def execute_one_query(cursor: sqlite3.Cursor, query: str):
    """
    Выполняет один запрос
    :param cursor: курсор
    :param query: запрос
    """
    cursor.execute(query)


def execute_many_query(cursor: sqlite3.Cursor, query: str, data: list):
    """
    Выполняет один запрос много раз
    :param cursor: курсор
    :param query: запрос
    :param data: данные
    """
    cursor.executemany(query, data)


def get_card_dict_by_row(row_data: tuple) -> dict:
    """
    Преобразует данные из строки в словарь
    :param row_data: данные из строки
    :return: словарь
    """
    return {
        'CardID': row_data[0],
        'question': row_data[1],
        'answer': row_data[2],
        'user_id': row_data[3],
        'upload_date': row_data[4],
        'views': row_data[5],
        'adds': row_data[6],
    }


def get_card_by_id(cursor: sqlite3.Cursor, card_id: int):
    """
    Получает карточку по ID
    :param cursor: курсор
    :param card_id: ID карточки
    :return: карточка
    """
    cursor.execute(f"SELECT * FROM Cards WHERE CardID = {card_id}")
    row_data = cursor.fetchone()
    result_dict = get_card_dict_by_row(row_data)
    return result_dict


def get_all_cards(cursor: sqlite3.Cursor):
    """
    Получает все карточки
    :param cursor: курсор
    :return: список карточек
    """
    cursor.execute("SELECT * FROM Cards")
    rows_data = cursor.fetchall()
    print(rows_data)
    result = [get_card_dict_by_row(row) for row in rows_data]
    return result


def main():
    # Создаем подключение к БД
    with sqlite3.connect(DB_PATH) as conn:

        # Создаем курсор - это специальный объект, который делает запросы и получает их результаты
        cursor = conn.cursor()

        # Читаем SQL скрипт из файла
        sql_script = read_sql_script(SQL_SCRIPT_PATH)

        # Выполняем SQL скрипт
        # execute_sql_script(cursor, conn, sql_script)

        # Выполняем один запрос - обновим таблицу Users добавим FirstName
        user_name = 'Дмитрий'
        query_add_user = f"INSERT INTO Users (FirstName) VALUES ('{user_name}')"

        # execute_one_query(cursor, query_add_user)

        # Commit
        # conn.commit()

        # Выполняем один запрос - добавим карточки
        query_add_card = "INSERT INTO Cards (question, answer, user_id) VALUES (?, ?, ?)"
        # execute_many_query(cursor, query_add_card, CARDS)

        # conn.commit()

        print(get_card_by_id(cursor, 2))
        print(get_all_cards(cursor))

        # Закрываем соединение (Уже не надо - мы в контекстном менеджере)



if __name__ == '__main__':
    main()
