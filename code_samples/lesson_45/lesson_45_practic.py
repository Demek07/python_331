"""
Практика по созданию БД для приложения интервального повторения карточек (Anki)

1. У нас уже есть БД и таблицы
2. Нам нужно получить данные
3. Нам нужно подготовить данные
4. Добавить данные в БД
"""

import re
import sqlite3
from lesson_45 import DB_PATH

SQL_CARDS_MD = '../../data/cards_sql.md'
PYTHON_DEV_CARDS_MD = '../../data/cards_python_dev.md'


# Простая функция для чтения файла
def read_card_from_md(file_path: str, sep='##'):
    """
    Генератор возвращающий по одной карточке
    :param file_path:
    :param sep:

    """
    with open(file_path, 'r', encoding='utf-8') as f:
        card = []
        for line in f:
            if line.startswith(sep + ' ') and card:
                yield ''.join(card)
                card = []
            card.append(line)

        if card:
            yield ''.join(card)


# Функция, которая примет 1 статью и вернет кортеж (question, answer)
"""
Функция будет готовить данные для БД

1. Убрать номер и точку и пробел ## 3. через try и regex
2. Убрать sep и пробел через try и regex 
3. Разделить на вопрос и ответ через
"""


def parse_article(article):
    # Убираем номер и точку и пробел в начале строки
    cleaned_article = re.sub(r'^## \d+\.\s*', '', article, flags=re.MULTILINE)

    # Разделяем вопрос и ответ через пустую строку после вопроса
    question_answer_split = re.split(r'\n\n', cleaned_article, maxsplit=1)

    if len(question_answer_split) == 2:
        question, answer = question_answer_split
        # Убираем 'sep и пробел' если они есть, но в приведенном примере это не требуется
        question = re.sub(r'sep\s*', '', question)
        answer = re.sub(r'sep\s*', '', answer)
        return (question.strip(), answer.strip())
    else:
        return "Вопрос не найден", "Ответ не найден"


if __name__ == '__main__':
    # Генератор возвращающий по одной карточке
    gen = read_card_from_md(SQL_CARDS_MD)

    # Будем коммитить по 10 строчек. Нужен счетчик
    counter = 0


    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        for row_card in gen:
            question, answer = parse_article(row_card)
            cursor.execute("INSERT INTO cards (question, answer) VALUES (?, ?)", (question, answer))
            # cursor.execute(f"INSERT INTO cards (question, answer) VALUES ('{question}', '{answer}')")
            counter += 1
            if counter == 10:
                counter = 0
                conn.commit()
        else:
            conn.commit()








