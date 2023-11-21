"""
Lesson 16
31.10.2023
Python331

1. Ответы на вопросы
- Павел. Дарья: Документация к функциям
- Анна: Цикл while - break, в функциях
2. Повторение материала
3. Аннотация типов. Type hinting
4. Встроенный модуль typing
"""

# Документация к функциям
# 1. Пишим функцию от начала до коцна
# 2. После двоеточия нажимаем Enter
# 3. Пишем """ + Enter
# 4. Вводим описание функции

#
# def sum_a_b(a, b, c):
#     """
#     Функция, которая принимает два числа и возвращает их сумму
#     :param a: Первое число
#     :param b: Второе число
#     :raises TypeError: Если в функцию переданы не числа
#     :return: Сумма двух чисел
#     """
#     if isinstance(a, (int, float)) and isinstance(b, (int, float)):
#         return a + b
#     else:
#         raise TypeError('Неправильный тип данных')


# break внутри while внутри функции

# def check_fruit_list(fruit_list, not_fruit_list):
#     """
#     Функция, которая проверяет что в списке фруктов есть только фрукты
#     :param fruit_list: Список фруктов
#     :param not_fruit_list: Список не фруктов
#     """
#     while fruit_list:
#         fruit = fruit_list.pop()
#         if fruit in not_fruit_list:
#             print(f'{fruit} - это не фрукт')
#             print('Делаю break')
#             break
#         else:
#             print(f'{fruit} - это фрукт')
#
#     else:
#         print('Все фрукты')
#

# return внутри while внутри функции (который работает как break)
# Включая конструкцию while - else

# def check_fruit_list_v2(fruit_list, not_fruit_list):
#     """
#     Функция, которая проверяет что в списке фруктов есть только фрукты
#     :param fruit_list: Список фруктов
#     :param not_fruit_list: Список не фруктов
#     """
#     while fruit_list:
#         fruit = fruit_list.pop()
#         if fruit in not_fruit_list:
#             return f'{fruit} - это не фрукт'
#     else:
#         return 'Все фрукты'

# def is_fruit(single_fruit, not_fruit_list):
#     """
#     Функция, которая проверяет что конкретный фрукт является фруктом
#     :param fruit_list: Конкретный фрукт
#     :param not_fruit_list: Список не фруктов
#     """
#     if single_fruit in not_fruit_list:
#         return True
#     else:
#         return False


# def main():
#     fruit_list = ['яблоко', 'банан', 'киви', 'арбуз', 'дыня']
#     not_fruit_list = ['помидор', 'огурец', 'капуста', 'картофель']
#
#     while fruit_list:
#         fruit = fruit_list.pop()
#         if is_fruit(fruit, not_fruit_list):
#             print(f'{fruit} - это не фрукт')
#             print('Делаю break')
#             break
#         else:
#             print(f'{fruit} - это фрукт')
#     else:
#         print('Все фрукты')


# main()


# Аннотация типов. Type hinting
# - При усложнении кода, становится сложно понять какие типы данных принимает функция
# - Пайчарм перестает давать подсказки методов и атрибутов
# - Мы можем случайно при передаче результатов одной функции через переменную в другую
# - Поместить то, что положет программу на лопатки :)

# Базовая аннотация типов данных
# :int - указываем что это integer - число
# :str - указываем что это строка
# :float - указываем что это число с плавающей точкой
# :bool - указываем что это булевое значение
# :list - указываем что это список
# :dict - указываем что это словарь
# :set - указываем что это множество
# :tuple - указываем что это кортеж
# :None - указываем что это None

# Аннотация типов для переменных

# a: int = '2'
# b: int = 2

# Аннотация типов для функций


# def sum_a_b_v2(a: int, b: int) -> float:  # - > (Без пробела) указываем что функция возвращает int
#     return a / b


# print(sum_a_b_v2(1, '2')) # Пайчарм подсказывает что передаем не тот тип данных
# num: dict = sum_a_b_v2(1, 2) # Пайчарм подсказывает что функция возвращает не тот тип данных

# str_num: str = '2'
# num: int = int(str_num)
# num_float: float = float(str_num)
# num_list: list = list(str_num)
# num_set: set = set(str_num)


# Args и kwargs в аннотации типов
# - *args - кортеж
# - **kwargs - словарь

# def sum_args(*args: int) -> int:
#     return sum(args)


# print(sum_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# TODO Практика
"""
Напишите функцию которая принимает один аргумент: строку
Возвращает bool - True если строка является палиндромом, False если нет
"""

