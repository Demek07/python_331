"""
Lesson 39
- Разбор домашнего задания
- Повторение материала
    - @pytest.mark.parametrize
    - @pytest.mark.xfail
    - @pytest.raises
    - @pytest.fixture
    - @pytest.fixture(scope='module')



- Моки?
- @pytest.mark.slow - маркировка тестов
- Вспоминаем генераторы и yield
- Фикстуры и yield
- Разбор тестов с фикстурами + yield
- Тестовые классы
-
"""
import os
import sqlite3

import pytest

DB_PATH = "marvel_not_normal.db"
SQL_FILE = "hw_32.sql"

TABLES = [
    'Sex',
    'EyeColor',
    'HairColor',
    'Alignment',
    'LivingStatus',
    'Identity',
    'MarvelCharacters'
]
COLUMNS_MARVEL_CHARACTERS = [
    'id',
    'page_id',
    'name',
    'urlslug',
    'identity_id',
    'align_id',
    'eye_id',
    'hair_id',
    'sex_id',
    'status_id',
    'APPEARANCES',
    'FIRST_APPEARANCE',
    'Year'
]


def test_db_exists():
    assert os.path.exists(DB_PATH), f"Файл БД {DB_PATH} не найден"


# Измененная фикстура для управления транзакциями
@pytest.fixture(scope="module")
def conn():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("BEGIN")
    yield connection
    connection.rollback()
    connection.close()


def test_sql_queries(conn):
    with open(SQL_FILE, 'r', encoding='utf-8') as f:
        sql_queries = f.read()
    conn.executescript(sql_queries)


@pytest.mark.parametrize("table_name", TABLES)
def test_table_exists(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
    assert cursor.fetchone() is not None, f"Таблица {table_name} не найдена"


@pytest.mark.parametrize("column", COLUMNS_MARVEL_CHARACTERS)
def test_marvel_characters_table_columns(conn, column):
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info(MarvelCharacters);")
    columns = [info[1] for info in cursor.fetchall()]
    assert column in columns, f"Поле {column} не найдено в таблице MarvelCharacters"
