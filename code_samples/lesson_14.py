"""
Lesson 14
24.10.2023
Python331

1. Разбор ДЗ Игра "Города" HW_9 (Базовый вариант) и HW_10 (JSON)
2. Match case
3. Практика
4. Знакомство с функциями
"""
"""
1. Скачайте **приложенный** к ДЗ датасет, в котором есть список словарей всех городов РФ.
2. Поместите его к себе в проект (скопируйте файл, чтобы он был в папке проекта PyCharm)
3. Сделайте рабочий файл `main.py` в котором будет код игры
4. Сделайте импорт переменной `cities_list` из файла cities в начале рабочего документа `main.py`
5. Объявите пустой сет.
6. Наполните его названиями городов перебор списка словарей импортированного в п.4 `cities` любым из пройденных способов
"""

# from cities import cities_list
#
# cities_set = set()
#
# for city in cities_list:
#     if city['name'][-1].lower() not in 'ьъы':
#         cities_set.add(city['name'])

# Пишем сет в json файл

import json

#
# with open('cities.json', 'w', encoding='utf-8') as file:
#     json.dump(list(cities_set), file, ensure_ascii=False, indent=4)

# Читаем из json файла
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
# # Как можно реализовать статистику по последним 5 играм?
# # Мы делаем список для результатов
#
# result = []
#
# # Добавляем в список результаты
# result.append('Вы проиграли')
# result.append('Вы выиграли')
#
# # Мы можем добавлять результаты не в конец а в начало
# result.insert(0, 'Вы выиграли')
# result.insert(0, 'Вы проиграли')
#
# # Чтобы контролировать длину списка, мы можем удалять элементы из конца\


# Match case
# Появился в Python 3.10

# cmd = 'left'  # left
#
# match cmd:  # должен быть хотя бы один case
#     case 'top' | 'right':
#         print('вверх или право')
#     case 'left':
#         print('влево')
#     case 'top':
#         print('вверх опять')
#     case _:  # wildcard отрабатывает если другие блоки не сработали - опционально (любое ДРУГОЕ значение)
#         print('неизвестная команда')
#
# print('Проверки завершены')
#
# # Это же на блоках if - else
#
# # if cmd in ('top', 'right'):
# #     print('вверх или право')
# # elif cmd == 'left':
# #     print('влево')
# # elif cmd == 'top':
# #     print('вверх опять')
# # else:
# #     print('неизвестная команда')
#
# match cmd:
#     case command:  # command - переменная в которую попадает значение cmd
#         print(f'Вы ввели команду {command}')
#
#         # case вызовет ошибку так как не может быть двух одинаковых команд
#     # похоже на if else (последний не может быть первым)
# ####
#
# match cmd:
#     case str():  # проверка на тип данных (в данном случае класс строка)
#         print('Вы ввели строку')
#     case _:  # wildcard
#         print('Вы ввели что-то другое')
#
# match cmd:
#     case str() as command:  # as - присваивание переменной command только после проверки типа данных
#         print(f'Вы ввели команду {command}')
#     case _:  # wildcard
#         print('Вы ввели что-то другое')
#
# match cmd:
#     case str(command):  # запись идентичная предыдущей
#         print(f'Вы ввели команду {command}')
#     case _:  # wildcard
#         print('Вы ввели что-то другое')
#
# cmd = 1  # 10 #cmd
# match cmd:
#     # guard - дополнительная проверка можно прописывать условия внутри case по правилам if
#     case int() as command if 0 < command < 10:  # сначала проверка на тип данных, потом на диапазон
#         print(f'Вы ввели число от 0 до 9 {command}')
#         # проверка на длину и на то что строка состоит только из букв
#     case str() | float() as command if len(command) < 10 and command.isalpha() and command[0] == 'c':
#         print(f'Вы ввели строку command {command}')
#     case _:  # wildcard
#         print('Вы ввели что-то другое')
#
#         # Почему не if elif else? - match case более читаемый и понятный
#
# cmd = ['Monty Python', 'Python', '2023']
#
# match cmd:
#     case list() as book:
#         print(f'{book} - это список!')
#     case _:  # wildcard
#         print('Вы ввели что-то другое')
#
# match cmd:
#     # распаковка списка (только если 3 элемента длины) можно добавить *_ - для остальных. Можно добавить защитника и скобки на условия
#     case author, title, year, *_ if len(cmd) < 6:
#         print(f'Автор: {author}, название: {title}, год: {year}')
#
# ####  Работает и для кортежей
# match cmd:
#     case [str() as author, str() as title, int() | float() as year, *_] if len(cmd) < 6 and len(title) > 2:
#         print(f'Автор: {author}, название: {title}, год: {year}')
#
# ########
#
# ####  Работа со словарями
# cmd = {'author': 'Monty Python', 'title': 'Python', 'year': 2023, 'pages': 238}
#
# match cmd:
#     # Важно чтобы эти ключи словаря были, иначе будет wildcard
#     case {'author': str(author), 'title': str() as title, 'year': int(year) | float(year), 'pages': 238 | 239} if len(
#             cmd) > 2:
#         print(f'Автор: {author}, название: {title}, год: {year}')
#     case _:
#         print('Неверные данные')
#
#     ####  Проверка на количество ключей
#
# match cmd:
#     case {'author': str() as author, 'title': str() as title, **kwargs} if len(
#             kwargs) >= 2:  # **kwargs - остальные ключи
#         print(f'Автор: {author}, название: {title}, год: {kwargs.get("year")}')
#     case _:
#         print('Неверные данные!!!')
#
#     # Проверка на содержимое ключей
# key = 'author'
# match cmd:
#     case {'author': 'Monty Python', 'title': str() as title, **kwargs} if len(kwargs) >= 2:
#         print(f'Автор: {author}, название: {title}, год: {kwargs.get("year")}')

