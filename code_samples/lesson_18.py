"""
Lesson 17
07.11.2023
Python331

1. Анонимные функции
- Что такое lambda функции
- Синтаксис
- Огранчения
- Где используются
2. Map. Filter. Sorted
"""
from pprint import pprint
from typing import List, Optional, Dict, Union


# Анонимные функции. Lambda функции
# - Пишется в одну строку
# - Не имеет имени
# - Не имеет return
# - Нет возможности написать несколько return
# - Не имеет документации

def get_sum(a, b):
    return a + b


lambda_get_sum: callable = lambda a, b: a + b

# Вызов обычной функции
print(get_sum(1, 2))

# Вызов lambda функции
print(lambda_get_sum(1, 2))

# Map - применяет функцию к каждому элементу итерируемого объекта

str_nums_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Через цикл for
nums_list = []
for num in str_nums_list:
    nums_list.append(int(num))

# Через comprehension
nums_list2 = [int(num) for num in str_nums_list]

# Через map
nums_list3 = list(map(int, str_nums_list))

# Map возвращает map object - это итерируемый объект
print(map(int, str_nums_list))
print(type(map(int, str_nums_list)))

map_obj = map(int, str_nums_list)
# Next
print(next(map_obj))
print(next(map_obj))

# Когда мы помещаем map в list, он полностью просчитывается и превращается в список
print(nums_list3)


# Пишем более сложную функцию для применения в цикле

# Применяем int и возводим в квадрат, если это число, если нет, None
def square_if_num(str_num: str) -> int | None:
    """
    Возводит число в квадрат, если это число, если нет, возвращает None
    :param str_num: Строка
    :return: Или число в квадрате, или None
    """
    if str_num.isdigit():
        num = int(str_num)
        return num ** 2
    else:
        return None


str_nums_list = ['1', '2', '3', '4', 'ыа', '6', '7', '8', '9', 'ыа']
# Эта же функция в виде lambda
square_lambda = lambda str_num: int(str_num) ** 2 if str_num.isdigit() else None

# Через map с обычной функцией
nums_list4 = list(map(square_if_num, str_nums_list))
print(nums_list4)

# Через map с lambda
# Optional - это тип данных, который может быть или int, или None
nums_list5: List[Optional[int]] = list(
    map(lambda str_num: int(str_num) ** 2 if str_num.isdigit() else None, str_nums_list))


def str_list_concat_v(str_list: List[str]) -> str:
    """
    Функция, которая принимает список строк и возвращает строку, в которой все элементы списка объединены через пробел
    :param str_list: Список строк
    :return: Строка
    """
    return ' '.join(str_list)


# result = str_list_concat_v(nums_list5)

# Список кортежей с двумя числами. 10 пар чисел
nums_list6 = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

# TODO Практика. 10 минут
"""
При помощи map и lambda функции, получите список состоящий из суммы чисел в каждом кортеже

"""

# Вариант через for
result_list0 = []
for num1, num2 in nums_list6:
    result_list0.append(num1 + num2)

# Вариант через List Comprehension
result_list1 = [num1 + num2 for num1, num2 in nums_list6]

# Вариант через map и lambda
result_list2 = list(map(lambda nums: nums[0] + nums[1], nums_list6))

# Вариант через lambda sum + comprehension
result_list2_1 = [sum(nums) for nums in nums_list6]

# Вариант через map lambda и sum
result_list3 = list(map(lambda nums: sum(nums), nums_list6))

# Вариант через цикл for и sum
result_list4 = []
for nums in nums_list6:
    result_list4.append(sum(nums))

# Filter - фильтрует итерируемый объект по условию
# filter(function, iterable)
# Фильтр возвращает filter object - это итерируемый объект

# Функция для фильтрации должна возвращать bool
names_lst: List[str] = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша',
                        'Даша', 'Вика', 'Нина', 'Аня', 'Витя', 'Валера']


# Функция для фильтрации (строки где есть буква а - регистронезависимая проверка)

def filter_a(name: str) -> bool:
    """
    Функция, которая проверяет есть ли в строке буква а
    :param name: Строка
    :return: bool
    """
    return 'а' in name.lower()


filtered_names_a: List[str] = list(filter(filter_a, names_lst))
print(filtered_names_a)

# Это же на lambda
filtered_names_a2: List[str] = list(filter(lambda name: 'а' in name.lower(), names_lst))

