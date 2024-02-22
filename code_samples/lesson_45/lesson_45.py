"""
Lesson 45
22.02.2024

1. Знакомство с Sqlite3
2. import sqlite3
3. Основные объекты sqlite3
- Objects: Connection, Cursor
4. Основные методы объектов sqlite3
- Methods: connect(), cursor(), executescript(), execute(), fetchone(), fetchall()
"""

# Импортируем модуль sqlite3
import sqlite3

DB_PATH = '../../data/lesson_45.db'
SQL_SCRIPT_PATH = 'lesson_45.sql'

"""
Три варианта выполнения запросов:
1. cursor.execute() - выполнение одного запроса
2. cursor.executemany() - выполнение одного запроса много раз
3. cursor.executescript() - выполнение нескольких запросов (разделенных точкой с запятой)
"""


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



def main():
    # Создаем подключение к БД
    conn = sqlite3.connect(DB_PATH)

    # Создаем курсор - это специальный объект, который делает запросы и получает их результаты
    cursor = conn.cursor()

    # Читаем SQL скрипт из файла
    sql_script = read_sql_script(SQL_SCRIPT_PATH)

    # Выполняем SQL скрипт
    execute_sql_script(cursor, conn, sql_script)

    # Закрываем соединение
    conn.close()


if __name__ == '__main__':
    main()