# key = 'author'
# # Паттерн не может быть переменной :(
# match cmd:
#     case {key: 'Monty Python', 'title': str() as title, **kwargs} if len(kwargs) >= 2:
#         print(f'Автор: {author}, название: {title}, год: {kwargs.get("year")}')


# TODO Практика
"""
Пробежать циклом по full_dict Marvel и проверить ключ 'year' на тип данных int через match case
Если тип данных не int - вывести на печать название фильма
"""


# from marvel import full_dict
#
# result = []
# for value in full_dict.values():
#     match value['year']:
#         case int():
#             pass
#         case _:
#             result.append(value['title'])
#
# print(result)

# Пишем это на if else

# result = []
# for value in full_dict.values():
#     # if type(value['year']) != int:
#     if not isinstance(value['year'], int):
#         result.append(value['title'])


# Знакомство с функциями

def summa(a, b):
    print(a + b)


# summa()  # TypeError: summa() missing 2 required positional arguments: 'a' and 'b'
summa(1, 2)  # 3

c = summa(1, 2)  # 3
print(c)  # None


def summa2(a, b):
    return a + b


d = summa2(1, 2)
print(d)  # 3
print(summa2(1, 2))  # 3

# TODO Практика
"""
Напишите функции:
1. Которая принимает 2 строки и возвращает их конкатенацию
2. Которая принимает 3 строки и возвращает их конкатенацию
"""


# Функция со всеми типами параметров
# def func(a, b, c=1, *args, **kwargs):
# pass


def say_hello_age(name, age):
    print(f'Привет, {name}! Тебе {age} лет')


# Позиционные аргументы
say_hello_age('John', 30)
say_hello_age(30, 'John')

# Именованные аргументы
say_hello_age(age=30, name='John')


# Значение по умолчанию
def say_hello_age2(name, age, msg='Привет'):
    print(f'{msg}, {name}! Тебе {age} лет')


say_hello_age2('John', 30)
say_hello_age2('John', 30, 'Пока')
# Порядок передачи аргументов. Сначала позиционные, потом именованные

say_hello_age2('John', msg='Пока', age=30)

# Распаковка аргументов
shop_lst = ['bread', 'milk', 'butter']
item1, item2, item3 = shop_lst
print(item1, item2, item3)
print(shop_lst[0], shop_lst[1], shop_lst[2])
print(*shop_lst)  # распаковка списка


def get_args(*args):
    print(args)
    print(type(args))


get_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

"""
Практика
Переделать функцию сложения строк на *args
"""

result = []
result = ''

def get_conc_strings(*strings):
    reuslt = ''
    for string in strings:
        reuslt += string
    return reuslt


def get_conc_strings2(*strings):
    return ''.join(strings)


print(get_conc_strings2('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'))


def main():
    string = ''
    get_conc_strings2(string)


main()