# Это же в цикле
filtered_names_a3: List[str] = []

for name in names_lst:
    if filter_a(name):
        filtered_names_a3.append(name)

from marvel import full_dict, small_dict

# Фильтруем marvel small_dict на фильмы вышедшие в input году

# user_input_year = input('Введите год выхода фильма:')

# filtered_small_dict_by_year: Dict[str, int] = dict(filter(lambda movie: movie[1] == int(user_input_year), small_dict.items()))
# print(filtered_small_dict_by_year)

# Поисковик фильмов определенной стадии вселенной marvel
# Альтернативное решение домашнего задания

marver_stage_dict: Dict[int, str] = {
    1: 'Первая фаза',
    2: 'Вторая фаза',
    3: 'Третья фаза',
    4: 'Четвертая фаза',
    5: 'Пятая фаза',
    6: 'Шестая фаза',
}

# user_input_stage: int = int(input('Введите номер фазы: '))
# str_stage: str = marver_stage_dict[user_input_stage]

# Ищем через Filter и lambda функцию по full dict marver

# result_films_titles = dict(filter(lambda movie: movie[1]['stage'] == str_stage, full_dict.items()))
# print(result_films_titles)

# Это же через dict comprehension
# result_films_titles2 = {movie[0]: movie[1] for movie in full_dict.items() if movie[1]['stage'] == str_stage}

# Получаем список названий фильмов через фильтр словаря
# result_films_titles3 = list(map(lambda movie: movie[1]['title'], result_films_titles.items()))
# Это же через dict comprehension
# result_films_titles4 = [movie[1]['title'] for movie in result_films_titles.items()]

# pprint с выключенной сортировкой
# pprint(result_films_titles, sort_dicts=False)

# Sorted - сортирует итерируемый объект
# sorted(iterable, key=None, reverse=False)
# Key - функция, которая применяется к каждому элементу перед сортировкой. Эта функция должна возвращать значение,
# по которому будет происходить сортировка

names_lst: List[str] = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша',
                        'Даша', 'Вика', 'Нина', 'Аня', 'Витя', 'Валера',
                        'Сергей', 'Николай', 'Станислав']

# Просто сортируем список имен
sorted_names1: List[str] = sorted(names_lst)
# print(sorted_names1)

# Применяем реверс
sorted_names2: List[str] = sorted(names_lst, reverse=True)
# print(sorted_names2)

# Key - соритровка по последней букве
sorted_names3: List[str] = sorted(names_lst, key=lambda name: name[-1])
# print(sorted_names3)

# Это же + reverse
sorted_names4: List[str] = sorted(names_lst, key=lambda name: name[-1], reverse=True)
# print(sorted_names4)

# Сортировка по длине строки
sorted_names5: List[str] = sorted(names_lst, key=len)
# print(sorted_names5)

# Сортировка small_dict marvel по алфавиту (ключ словаря)
sorted_small_dict: Dict[str, Optional[int]] = dict(sorted(small_dict.items(), reverse=True))
# pprint(sorted_small_dict, sort_dicts=False)

# Key может отдавать не одно значение, а несколько
# Сортировка по длине строки и по алфавиту
sorted_names6: List[str] = sorted(names_lst, key=lambda name: (len(name), name))


# print(sorted_names6)

# Сортировка marvel full_dict по stage и по title

def key_sort_stage_title(items: Dict[int, Dict[str, Union[str, int]]]) -> tuple[str, str]:
    """
    Функция для сортировки словаря по stage и title
    :param items: Словарь
    :return: Кортеж из двух строк
    """
    title = items[1]['title']
    year = items[1]['year'] if items[1]['year'] != 'TBA' else 3000
    stage = items[1]['stage']
    return year, title




# Делаем сортировку используя как ключ функцию key_sort_stage_title

sorted_full_dict = dict(sorted(full_dict.items(), key=key_sort_stage_title))
pprint(sorted_full_dict, sort_dicts=False)


# Проверка sorted на списке.
# Сортировка происходит лексикографически
# Сначала сверяется первая буква в слове, потом вторая и т.д.

some_letters_list = ['а', 'аб', 'ав', 'аг', 'аббв', 'аббвг', 'аббвгд', 'аббвгде', 'аббвгдее', 'аббвгдееё', 'аббвгдееёж',
                     'аббвгдееёжз', 'аббвгдееёжзи', 'аббвгдееёжзий']

print(sorted(some_letters_list))