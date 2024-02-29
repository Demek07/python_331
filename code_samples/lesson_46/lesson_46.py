"""
Lesson 46
27.02.2024

- Разбор домашнего задания
- Подготовка базы данных для проекта Django (Карточки)
- Работа с Open AI API - написание серии функций
- Заполнение базы данных тегами для карточек

openai==0.27.8???
"""
import json
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
    Ты эксперт по Пайтон, HTML, CSS, JS и отличный методист.
    Хорошо знаешь другие языки программирования, в том числе базы данных.\
    Язык ответа: русский, английский.
    """

WRITER_TASK = rf"""
Просмотри данные которые я тебе отправил и сделай следующее:
1. Определи категорию для этой карточки (Python или SQL)
2. Определи теги для этой карточки. Придерживайся следующих правил:\
- Используй два языка. Русский и Английский для тегов.
- Английский язык: для названия технологий, категорий, ключевых слов и т.д.
- Русский язык: для общих, описательных, составных тегов, вроде "лучшие практики", "базы данных" и т.д.
- Теги должны быть в нижнем регистре
- Теги должны быть без пробелов
- Теги должны быть уникальными
- Никаких решеток в тегах не должно быть
- В тегах допускается несколько слов - разделяй их нижним подчеркиванием
- ЧАСТЬ тегов должна быть ОБЩАЯ, а ЧАСТЬ - СПЕЦИФИЧНАЯ для данной карточки
- ИСПОЛЬЗУЙ категорию в тегах. Категорию пиши на английском языке

!!!НЕ МЕНЕЕ 4 ТЕГОВ И  БОЛЕЕ 10 ТЕГОВ ДЛЯ КАЖДОЙ КАРТОЧКИ.
!!!Ответ в виде JSON строки.
!!!Объект должен содержать ключи "category" и "tags".
"category" - строка, название категории.
"tags" - список строк, названия тегов. На РУССКОМ и английском языке.\
ИСПОЛЬЗУЙ ОПИСАННЫЕ МНОЙ ПРАВИЛА ДЛЯ ЯЗЫКА ТЕГОВ\
!!! НЕ ДЕЛАЙ СОСТАВНЫЕ ТЕГИ ИЗ РАЗНЫХ ЯЗЫКОВ НИКОГДА!!!!!\

Вот вопрос и ответ:\

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

