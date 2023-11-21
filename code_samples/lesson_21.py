"""
Lesson 21
16.11.2023
Python331

1. Декораторы
2. Декорирование несколькими декораторами
3. Декораторы с параметрами


https://stackoverflow.com/questions/739654/how-do-i-make-function-decorators-and-chain-them-together/1594484#1594484
https://habr.com/ru/companies/otus/articles/727590/
https://djangofan.ru/python_20


"""
from typing import Callable, List


#
# def check_time_decorator(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         func(*args, **kwargs)
#         finish_time = time.perf_counter()
#         result_time = finish_time - start_time
#         print(f'Прошло {result_time:.10f} секунд')
#
#     return wrapper
#
#
# from cities import cities_list
#
#
# # Функция которая пробегает по списку городов и возвращает список городов в котором есть буква (которую принимает функция)
# # Работа в цикле
#
# @check_time_decorator
# def get_city_by_letter_in_for(letter: str) -> List[str]:
#     result_list: List[str] = []
#     for city in cities_list:
#         if letter in city:
#             result_list.append(city)
#     return result_list
#
#
# # Это же в списковом включении
# @check_time_decorator
# def get_city_by_letter_in_comprehension(letter: str) -> List[str]:
#     return [city for city in cities_list if letter in city]
#
#
# # Вызываем функцию 1
# # get_city_by_letter_in_for('а')
# # Вызываем функцию 2
# # get_city_by_letter_in_comprehension('а')
#
#
# # Декораторы с параметрами
# # Декораторы с параметрами - это функции, которые принимают параметры и возвращают декоратор.
#
# def print_decorator(func: Callable) -> Callable:
#     def wrapper() -> None:
#         print("Start")
#         func()
#         print("End")
#
#     return wrapper
#
#
# # Этот же декоратор, но чтобы он принимал 2 параметра, это префикс и постфикс
# # Первая функция передает параметры декоратора в обвертку
# def print_decorator2(prefix: str, postfix: str) -> Callable:
#     # Вторая функция передает обворачиваемую функцию в обвертку
#     def decorator(func: Callable) -> Callable:
#         # Третья функция - сама обвертка
#         def wrapper(name) -> None:
#             print(prefix)
#             func(name)
#             print(postfix)
#
#         return wrapper
#
#     return decorator
#
#
# def print_hello(name: str) -> None:
#     print(f'Hello {name}')
#
# print('start')
# f: Callable = print_decorator2("Start", "End")(print_hello)
# f("Олег")
#
# """
# f -> wrapper отрабатывает внутри декоратора print_decorator2("Start", "End")
# """
#
#
# # Используем синтаксис декораторов
#
# @print_decorator2("Ад", "Рай")
# def print_hello2(name: str) -> None:
#     print(f'Hello {name}')
#
#
# print_hello2('Прохор Шаляпин')
#
# #TODO Практика
# """
# Напишите 2 декоратора print_decorator и print_decorator2
# 1. print_decorator - просто печатает start_1 и end_1
# 2. print_decorator2 - просто печатает start_2 и end_2
# 3. Напишите функцию some_func, которая просто печатает "Вызов функции some_func"
# 4. Декорируйте функцию some_func
# - Одним декоратором print_decorator
# - Двумя декораторами print_decorator и print_decorator2 (один над другим)
# - Поменяйте местами декораторы print_decorator2 и print_decorator
# """


# def print_decorator2(func: Callable) -> Callable:
#     # func - some_func
#     def wrapper() -> None:
#         print("Start декоратора 2")
#         func()
#         # print("End декоратора 2")
#
#     return wrapper
#
#
# def print_decorator3(func: Callable) -> Callable:
#     # func - wrapper второго декоратора
#     def wrapper() -> None:
#         print("Start декоратора 3")
#         func()
# #         print("End декоратора 3")
#
#     return wrapper
#
#
# def some_func():
#     print("Вызов функции some_func")
#
# #
# # dec = print_decorator3(print_decorator2(some_func))
# # dec()
# """
# dec -> wrapper3 -> print_decorator3 -> wrapper2 -> print_decorator2 -> some_func
# """
#
# @print_decorator3
# @print_decorator2
# def some_func2():
#     print('Вызов функции some_func2')
#
#
# some_func2()


