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

# Создаем подключение к БД
conn = sqlite3.connect(DB_PATH)

# Создаем курсор - это специальный объект, который делает запросы и получает их результаты
cursor = conn.cursor()

"""
Три варианта выполнения запросов:
1. cursor.execute() - выполнение одного запроса
2. cursor.executemany() - выполнение одного запроса много раз
3. cursor.executescript() - выполнение нескольких запросов (разделенных точкой с запятой)
"""

