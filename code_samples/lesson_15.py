"""
Lesson 15
26.10.2023
Python331

1. Повторение материала
2. Функции
- Объявление функции
- Параметры функции
- Возвращаемое значение
- Ссылка на функцию и вызов функции
- Позиционные и именованные параметры
Отладочная строка
- Передача параметров по умолчанию
- Передача произвольного количества параметров
- Распаковка параметров
- Распаковка словарей
- Распаковка списков
- Функция со всеми типами аргументов
- Распаковка аргумнтов в функцию (пример с print)
- Области видимости (Встроенная, глобальная, локальная, нелокальная)
3. Написали модуль с функциями для проверки пароля
"""
from marvel import small_dict


# def - definition (определение)

def my_func():
    print('Hello, world!')


# Вызов функции
# my_func()

# Ссылка на функцию
# new_func = my_func
# print(new_func)
# Вызов функции через ссылку
# new_func()


# Параметры функции
def my_func_2(name):
    print(f'Hello, {name}!')


# return - возвращает значение из функции
# После return код не выполняется
def my_func_3(name):
    if name.startswith('А'):
        return (f'Привет, {name}!\n'
                f'Похоже твое имя начинается на букву А!')
    else:
        return f'Привет, {name}!'

    print('Этот код не выполнится')


# my_func_3('Андрей')
# my_func_3('Иван')

# Позиционные параметры
def my_func_4(group, name):
    return {
        'group': group,
        'name': name
    }


result1 = my_func_4('Python331', 'Сергей Орлов')
result2 = my_func_4('Сергей Орлов', 'Python331')

# print(f'{result1=}')
# print(f'{result2=}')

# Именованные параметры
result3 = my_func_4(name='Сергей Орлов', group='Python331')


# print(f'{result3=}')  # Отладочная строка {переменная=}


# Передача параметров по умолчанию
def my_func_5(name, group='Python331'):
    return {
        'group': group,
        'name': name
    }


# Количество передаваемых аргументов должно быть равно количеству параметров
# TypeError: my_func_5() takes from 1 to 2 positional arguments but 3 were given
# result4 = my_func_5('Сергей Орлов', 'Python331', 'Python331') # Ошибка

result4 = my_func_5('Сергей Орлов')
# print(f'{result4=}')

result5 = my_func_5('Николай Андреев', 'Python332')
# print(f'{result5=}')

# Передача произвольного количества параметров
products = ['Колбаса', 'Сыр', 'Молоко']
product1, product2, product3 = products

# print(f'{product1=}', f'{product2=}', f'{product3=}')

products = ['Колбаса', 'Сыр', 'Молоко', 'Хлеб', 'Масло']

product1, product2, product3, *other_products = products


# print(f'{product1=}', f'{product2=}', f'{product3=}', f'{other_products=}')

# print(products)
# print(*products)

# print(products[0], products[1], products[2], products[3], products[4])
# print('Раз', 'Два', 'Три', 'Четыре', 'Пять')


def my_func_6(*args):
    print(f'{args=}')
    print(type(args))
    print(len(args))
    for arg in args:
        print(arg)


# my_func_6(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# my_func_6(*products)


# Функция со всеми типами аргументов
# def func(a, b, c=1, *args, **kwargs):
# - Позиционные параметры
# - Именованные параметры
# - Параметры по умолчанию
# - Произвольное количество параметров
# - Произвольное количество именованных параметров

# **kwargs - keyword arguments
def my_func_7(**kwargs):
    print(f'{kwargs=}')
    print(type(kwargs))
    print(len(kwargs))
    for key, value in kwargs.items():
        print(f'{key=}, {value=}')


# my_func_7(name='John', age=30, phone='+77051324555', address='Kazakhstan', is_married=False)
# my_func_7(**{'name': 'John', 'age': 30, 'phone': '+77051324555'})

print_dict = {
    'sep': ' |sep| ',
    'end': ' |end| ',
}
# Мы можем передать в print распакованный словарь с теми аргументами
# которые принимает функция print
# print('Hello', 'world', '!', **print_dict)
# Но вот это уже не будет работать. Потому что print не принимает ТАКИЕ аргументы
# print(**{'name': 'John', 'age': 30, 'phone': '+77051324555'})

# Области видимости
# Встроенная область видимости - встроенные функции и переменные
# Глобальная область видимости - переменные объявленные вне функций
# Локальная область видимости - переменные объявленные внутри функций
# Нелокальная область видимости - переменные объявленные внутри функций

