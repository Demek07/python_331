"""
Lesson 17
02.11.2023
Python331

1. Тотальный разбор. Игра "Города" - рефакторинг + аннотация типов
2. Повторение материала (списковые включения, словарные включения, включения множеств)

"""
import json
from typing import Dict

from cities import cities_list

# cities_set = set()
#
# for city in cities_list:
#     cities_set.add(city['name'])
#
russian_letters_set = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')


#
# bad_letters = {'ь', 'ё', 'ъ', 'ы'}

# Добыли плохие буквы
# Идем по сету букв русского языка и проверяем на какую букву нет города
# for letter in russian_letters_set:
#     if not any(city.startswith(letter.upper()) for city in cities_set):
#         bad_letters.add(letter)
#


#
# import json
#
#
# with open('cities.json', 'w', encoding='utf-8') as file:
#     json.dump(list(cities_set), file, ensure_ascii=False, indent=4)
#
# # Читаем из json файла
# with open('cities.json', 'r', encoding='utf-8') as file:
#     cities_set = set(json.load(file))
#
# """
# Игра
# 1. Объявите цикл `while`
# 2. Объявите пользовательский ввод
# 3. Сделайте проверку на стоп. Если пользователь ввёл стоп - он **проиграл** машине.
# 4. Сделайте проверку, что это название есть в сете городов (Если нет - вероятно вы проиграли машине)
# 5. Если есть. Удалите его из сета
# 6. Придумайте, как можно реализовать проверку условий выполнения игры (подходит ли ответ пользователя,
#  согласно тому городу, который озвучил компьютер?)
# 7. Пусть компьютер теперь сделает свой ход. Поищет город, который кончается на
#  последнюю букву того города, который назвали вы.
# 8. Если такой город есть - повторите цикл.
# 9. В конце игры, объявите победителя.
# """
# computer_city = None
#
# while cities_set:
#     # Пользовательский ввод
#     humans_city = input('Введите город: ').strip()
#
#     # Проверка на стоп
#     if humans_city == 'стоп':
#         print('Вы проиграли')
#         break
#
#     # Проверка на вхождение в сет
#     if humans_city not in cities_set:
#         print('Такого города нет')
#         break
#
#     # Если компьютер уже ходил. Делаем проверку на последнюю букву
#     if computer_city:
#         if computer_city[-1].lower() != humans_city[0].lower():
#             print('Вы проиграли')
#             break
#
#     # Удаление из сета
#     cities_set.remove(humans_city)
#
#     # Принт ход человека
#     print(f'Вы ввели: {humans_city}')
#
#     # Ход машины
#     for city in cities_set:
#         if city[0].lower() == humans_city[-1].lower():
#             computer_city = city
#
#     # Удаление из сета
#     cities_set.remove(computer_city)
#
#     # Принт ход машины
#     print(f'Машина ввела: {computer_city}')
#
#
# else:
#     print('Вы терминатор. Вы выиграли!')
#

# Делаем рефакторинг на функции с аннотацией типов!

