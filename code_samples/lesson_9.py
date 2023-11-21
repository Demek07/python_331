# Lesson 9
# 12.10.2023

"""
1. Повторение материала
2. key, values, items
3. Распаковка кортежа по переменным
4. Распаковка значений в цикле for из items()
5. Кортежи
6. List Comprehension
7. Set Comprehension
8. Dict Comprehension
9. Список словарей
10. Тернарный оператор в словарях и comprehension
11. Знакомство с Tabulate


3. Списки словарей
"""
from pprint import pprint
from marvel import full_dict, small_dict

# Словари keys() values() items()

# person_dict = {
#     'name': 'John',
#     'age': 30,
#     'phone': '+380501234567',
# }
# print(len(person_dict))
# print(list(person_dict.keys()))
# print(list(person_dict.values()))
# print(list(person_dict.items()))

# Циклы и словари

# for key in person_dict:
#     print(key)
#
# for key in person_dict.keys():
#     print(key)
#
# for value in person_dict.values():
#     print(value)

# В переменную попадет кортеж из двух элементов - ключ и значение
# for item in person_dict.items():
#     print(type(item))
#     print(item)

# Как происходит распаковка элементов по 2 переменным в цикле?
# Распаковка дней недели по переменным

# sun, mon, tue, wed, thu, fri, sat = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# print(sun, mon, tue, wed, thu, fri, sat, sep='\n')

# Точно так же происходит распаковка в цикле, когда мы итерируемся по items() словаря
# for key, value in person_dict.items():
#     print(key, value, sep=': ')

# Кортежи (tuple)
# Кортеж является упорядоченной неизменяемой коллекцией элементов
# Кортежи могут содержать элементы разных типов
# У кортежей есть индексы, начинающиеся с 0

# Методы кортежей
# tuple() - создание кортежа
# count() - возвращает количество элементов с указанным значением
# index() - возвращает индекс первого элемента с указанным значением
# Удаление кортежа del tuple_name
# Сортировка кортежа sorted(tuple_name) - функция возвращает отсортированный список
# Срезы кортежей tuple_name[start:stop:step]

# some_int = 1,3
# print(type(some_int))
# print(some_int)

# List Comprehension
# Соберем title из Full_dict Марвел
# films_title = []

# for value in full_dict.values():
#     title = value['title']
#     films_title.append(title)

# pprint(films_title)
# 1. Чем мы формируем список?
# 2. Как мы формируем список?
# films_title_2 = [value['title'] for value in full_dict.values()]
# pprint(films_title_2)
# print(len(films_title_2))

# Set Comprehension

# films_title_set = {value['title'] for value in full_dict.values()}
# print(len(films_title_set))

# Все фильмы название которых начинается на Ж
# films_title = []
# for value in full_dict.values():
#     title = value['title']
#     if title.lower() == 'ж':
#         films_title.append(title)

# films_title_set_2 = {value['title'] for value in full_dict.values() if value['title'].lower()[0] == 'ч'}
# pprint(films_title_set_2)
# Todo
"""
Напишите set comprehension, который соберет названия фильмов вышедших в 2013 году

* Сложная версия:
- Напишите set comprehension, который соберет названия фильмов вышедших ДО 2013 года
"""

# films_set = set()
#
# for value in full_dict.values():
#     if value['year'] == 2013:
#         films_set.add(value['title'])
#
# films_title_set_3 = {value['title'] for value in full_dict.values() if value['year'] == 2013}
#
# pprint(films_set)
# pprint(films_title_set_3)

# Фильмы ДО 2013 года
# films_title_set_4 = {value['title'] for value in full_dict.values()
#                      if type(value['year']) == int and value['year'] < 2013}

# Это же но с isinstanse
# films_title_set_5 = {value['title'] for value in full_dict.values()
#                      if isinstance(value['year'], int) and value['year'] < 2013}

# isinstanse - проверяет принадлежность объекта к определенному типу данных
# первый аргумент - объект, второй - тип данных

# pprint(films_title_set_5)

# Dict Comprehension
# Такой же словарь но с фильмами где "stage" == "Первая фаза"

# films_dict = {}
#
# for key, value in full_dict.items():
#     if value['stage'] == 'Первая фаза':
#         films_dict[key] = value
#
# pprint(films_dict)
#
# films_dict_2 = {key: value for key, value in full_dict.items() if value['stage'] == 'Первая фаза'}
#
# films_dict_3 = {key: {
#     'title': value['title'],
#     'year': value['year'],
# } for key, value in full_dict.items() if value['stage'] == 'Первая фаза'}

# Список словарей объявлений. Ключи: заголовок, цена, автор, город, телефон
#
# ads_list = [
#     {
#         'title': 'Велосипед',
#         'price': 1000,
#         'author': 'Анна',
#         'city': 'Ростов',
#         'phone': '+7 999 888 77 66'
#     },
#     {
#         'title': 'Книга',
#         'price': 300,
#         'author': 'Андрей',
#         'city': 'Москва',
#         'phone': '+7 999 888 22 66'
#     },
#     {
#         'title': 'Ноутбук',
#         'price': 50000,
#         'author': 'Елена',
#         'city': 'Санкт-Петербург',
#         'phone': '+7 239 888 77 11'
#     },
#     ]

# Ищем объявления от 1000 и выше

# result = []
# for ad in ads_list:
#     if ad['price'] >= 1000:
#         result.append(ad)
#
# pprint(result)

# TODO Практика
"""
Попробуйте преобразовать small_dict из словаря в список словарей
НЕ включив фильмы где год выпуска None

Простой вариант: цикл
Сложный вариант list comprehension
"""

# pprint(small_dict, sort_dicts=False)  # sort_dicts - сортировка словарей внутри списка

# Первый вариант (через цикл)
result_lst = []

for key, value in small_dict.items():
        result_lst.append({
            key: value if value else 'TBA'
        })

pprint(result_lst)

# Второй вариант (через list comprehension)
# result_lst_2 = [{key: value} for key, value in small_dict.items() if value and value > 2023]
# pprint(result_lst_2)

# Tabulate
# pip install tabulate

# from tabulate import tabulate
from tabulate import tabulate

# Список словарей из full_dict состоящий из values
result_lst = [value for value in full_dict.values()]

print(tabulate(result_lst, headers='keys', tablefmt='grid'))
# Вывод в HTML
print(tabulate(result_lst, headers='keys', tablefmt='html'))