# def is_palindrome(string: str) -> bool:
#     """
#     Функция, которая проверяет является ли строка палиндромом
#     :param string: Слово или фраза на проверку
#     :return: bool
#     """
#     return string == string[::-1]


# def check_list_palindrome(list_: list) -> bool:
#     result = True
#     while list_:
#         if not is_palindrome(list_.pop()):
#             result = False
#             break
#     return result
#
#
# words_list: list = ['шалаш', 'привет', 1]
# # Будет ошибка TypeError: 'int' object is not subscriptable
# # Потому что нельзя сделать срез числа 1
# print(check_list_palindrome(words_list))

# Встроенный модуль typing
# - Позволяет указывать аннотации типов для коллекций

# from typing import (List, Dict, Tuple, Set, Union,
#                     Optional, Any, Callable, Iterable, Iterator, Generator)
#
#
# def is_palindrome(string: str) -> bool:
#     """
#     Функция, которая проверяет является ли строка палиндромом
#     :param string: Слово или фраза на проверку
#     :return: bool
#     """
#     return string == string[::-1]
#
#
# def get_list_num() -> List[int]:
#     return [1, 2, 3, 4, 5]
#
#
# def check_list_palindrome2(list_: List[str]) -> bool:
#     result = True
#     while list_:
#         if not is_palindrome(list_.pop()):
#             result = False
#             break
#     return result
#
#
# result_a = get_list_num()
# result_b = check_list_palindrome2(result_a) # Пайчарм подсказывает что передаем не тот тип данных
#
# words_list = [1, 'привет']
# # Будет ошибка TypeError: 'int' object is not subscriptable
# print(check_list_palindrome2(words_list))

# pip install mypy
# List[str] - список строк
# Dict[str, int] - словарь с ключами строками и значениями int
# Tuple[str, int, float] - кортеж с элементами строка, int, float
# Set[str] - множество строк
# Union[str, int] - строка или int (или одно, или другое)
# | - это оператор Union
# Optional[str] - строка или None (или одно или НИЧЕГО)
# Any - любой тип данных (Когда не знаем что там)
# Callable - функция
# Iterable - итерируемый объект
# Iterator - итератор
# Generator - генератор
# object - любой объект


# product_list: List[str] = input('Введите список продуктов: ').split()
#
#
# def check_list_str(list_: List[str]) -> List[bool]:
#     result = []
#     while list_:
#         result.append(list_.pop().isalpha())
#     return result

# TODO Практика
"""
1. Импортировать в проект модуль typing
2. Установить mypy  pip install mypy
3. Написать type hinting для small_dict и full_dict
4. Попробовать сделать проверку через mypy
- Запускаем терминал
- Пишем команду: mypy имя_файла.py
"""
from typing import (List, Dict, Tuple, Set, Union,
                    Optional, Any)

from marvel import small_dict, full_dict

# Это не правильно
# small_dict_marvel: Dict[str, int] = small_dict

small_dict_marvel: Dict[str, Optional[int]] = small_dict
small_dict_marvel2: Dict[str, int | None] = small_dict
small_dict_marvel3: Dict[str, Union[int, None]] = small_dict

test: Dict[int, Dict[str, Union[str, int]]] = {
    0: {
        'title': 'Железный человек',
        'year': 2008,
        'director': 'Джон Фавро',
        'screenwriter': 'Марк Фергус и Хоук Остби, Артур Маркам и Мэтт Холлоуэй',
        'producer': 'Ави Арад и Кевин Файги',
        'stage': 'Первая фаза'
    },

    1: {
        'title': 'Железный человек',
        'year': 2008,
        'director': 'Джон Фавро',
        'screenwriter': 'Марк Фергус и Хоук Остби, Артур Маркам и Мэтт Холлоуэй',
        'producer': 'Ави Арад и Кевин Файги',
        'stage': 'Первая фаза'
    }}

# full_dict_marvel: Dict[int, Dict[str, Union[str, int]]] = full_dict

# pyinstaller
# pip install pyinstaller
# Упаковка в один файл
# pyinstaller имя_файла.py --onefile
# pwd - показывает текущую директорию
# ls - показывает содержимое директории
# cd - позволяет перейти в другую директорию


"""
Эта ошибка происходит, потому что mypy не может гарантировать, что вложенные словари 
будут иметь ожидаемую структуру, когда вы используете общий тип Dict.
"""

"""
Для отображения исключений при запуске exe файла, необходимо запускать его прямо из консоли.
Если запускать его двойным кликом мыши, то консоль закроется

Или, надо правильно прописать исключение :)))

У меня было json.JSONDecodeError (это не правильно)
Вместо json.decoder.JSONDecodeError (это правильно)

И запуск в консоли показал ошибку.
"""