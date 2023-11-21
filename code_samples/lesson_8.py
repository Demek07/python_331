# import marvel # Не удобно обращаться к модулю
from pprint import pprint

import marvel
from marvel import * # Не рекомендуется
from marvel import full_dict #



# Lesson 8. 10.10.2023
"""
1. Разбор домашних заданий
- Генератор пословиц
- Try - Except
- Валидатор номера телефона

2. Повторение материала
- Строки и методы строк
- Списки и методы списков
- Сеты и методы сетов

3. Словари
- Методы словарей
- Запись в словарь
- Цикл for в словарях
- Практика
- Импорт модулей
- Pprint
"""
import time

# Генератор пословиц.
# Как нам запросить определенное количество пословиц?
# provebs_list = ['Век живи - век учись', 'Без труда не выловишь и рыбку из пруда']
# len_set = 20
# input_value = input('Сколько пословиц вывести? ')
# if input_value.isdigit():
#     proverbs_count = int(input_value)
#     if proverbs_count > len_set:
#         print(f'Ваш запрос {proverbs_count} превышает количество пословиц в базе {len_set}.\n'
#               f'Будет выведено {len_set} пословиц')
#         proverbs_count = len_set
#
# else:
#     raise ValueError('Вы ввели не число')
#
#
# # Мы получили количество пословиц
# # Нам нужно сделать X итераций для создания новых пословиц
#
# # for i in range(proverbs_count):
# provebs_set = set(provebs_list)
#
# provebs_result = []
#
# while len(provebs_result) != proverbs_count or not provebs_set:
#     # Генерация пословиц
#     # 1. Выбрать случайную пословицу из сет
#     random_proveb = provebs_set.pop()
#     print(type(random_proveb))
#     random_proveb.replace('Ум', '')

# Методы списков
# append() - добавляет элемент в конец списка
# extend() - расширяет список другим списком
# count() - возвращает количество элементов, которые равны указанному
# sort() - сортирует список на основе функции сравнения
# insert() - добавляет элемент в список по указанному индексу
# remove() - удаляет первый элемент из списка, который равен указанному
# pop() - удаляет элемент из списка по указанному индексу и возвращает его
# clear() - очищает список
# index() - возвращает индекс первого элемента, который равен указанному
# reverse() - разворачивает список

# while
# while - else
# try - except - else - finally
# raise
# exception
# set
# set methods
# set operations

# Популярные исключения
# ValueError - ошибка типа данных
# ZeroDivisionError - ошибка деления на ноль
# NameError - ошибка имени
# TypeError - ошибка типа данных
# IndexError - ошибка индекса
# KeyError - ошибка ключа
# AttributeError - ошибка атрибута
# FileNotFoundError - ошибка файла не найден
# ModuleNotFoundError - ошибка модуля не найден
# ImportError - ошибка импорта
# KeyboardInterrupt - ошибка прерывания пользователем

# Методы множества
# add - добавление элемента в множество
# remove - удаление элемента из множества, если элемента нет - генерирует исключение KeyError
# discard - удаление элемента из множества, если элемента нет - ничего не делает
# pop - возвращает и удаляет случайный элемент из множества
# clear - очищает множество
# copy - копирует множество
# union - объединение множеств (|) - возвращает новое множество
# intersection - пересечение множеств (&) - возвращает новое множество
# difference - разность множеств (-) - возвращает новое множество
# symmetric_difference - симметричная разность множеств (^) - возвращает новое множество
# issubset - является ли множество подмножеством другого множества (<=)
# issuperset - является ли множество надмножеством другого множества (>=)
# isdisjoint - являются ли множества непересекающимися (если нет общих элементов - True, иначе - False)

# product_set = set()  # {} - пустой словарь
#
# while True:
#     product = input('Введите название продукта: ').lower()
#     if not product: # Строка без символов - False
#         break
#     product_set.add(product)
#
# print(product_set)
#
# while product_set:
#     print(f'Было {product_set}')
#     print(product_set.pop())
#     print(f'Стало {product_set}')
#     print('-' * 50)
#     time.sleep(2)
#
# while True:
#     # Идем по магазину и покупаем продукты
#     product = input('Введите название покупаемого продукта: ').lower()
#     try:
#         product_set.remove(product)
#     except KeyError:
#         print(f'Продукта {product} нет в списке!!!\n'
#               f'Остались продукты: {product_set}')