def get_cities_set_from_json(file_name: str = 'cities.json') -> set:
    """
    Читает json файл и возвращает сет городов
    :param file_name: По умолчанию 'cities.json'
    :return: Сет городов
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        cities_set = set(json.load(file))

    return cities_set


def get_bad_startswith_letters(letters_set: set, cities_set: set) -> set:
    """
    Функция, которая возвращает сет плохих первых букв
    :param letters_set: Сет букв для поиска
    :param cities_set: Сет городов для анализа
    :return: Сет плохих букв, с которых не начинаются города в cities_set
    """
    bad_startswith_letters: set = set()

    for letter in letters_set:
        if not any(city.startswith(letter.upper()) for city in cities_set):
            bad_startswith_letters.add(letter)

    return bad_startswith_letters


def check_bad_startwith_letter(city: str, bad_letters: set) -> bool:
    """
    Функция принимает город и возвращает True, если он начинается на плохую букву
    :param city: Название города
    :param bad_letters: Сет плохих букв
    :return: bool
    """
    if city[0].lower() in bad_letters:
        return True
    else:
        return False


def check_main_game_rule(last_round_city: str, current_round_city: str) -> bool:
    """
    Функция принимает два города и проверяет, что первая буква города current_round_city
    равна последней букве города last_round_city
    :param last_round_city: Город из прошлого раунда
    :param current_round_city: Город из текущего раунда
    :return: bool
    """
    if last_round_city[-1].lower() == current_round_city[0].lower():
        return True
    else:
        return False


def computer_move(cities_set: set, last_round_city: str) -> str | None:
    """
    Функция принимает сет городов, город из прошлого раунда. Проходит циклом по сету
    городов, проверяя каждый город на главное правило игры
    :param cities_set:
    :param last_round_city:
    :return:
    """
    for city in cities_set:
        if check_main_game_rule(last_round_city, city):
            return city

    else:
        return None


def main():
    # Читаем json файл с городами и получаем сет городов
    cities_set = get_cities_set_from_json()

    # Получаем сет плохих букв
    bad_letters = get_bad_startswith_letters(russian_letters_set, cities_set)

    # Объявляем переменную под город машины (None на старте)
    computer_city = None

    while cities_set:
        # Пользовательский ввод
        humans_city = input('Введите город: ').strip()

        # Проверка на стоп
        if humans_city == 'стоп':
            print('Вы проиграли')
            # Логирование
            break

        # Проверка на вхождение в сет
        if humans_city not in cities_set:
            print('Такого города нет')
            # Логирование
            break

        # Если компьютер уже ходил. Делаем проверку на последнюю букву
        if computer_city:
            if not check_main_game_rule(computer_city, humans_city):
                print('Вы проиграли')
                # Логирование
                break

        # Удаление из сета
        cities_set.remove(humans_city)

        # Принт ход человека
        print(f'Вы ввели: {humans_city}')

        # Ход машины
        computer_city = computer_move(cities_set, humans_city)

        if not computer_city:
            print('Вы выиграли')
            # Логирование
            break

        # Удаление из сета
        cities_set.remove(computer_city)
        # Принт ход машины
        print(f'Машина ввела: {computer_city}')

    else:
        print('Вы терминатор. Вы выиграли!')
        # Логирование


# main()

from marvel import full_dict

# def print_full_dict(full_dict: Dict[int, Dict[int, str | int]]):
#     print(full_dict)
#
#
# print_full_dict(full_dict)

# Todo Практика!
"""
1. Списковые включения
- Собрать из full_dict Marvel title фильмов в список

2. Включения множеств
- Собрать из full_dict Marvel stage во множество

3. Словарные включения
- Собрать из full_dict Marvel title фильмов в словарь, где ключ - title фильма, а значение - это stage фильма


4. Словарные включения
- Собрать из full_dict Marvel title фильмов в словарь, где ключ - это id фильма, а значение - это title фильма
"""

# 1. Списковые включения
# - Собрать из full_dict Marvel title фильмов в список
# marvel_titles_list = [movie['title'] for movie in full_dict.values()]
# print(marvel_titles_list)

# 2. Включения множеств
# - Собрать из full_dict Marvel stage во множество
# marvel_stages_set = {movie['stage'] for movie in full_dict.values()}
# print(marvel_stages_set)

# 3. Словарные включения
# - Собрать из full_dict Marvel title фильмов в словарь, где ключ - title фильма,
# а значение - это stage фильма

# marvel_titles_dict = {movie['title']: movie['stage'] for movie in full_dict.values()}
# print(marvel_titles_dict)

# 4. Словарные включения
# - Собрать из full_dict Marvel title фильмов в словарь, где ключ - это id фильма,
# а значение - это title фильма

# print(full_dict.items())
# marvel_titles_dict = {movie[0]: movie[1]['title'] for movie in full_dict.items() if movie[0] < 5}
# print(marvel_titles_dict)

# Реализация №2 через dict comprehension (key, value)
# marvel_titles_dict2 = {key: value['title'] for key, value in full_dict.items() if key < 5}
# print(marvel_titles_dict2)


# Функция map() - применяет функцию к каждому элементу последовательности
# map(function, iterable, ...)

nums_str = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Реализация через цикл

nums_int = []

for num in nums_str:
    nums_int.append(int(num))

# Реализация через comprehension

nums_int2 = [int(num) for num in nums_str]

# Реализация через map
nums_int3 = list(map(int, nums_str))


# Пишем более сложную функцию для применения в цикле

def square(str_num: str) -> int:
    num = int(str_num)
    return num ** 2


# Реализация через цикл

nums_int4 = []

for num in nums_str:
    nums_int4.append(square(num))

# Реализация через comprehension
nums_int5 = [square(num) for num in nums_str]

# Реализация через map
nums_int6 = list(map(square, nums_str))
print(nums_int6)
print(type(nums_int6))

# Анонимные функции lambda
# lambda arguments: expression

# Реализация через map и lambda
nums_int7 = list(map(lambda num: int(num) ** 2, nums_str))

# Как дать имя анонимной функции?
# - Присвоить ее переменной

square_lambda = lambda num: int(num) ** 2

res = square_lambda('2')
print(res)
