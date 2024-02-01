"""
Посмотреть pytest.assume - Почему module pytest has no attribute assume


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
from random import randint as random
import pytest

txt_file_path = "../data/generator_text.txt"


def read_lines_file(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        for line in file:
            yield line.strip()


generator = read_lines_file(txt_file_path)
# # встречается ли слово тор в строке

word = input('введите слово для поиска: ')
if any(word.lower() in line.lower() for line in read_lines_file(txt_file_path)):
    print(f"{word} есть в строках")
else:
    print(f"{word} нет в строках")

spisok = list(line for line in generator if word.lower() in line.lower())
print(spisok)
print(len(spisok))

spisok1 = list(line for line in read_lines_file(txt_file_path) if word.lower() in line.lower())
print(spisok1)
print(len(spisok1))