# gadget_set = {'phone', 'laptop', 'tablet', 'pc'}
#
# for gadget in gadget_set:
#     print(gadget)
#     gadget_set.remove(gadget)
#
# print(gadget_set)

# Словари.
# Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу.
# (Упорядочены с версии - 3.7)
# Ключи словаря - неизменяемые объекты (int, float, str, bool, tuple)
# Ключи - уникальные, не могут повторяться

# empty_dict = {}
# empty_dict = dict()

# Словарь с элементами
# dict_1 = {'key_1': 'value_1', 'key_2': 'value_2'}


# Методы словарей
# update() - обновляет словарь, добавляя пары (ключ, значение) из другого словаря
# keys() - возвращает ключи в словаре
# values() - возвращает значения в словаре
# items() - возвращает пары (ключ, значение)
# get() - возвращает значение ключа, если его нет - мы можем установить значение по умолчанию
# pop() - удаляет ключ и возвращает значение
# popitem() - удаляет и возвращает пару (ключ, значение)
# copy() - возвращает копию словаря
# clear() - очищает словарь
# setdefault() - возвращает значение ключа, если его нет - добавляет ключ со значением
# Удаление ключа из словаря - del dict['key']

# person_dict = {'name': 'John', 'age': 30, 'phone': '+380501234567', 'email': 'john@mail.ru',
#                'languages': ['Python', 'Go', 'JS'], 'is_student': True}

# print(person_dict)
# print(person_dict['name'])
# print(type(person_dict['name']))

# print(person_dict.keys())
# print(list(person_dict.keys()))
#
# print(person_dict.values())
# print(list(person_dict.values()))
#
# print(person_dict.items())
# print(list(person_dict.items()))

# print(person_dict)
#
# person_dict.update(
#     {
#         'is_married': False,
#         'is_student': False
#     }
# )

# friends = person_dict['friends'] # KeyError (ключа нет в словаре)
# friends = person_dict.get('friends', 0)  # None (ключа нет в словаре)
# if friends:
#     print(friends)
# else:
#     print("У него нет друзей :(")
#
# print(friends)

# Цикл for в словарях
# person_dict = {
#     'name': 'John',
#     'age': 30,
#     'phone': '+380501234567',
#     'email': 'john@gmail.com',
#     'languages': ['Python', 'Go', 'JS']
# }
# print(f'{len(person_dict)=}')
# for key in person_dict:
#     print(key)
#
# for key in person_dict.keys():
#     print(f"{key=}")
#
# for key in person_dict.values():
#     print(f"{key=}")
#
# for key, value in person_dict.items():
#     print(f"{key=}, {value=}")

# TODO - практика
"""
Работаем со словарем person_dict.
1. Пользовательский ввод - запросить у пользователя язык программирования
2. Проверить, знает ли пользователь этот язык (словарь ключ languages)
3. Если знает - вывести сообщение: "Пользователь знает этот язык"
4. Если не знает - вывести сообщение: "Пользователь не знает этот язык"
5. Сложная версия: регистронезависимая проверка
"""

person_dict = {
    'name': 'John',
    'age': 30,
    'phone': '+380501234567',
    'email': 'john@gmail.com',
    'languages': ['Python', 'Go', 'JS']
}

# input_language = input('Введите язык программирования: ')
#
# user_languages = person_dict['languages']
#
# if input_language in user_languages:
#     print('Пользователь знает этот язык')
#
# user_languages_lower = []
#
# for language in user_languages:
#     user_languages_lower.append(language.lower())
#
# if input_language.lower() in user_languages_lower:
#     print(f'Пользователь знает {input_language}')
#
#
# if input_language.lower() in [language.lower() for language in person_dict['languages']]:
#     print('Пользователь знает этот язык')
#

# print(full_dict)
pprint(full_dict)