"""
Lesson 46
27.02.2024

- Разбор домашнего задания
- Подготовка базы данных для проекта Django (Карточки)
- Работа с Open AI API - написание серии функций
- Заполнение базы данных тегами для карточек


"""
import csv
import json
import time
from pprint import pprint

import openai
from openai import OpenAI
from settings import OPEN_AI_API_KEY
from typing import List, Dict
import sqlite3

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

# Ролевая модель ответа
ROLE_CONTENT = rf"""
    Ты эксперт по Пайтон, HTML, CSS, JS и отличный методист.
    Хорошо знаешь другие языки программирования, в том числе базы данных.\
    Язык ответа: русский, английский.
    """

# Задание
WRITER_TASK = rf"""
Просмотри данные которые я тебе отправил и сделай следующее:
1. Определи категорию для этой карточки (Python или SQL)
2. Определи теги для этой карточки. Придерживайся следующих правил:\
- Используй два языка. Русский и Английский для тегов.
- Английский язык: для названия технологий, категорий, ключевых слов и т.д.
- Русский язык: для общих, описательных, составных тегов
- Теги должны быть в нижнем регистре
- Теги должны быть без пробелов
- Теги должны быть уникальными
- Никаких решеток в тегах не должно быть
- В тегах допускается несколько слов - разделяй их нижним подчеркиванием
- ЧАСТЬ тегов должна быть ОБЩАЯ, а ЧАСТЬ - СПЕЦИФИЧНАЯ для данной карточки
- ИСПОЛЬЗУЙ категорию в тегах. Категорию пиши на английском языке

!!!НЕ МЕНЕЕ 2 ТЕГОВ И  БОЛЕЕ 6 ТЕГОВ ДЛЯ КАЖДОЙ КАРТОЧКИ.
!!!Ответ в виде JSON строки.
!!!Объект должен содержать ключи "category" и "tags".
"category" - строка, название категории.
"tags" - список строк, названия тегов. На РУССКОМ и английском языке.\
ИСПОЛЬЗУЙ ОПИСАННЫЕ МНОЙ ПРАВИЛА ДЛЯ ЯЗЫКА ТЕГОВ\
!!! НЕ ДЕЛАЙ СОСТАВНЫЕ ТЕГИ ИЗ английского и русского ЯЗЫКОВ НИКОГДА!!!!!\

Вот вопрос и ответ:\

"""

DB_PATH = '../../data/lesson_45.db'
RESULT_CSV = '../../data/cards_tags.csv'


def get_unique_cards(db_path: str) -> List[Dict[str, str]]:
    """
    Функция, которая позволяет получить уникальные вопросы и ответы из базы
    :param: db_path: путь к базе данных
    :return: List[Dict[str, str]]: список уникальных вопросов и ответов из базы данных
    """
    result = []
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT question, answer, CardID FROM Cards;")
        for row in cursor.fetchall():
            result.append({
                'question': row[0],
                'answer': row[1],
                'CardID': row[2],
            })
    return result


def append_tags_to_csv(data: Dict[str, str], csv_path: str):
    """
    Функция, которая позволяет добавить теги в csv файл. Запись просисходит поштучно
    Кодировка windows-1251, разделитель - ";"
    Line terminator - "\n"
    Столбцы - question, answer, category, tags
    tags - это список тегов в формате JSON строки

    :param data: Dict[str, str]: данные для записи
    :param csv_path: str: путь к csv файлу
    :return: None
    """
    with open(csv_path, 'a', newline='', encoding='windows-1251') as file:
        writer = csv.writer(file, delimiter=';', lineterminator='\n')
        writer = csv.DictWriter(file, fieldnames=data.keys(), delimiter=';',
                                lineterminator='\n')
        # writer.writeheader()
        writer.writerow(data)


def get_request_open_ai(system_role_content: str, role_content: str,
                        prompt: str, model: str, temperature: float, max_tokens: int,
                        system_role: str = 'system') -> dict:
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
            # print(f'\n{"-" * 20}\n'
            #       'Отправляем запрос в OpenAI API\n'
            #       f'Модель: {model}\n'
            #       f'{"-" * 20}\n')
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                response_format={"type": "json_object"}
            )
            break
        except openai.error.ServiceUnavailableError as e:
            print(f'{"-" * 20}\n'
                  f'Ошибка при отправке запроса в OpenAI API, {e}.\n'
                  'Попытка повторить запрос через 20 секунд'
                  f'{"-" * 20}\n')
            time.sleep(20)

    result = response.choices[0].message.content.strip()
    result_dict = json.loads(result)
    return result_dict


# Функция main, в которой будет чтение данных из базы, запрос в OpenAI и запись в CSV
def main():
    # Получаем уникальные вопросы и ответы из базы
    unique_cards = get_unique_cards(DB_PATH)
    count = 0
    len_task = len(unique_cards)

    # Проходимся по всем вопросам и ответам
    for card in unique_cards:
        # Формируем параметры запроса

        kwargs_dict = {
            'temperature': 0.6,
            'max_tokens': 500,
            'system_role_content': ROLE_CONTENT,
            'prompt': WRITER_TASK + '\n' + card.get('question').strip() + '\n' + card.get('answer').strip(),
            'model': 'gpt-4-0125-preview',
            'role_content': 'user',
            'system_role': 'system'
        }
        # pprint(kwargs_dict)
        # Запрос в OpenAI
        result = get_request_open_ai(**kwargs_dict)

        # Формируем словарь для записи в CSV
        final_result = {
            'CardID': card.get('CardID'),
            'category': result.get('category'),
            'tags': json.dumps(result.get('tags'), ensure_ascii=False)
        }
        #         pprint(f'\n\nФинальный результат: {final_result}')

        # Запись в CSV
        append_tags_to_csv(final_result, RESULT_CSV)

        count += 1
        print(f'{count} из {len_task} обработано и записано в CSV')


if __name__ == '__main__':
    main()