# Интерпретатор ищет переменные в следующем порядке:
# Локальная область видимости
# Нелокальная область видимости
# Глобальная область видимости
# Встроенная область видимости


# Глобальная а
a = 2


def change_a():
    # Локальная а
    # global a # Global - глобальная область видимости
    a = 3
    print(a)


# print(a)
# change_a()
# print(a)


# Нелокальная область видимости
# a = 1
# def outer():
#     a = 2
#
#     def inner():
#         nonlocal a
#         a = 3
#         print(a)
#
#     print(a)
#     inner()
#     print(a)
#
#
# outer()

# def my_func_8():
#     a = 1
#
#     def inner():
#        nonlocal a
#        a = 2
#        print(f'inner: {a=}')
#
#     print(f'my_func_8: {a=}')
#     inner()
#     print(f'my_func_8: {a=}')
#
# my_func_8()

# Todo Практика 1
"""
Будем работать с marvel small_dict
Напишите функцию, которая принимает на вход год выхода фильма, 
и **kwargs в виде датасета **small_dict

Функция возвращает сет названий фильмов, вышедших в этот год
"""


def get_film_by_year(year, **kwargs):
    """
    Принимает год и **kwargs в виде датасета **small_dict
    Возвращает сет названий фильмов, вышедших в этот год
    :param year: Год выхода фильма
    :param kwargs: Датасет фильмов
    :return: Сет названий фильмов
    """
    result = set()
    for title, year_ in kwargs.items():
        if year_ == year:
            result.add(title)

    if result:
        return result
    else:
        return None


# user_year = int(input('Введите год: '))
#
# result = get_film_by_year(user_year, **small_dict)
#
# if result:
#     print(f'Фильмы вышедшие в {user_year}:\n{result}')
# else:
#     print(f'Фильмы вышедшие в {user_year} не найдены')


# Пишем скрипт проверки пароля и делаем его серией функций

"""
Проверка пароля
- Пароль должен быть не менее 8 символов
- Пароль должен содержать цифры
- Пароль должен содержать буквы
- Пароль должен содержать буквы разных регистров
- Пароль должен содержать спец символы
- Пароль не должен содержать пробелы

"""
#
LEN_THRESHOLD = 8
DIGIT_THRESHOLD = 1
LETTER_THRESHOLD = 2
UPPER_THRESHOLD = 1
LOWER_THRESHOLD = 1
SPECIAL_THRESHOLD = 1
SPECIAL = '!@#$%^&*()_+=-'
#
# result = ''
# input_password = input('Введите пароль: ')
#
# # Проверка длины пароля
# if len(input_password) < LEN_THRESHOLD:
#     result += f'Пароль должен быть не менее {LEN_THRESHOLD} символов\n'
#
# # Проверка наличия цифр
# digit_counter = 0
# for symbol in input_password:
#     if symbol.isdigit():
#         digit_counter += 1
#
# if digit_counter < DIGIT_THRESHOLD:
#     result += f'Пароль должен содержать не менее {DIGIT_THRESHOLD} цифр\n'
#
# # Проверка наличия букв
# letter_counter = 0
# for symbol in input_password:
#     if symbol.isalpha():
#         letter_counter += 1
#
# if letter_counter < LETTER_THRESHOLD:
#     result += f'Пароль должен содержать не менее {LETTER_THRESHOLD} букв\n'
#
# # Проверка наличия букв разных регистров
# upper_counter = 0
# lower_counter = 0
#
# for symbol in input_password:
#     if symbol.isupper():
#         upper_counter += 1
#     elif symbol.islower():
#         lower_counter += 1
#
# if upper_counter < UPPER_THRESHOLD:
#     result += f'Пароль должен содержать не менее {UPPER_THRESHOLD} букв в верхнем регистре\n'
#
# if lower_counter < LOWER_THRESHOLD:
#     result += f'Пароль должен содержать не менее {LOWER_THRESHOLD} букв в нижнем регистре\n'
#
# # Проверка наличия спец символов
# special_counter = 0
# for symbol in input_password:
#     if symbol in SPECIAL:
#         special_counter += 1
#
# if special_counter < SPECIAL_THRESHOLD:
#     result += f'Пароль должен содержать не менее {SPECIAL_THRESHOLD} спец символов\n'
#
# # Проверка наличия пробелов
# if ' ' in input_password:
#     result += f'Пароль не должен содержать пробелы\n'
#
# if result:
#     print(result)
# else:
#     print('Пароль подходит')