QESTION = "## Что делает оператор `EXPLAIN`?"
ANSWER = """
```sql
EXPLAIN имя_таблицы
EXPLAIN SELECT опции_выборки
```

Если оператор SELECT предваряется ключевым словом EXPLAIN, MySQL сообщит о том, как будет производиться обработка SELECT, и предоставит информацию о порядке и методе связывания таблиц.

При помощи EXPLAIN можно выяснить, когда стоит снабдить таблицы индексами, чтобы получить более быструю выборку, использующую индексы для поиска записей. Кроме того, можно проверить, насколько удачный порядок связывания таблиц был выбран оптимизатором. Заставить оптимизатор связывать таблицы в заданном порядке можно при помощи указания STRAIGHT_JOIN.

Для непростых соединений EXPLAIN возвращает строку информации о каждой из использованных в работе оператора SELECT таблиц. Таблицы перечисляются в том порядке, в котором они будут считываться. MySQL выполняет все связывания за один проход (метод называется "single-sweep multi-join"). Делается это так: MySQL читает строку из первой таблицы, находит совпадающую строку во второй таблице, затем - в третьей, и так далее. Когда обработка всех таблиц завершается, MySQL выдает выбранные столбцы и обходит в обратном порядке список таблиц до тех пор, пока не будет найдена таблица с наибольшим совпадением строк. Следующая строка считывается из этой таблицы и процесс продолжается в следующей таблице.

```sql
********************** 1. row **********************
id: 1
select_type: SIMPLE
table: categories
type: ALL
possible_keys: NULL
key: NULL
key_len: NULL
ref: NULL
rows: 4
Extra:
1 row in set (0.00 sec)
```

- id – порядковый номер для каждого SELECT’а внутри запроса (когда имеется несколько подзапросов)
  select_type – тип запроса SELECT.

- SIMPLE — Простой запрос SELECT без подзапросов или UNION’ов
- PRIMARY – данный SELECT – самый внешний запрос в JOIN’е
- DERIVED – данный SELECT является частью подзапроса внутри FROM
- SUBQUERY – первый SELECT в подзапросе
- DEPENDENT SUBQUERY – подзапрос, который зависит от внешнего запроса
- UNCACHABLE SUBQUERY – не кешируемый подзапрос (существуют определенные условия для того, чтобы запрос кешировался)
- UNION – второй или последующий SELECT в UNION’е
- DEPENDENT UNION – второй или последующий SELECT в UNION’е, зависимый от внешнего запроса
- UNION RESULT – результат UNION’а

- Table – таблица, к которой относится выводимая строка
- Type — указывает на то, как MySQL связывает используемые таблицы. Это одно из наиболее полезных полей в выводе потому, что может сообщать об отсутствующих индексах или почему написанный запрос должен быть пересмотрен и переписан.
  Возможные значения:

- System – таблица имеет только одну строку
- Const – таблица имеет только одну соответствующую строку, которая проиндексирована. Это наиболее быстрый тип соединения потому, что таблица читается только один раз и значение строки может восприниматься при дальнейших соединениях как константа.
- Eq_ref – все части индекса используются для связывания. Используемые индексы: PRIMARY KEY или UNIQUE NOT NULL. Это еще один наилучший возможный тип связывания.
- Ref – все соответствующие строки индексного столбца считываются для каждой комбинации строк из предыдущей таблицы. Этот тип соединения для индексированных столбцов выглядит как использование операторов = или < = >
- Fulltext – соединение использует полнотекстовый индекс таблицы
- Ref_or_null – то же самое, что и ref, но также содержит строки со значением null для столбца
- Index_merge – соединение использует список индексов для получения результирующего набора. Столбец key вывода команды EXPLAIN будет содержать список использованных индексов.
- Unique_subquery – подзапрос IN возвращает только один результат из таблицы и использует первичный ключ.
- Index_subquery – тоже, что и предыдущий, но возвращает более одного результата.
- Range – индекс, использованный для нахождения соответствующей строки в определенном диапазоне, обычно, когда ключевой столбец сравнивается с константой, используя операторы вроде: BETWEEN, IN, >, >=, etc.
- Index – сканируется все дерево индексов для нахождения соответствующих строк.
- All – Для нахождения соответствующих строк используются сканирование всей таблицы. Это наихудший тип соединения и обычно указывает на отсутствие подходящих индексов в таблице.

- Possible_keys – показывает индексы, которые могут быть использованы для нахождения строк в таблице. На практике они могут использоваться, а могут и не использоваться. Фактически, этот столбец может сослужить добрую службу в деле оптимизации запросов, т.к значение NULL указывает на то, что не найдено ни одного подходящего индекса .
- Key– указывает на использованный индекс. Этот столбец может содержать индекс, не указанный в столбце possible_keys. В процессе соединения таблиц оптимизатор ищет наилучшие варианты и может найти ключи, которые не отображены в possible_keys, но являются более оптимальными для использования.
- Key_len – длина индекса, которую оптимизатор MySQL выбрал для использования. Например, значение key_len, равное 4, означает, что памяти требуется для хранения 4 знаков. На эту тему вот cсылка
- Ref – указываются столбцы или константы, которые сравниваются с индексом, указанным в поле key. MySQL выберет либо значение константы для сравнения, либо само поле, основываясь на плане выполнения запроса.
- Rows – отображает число записей, обработанных для получения выходных данных. Это еще одно очень важное поле, которое дает повод оптимизировать запросы, особенно те, которые используют JOIN’ы и подзапросы.
- Extra – содержит дополнительную информацию, относящуюся к плану выполнения запроса. Такие значения как “Using temporary”, “Using filesort” и т.д могут быть индикатором проблемного запроса. С полным списком возможных значений вы можете ознакомиться здесь
```

В этом примере функция my_func() принимает один аргумент и определяет две локальные переменные (a и z). Когда она вызывается, она выводит на экран словари глобальных и локальных переменных.
"""

kwargs_dict = {
    'temperature': 1,
    'max_tokens': 2000,
    'system_role_content': ROLE_CONTENT,
    'prompt': WRITER_TASK + '\n' + QESTION + '\n' + ANSWER,
    'model': 'gpt-3.5-turbo-0125',
    'role_content': 'user',
    'system_role': 'system'
}

print(get_request_open_ai(**kwargs_dict))