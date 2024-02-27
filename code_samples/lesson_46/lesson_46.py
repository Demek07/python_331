"""
Lesson 46
27.02.2024

- Разбор домашнего задания
- Подготовка базы данных для проекта Django (Карточки)
- Работа с Open AI API - написание серии функций
- Заполнение базы данных тегами для карточек

openai==0.27.8???
"""
import time

import openai
from openai import OpenAI

from settings import OPEN_AI_API_KEY

DOLLAR_COURSE = 85
MODELS = {
    'gpt3.5':
        {
            'full_name': 'gpt-3.5-turbo-16k',
            'input': 0.003,
            'output': 0.004,
            'limit': 16000
        },
    'gpt4':
        {
            'full_name': 'gpt-4-0314',
            'input': 0.03,
            'output': 0.06,
            'limit': 8000
        },
    'gpt-4-32k':
        {
            'full_name': 'gpt-4-32k-0314',
            'input': 0.06,
            'output': 0.12,
            'limit': 32000
        },
    'gpt-4-128k':
        {
            'full_name': 'gpt-4-128k-0613',
            'input': 0.01,
            'output': 0.03,
            'limit': 127000
        }
}

ROLE_CONTENT = rf"""
    Ты эксперт по Пайтон, HTML, CSS, JS и отличный методист.\
    Хорошо знаешь другие языки программирования, в том числе базы данных.
    """

WRITER_TASK = rf"""
Просмотри данные которые я тебе отправил и сделай следующее:\
1. Определи категорию для этой карточки (Python или SQL)\
2. Определи теги для этой карточки. Придерживайся следующих правил:\
- Теги должны быть в нижнем регистре\\
- Теги должны быть без пробелов\\\
- Теги должны быть уникальными\\\
- Никаких решеток в тегах не должно быть\\\\
- В тегах допускается несколько слов - разделяй их нижним подчеркиванием\\\\

НЕ БОЛЕЕ 10 ТЕГОВ ДЛЯ КАЖДОЙ КАРТОЧКИ.\\

Ответ в виде JSON строки.\
Объект должен содержать ключи "category" и "tags".\\
"category" - строка, название категории.\\\
"tags" - список строк, названия тегов.\\\
"""




"""
Входные данные:
- Есть база данных карточек без тегов и категорий

Задача:
- Получить категории и теги

Желательно с минимальными финансовыми затратами,
используем минимальное количество токенов
GPT-3.5, для начала можно попробовать работать только с вопросами

1. Функция  get_unique_cards -> List[Dict[str, str]]:
result = [
    {"question": "Что такое PEP 8?"
    "answer": "PEP 8 — стандарт написания кода на Python."},
...........

Получить уникальные вопросы и ответы из базы

SELECT DISTINCT question, answer
from Cards

2. Функция get_ai_request(много параметров, request: str) -> Будем экспериментировать):

3. Функция get_ai_data(question: str, answer: str) -> Dict[str, List[str]|str]:
Использует функцию get_ai_request, чтобы получить ответы на вопросы

4. Записать данные хотя бы в CSV файл (по мере каждого запроса)
"""

from typing import List, Dict
import sqlite3

DB_PATH = '../../data/lesson_45.db'


# def get_unique_cards(db_path: str) -> List[Dict[str, str]]:
#     """
#     Функция, которая позволяет получить уникальные вопросы и ответы из базы
#     :param: db_path: путь к базе данных
#     :return: List[Dict[str, str]]: список уникальных вопросов и ответов из базы данных
#     """
#     result = []
#     with sqlite3.connect(db_path) as conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT DISTINCT question, answer FROM Cards")
#         for row in cursor.fetchall():
#             result.append({"question": row[0], "answer": row[1]})
#     return result
#
#
# print(get_unique_cards(DB_PATH))


# DB_PATH = 'lesson_46.db'
#
#
# def get_unique_cards(cursor: sqlite3.Cursor) -> list:
#     cursor.execute("SELECT DISTINCT question, answer FROM Cards")
#     rows_data = cursor.fetchall()
#     result = []
#     for row in rows_data:
#         result.append({"question": row[0], "answer": row[1]})
#
#     return result
#
#
# def main():
#     # Создаем подключение к БД
#     with sqlite3.connect(DB_PATH) as conn:
#         cursor = conn.cursor()
#     print(get_unique_cards(cursor))
#
#
# if __name__ == '__main__':
#     main()


def get_request_open_ai(system_role_content: str, role_content: str,
                        prompt: str, model: str, temperature: float, max_tokens: int,
                        system_role: str = 'system') -> str:
    """
    Функция для запроса в OpenAI используя новый API

    :param system_role: Это роль системы
    :param system_role_content: Это сообщение системы
    :param role_content: Это сообщение пользователя
    :param prompt: Это подсказка для модели
    :param model: Это модель
    :param temperature: Это температура (от 0 до 2)
    :param max_tokens: Это максимальное количество токенов
    :return: Возвращает ответ от openai
    """

    client = OpenAI(api_key=OPEN_AI_API_KEY)

    messages = [
        {"role": system_role, "content": system_role_content},
        {"role": "user", "content": role_content},
        {"role": "assistant", "content": prompt},
    ]

    # Отправляем запрос в OpenAI API
    while True:
        try:
            print(f'\n{"-" * 20}\n'
                  'Отправляем запрос в OpenAI API\n'
                  f'Модель: {model}\n'
                  f'{"-" * 20}\n')
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                # response_format="json" # Возвращаем ответ в формате JSON
            )
            break
        except openai.error.ServiceUnavailableError as e:
            print(f'{"-" * 20}\n'
                  f'Ошибка при отправке запроса в OpenAI API, {e}.\n'
                  'Попытка повторить запрос через 20 секунд'
                  f'{"-" * 20}\n')
            time.sleep(20)

    result = response.choices[0].message.content.strip()
    return result

    # json_result = json.dumps(response, ensure_ascii=False)
    # return json_result

# Тестируем функцию запроса в OpenAI

"""
result = get_request_open_ai(system_role_content=WRITER_ROLE_CONTENT,
                                             role_content='user',
                                             prompt=WRITER_TASK + '\n' + item,
                                             model=model,
                                             temperature=TEMPERATURE,
                                             system_role='system',
                                             max_token=max_tokens - tokens)
"""

kwargs_dict = {
    'temperature': 0.5,
    'max_tokens': 200,
    'system_role_content': ROLE_CONTENT,
    'prompt': WRITER_TASK + '\n' + 'Что такое PEP 8 в Python?',
    'model': 'gpt-3.5-turbo-16k',
    'role_content': 'user',
    'system_role': 'system'
}

print(get_request_open_ai(**kwargs_dict))