# Пишем каждую проверку на отдельную функцию
# Делаем функцию check_password которая будет вызывать все функции проверки

def check_len_password(password, len_threshold):
    """
    Проверка длины пароля
    :param password: Пароль
    :param threshold: Порог длины
    :raise ValueError: Если длина пароля меньше порога
    :return: None - если все хорошо
    """
    if len(password) < len_threshold:
        raise ValueError(f'Пароль должен быть не менее {len_threshold} символов')
    else:
        return None


def check_digit_password(password, digit_threshold):
    """
    Проверка наличия цифр в пароле
    :param password: Пароль
    :param threshold: Порог количества цифр
    :raise ValueError: Если количество цифр меньше порога
    :return: None - если все хорошо
    """
    digit_counter = 0
    for symbol in password:
        if symbol.isdigit():
            digit_counter += 1

    if digit_counter < digit_threshold:
        raise ValueError(f'Пароль должен содержать не менее {digit_threshold} цифр')
    else:
        return None


def check_letter_password(password, letter_threshold):
    """
    Проверка наличия букв в пароле
    :param password: Пароль
    :param letter_threshold:
    :raise ValueError: Если количество букв меньше порога
    :return: None - если все хорошо
    """
    letter_counter = 0
    for symbol in password:
        if symbol.isalpha():
            letter_counter += 1

    if letter_counter < letter_threshold:
        raise ValueError(f'Пароль должен содержать не менее {letter_threshold} букв')
    else:
        return None


def check_upper_password(password, upper_threshold):
    """
    Проверка наличия букв в верхнем регистре в пароле
    :param password: Пароль
    :param upper_threshold: Порог количества букв в верхнем регистре
    :raise ValueError: Если количество букв в верхнем регистре меньше порога
    :return: None - если все хорошо
    """
    upper_counter = 0
    for symbol in password:
        if symbol.isupper():
            upper_counter += 1

    if upper_counter < upper_threshold:
        raise ValueError(f'Пароль должен содержать не менее {upper_threshold} букв в верхнем регистре')
    else:
        return None


def check_lower_password(password, lower_threshold):
    """
    Проверка наличия букв в нижнем регистре в пароле
    :param password: Пароль
    :param lower_threshold: Порог количества букв в нижнем регистре
    :raise ValueError: Если количество букв в нижнем регистре меньше порога
    :return: None - если все хорошо
    """
    lower_counter = 0
    for symbol in password:
        if symbol.islower():
            lower_counter += 1

    if lower_counter < lower_threshold:
        raise ValueError(f'Пароль должен содержать не менее {lower_threshold} букв в нижнем регистре')
    else:
        return None


def check_special_password(password, special_threshold, special):
    """
    Проверка наличия спец символов в пароле
    :param password: Пароль
    :param special_threshold: Порог количества спец символов
    :param special: Спец символы
    :raise ValueError: Если количество спец символов меньше порога
    :return: None - если все хорошо
    """
    special_counter = 0
    for symbol in password:
        if symbol in special:
            special_counter += 1

    if special_counter < special_threshold:
        raise ValueError(f'Пароль должен содержать не менее {special_threshold} спец символов')
    else:
        return None


def check_space_password(password):
    """
    Проверка наличия пробелов в пароле
    :param password: Пароль
    :raise ValueError: Если пароль содержит пробелы
    :return: None - если все хорошо
    """
    if ' ' in password:
        raise ValueError(f'Пароль не должен содержать пробелы')
    else:
        return None


def check_password(password):
    """
    Проверка пароля
    :param password: Пароль
    :return: None - если все хорошо
    """
    check_len_password(password, LEN_THRESHOLD)
    check_digit_password(password, DIGIT_THRESHOLD)
    check_letter_password(password, LETTER_THRESHOLD)
    check_upper_password(password, UPPER_THRESHOLD)
    check_lower_password(password, LOWER_THRESHOLD)
    check_special_password(password, SPECIAL_THRESHOLD, SPECIAL)
    check_space_password(password)
    return None


def main():
    input_password = input('Введите пароль: ')
    try:
        check_password(input_password)
    except ValueError as error:
        print(error)
    else:
        print('Пароль подходит')


main()