#####
# Добавляем полезную работу в декоратор и проверяем последовательность декорирования
# одной функции несколькими декораторами

def print_decorator3(func: Callable) -> Callable:
    # func - some_func
    def wrapper() -> None:
        print("Start print_decorator3")
        func()
        # print("End декоратора 2")

    return wrapper


def print_decorator4(func: Callable) -> Callable:
    # func - wrapper второго декоратора
    def wrapper() -> None:
        print("Start print_decorator4")
        func()

    #         print("End декоратора 3")

    return wrapper


def some_func2():
    print("Вызов функции some_func")


#
# dec = print_decorator3(print_decorator2(some_func))
# dec()
"""
dec -> wrapper3 -> print_decorator3 -> wrapper2 -> print_decorator2 -> some_func
"""


@print_decorator4
@print_decorator3
def some_func2():
    print('Вызов функции some_func2')


# some_func2()

# TODO ПЕРЕРЫВ)))


# Декоратор который проверят что арги функции get_sum являются числами, либо функция отрабатывает либо Raise TypeError

def check_type(func: Callable) -> Callable:
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                return None

        return func(*args)

    return wrapper


@check_type
def get_sum(*args):
    return f'Сумма чисел = {sum(args)}'


# get_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(get_sum(1, 2))

# TODO Практика
"""
1. Импортируем marvel full_dict
2. Делаем переменную, в которую помещаем список вложенных словарей (без ключей, только вложенные словари)
3. Делаем функцию, которая принимает этот список вложенных словарей, и возвращает словарь, ключ - title, значение - год выпуска
4. Пишем декоратор валидации, который проверяет, что в словаре, по ключу year лежит int райзим если нет

"""
# 1
from marvel import full_dict

# 2
films_list: List[dict] = [value for value in full_dict.values()]


# 4
def check_year(func: Callable) -> Callable:
    """
    Декоратор валидации, который проверяет, что в словаре, по ключу year лежит int райзим если нет
    :param func:
    :return:
    """

    def wrapper(films: List[dict]):
        for film in films:
            if not isinstance(film['year'], int):
                raise TypeError(f'Значение {film["year"]} не является int')
        return func(films)

    return wrapper


# 3
@check_year
def get_films_year_dict(films: List[dict]) -> dict:
    """
    Возвращает словарь, ключ - title, значение - год выпуска
    :param films:
    :return:
    """
    return {film['title']: film['year'] for film in films}


# 5 Тест
print(get_films_year_dict(films_list))


def strong(func):
    def wrapper():
        print('strong')
        return '<strong>' + func() + '</strong>'

    return wrapper


def emphasis(func):
    def wrapper():
        print('emphasis')
        return '<em>' + func() + '</em>'

    return wrapper


# СНИЗУ ВВЕРХ :)
@strong
@emphasis
def greet():
    return 'Hello!'


print(greet())  # <strong><em>Hello!</em></strong>


# Декоратор с параметрами
# Добавим декоратору возможность принимать значение ключа и так же тип данных на которое нужно проверить значение


def check_dict_key_type(key: str, value_type: type):
    def decorator(func: Callable):
        def wrapper(data: List[dict]):
            for item in data:
                if not isinstance(item[key], value_type):
                    raise TypeError(f'Значение {item[key]} не является {value_type}')
            return func(data)

        return wrapper

    return decorator


@check_dict_key_type('title', str)
def get_films_year_dict2(films: List[dict]) -> dict:
    """
    Возвращает словарь, ключ - title, значение - год выпуска
    :param films:
    :return:
    """
    return {film['title']: film['year'] for film in films}


# Тестируем
print(get_films_year_dict2(films_list))
