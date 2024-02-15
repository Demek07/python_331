"""
Lesson 19
09.11.2023
Python331

1. Области видимости переменных
2. Переменные внутри функций
3. Функции внутри функций
4. Замыкания
5. Декораторы
6. Декораторы с параметрами???
"""
from typing import Callable, List, Any


# Области видимости переменных

# 0. Built-in - встроенная область видимости
# Описаны все встроенные функции и переменные
# print = 'Чебурек'
# Сломал принт!!!
# print('Hello world')

# 1. Global - глобальная область видимости
# global_ = 'global'


# 2. Local - локальная область видимости
# a = 1  # global
#
#
# def a_two():
#     a = 2  # local
#     print(a)
#
#
# print(a)  # global
# a_two()  # local
# print(a)  # global

# global внутри функции

# a = 1  # global


# def a_two():
#     global a
#     a = 2  # global!!!
#     print(a)
#
#
# print(a)  # global
# a_two()  # global
# print(a)  # global
#

# 3. Nonlocal - область видимости внутри вложенных функций
# a = 5  # global
#
#
def a_one():
    a = 1  # local a_one

    def a_two():
        nonlocal a
        a = 2  # local a_two
        print(f'Внутри a_two: {a}')
#
#     print(f'Внутри a_one до вызова a_two: {a}')
#     a_two()
#     print(f'Внутри a_one после вызова a_two: {a}')
#
#
# print(f'Внешняя a: {a}')
# a_one()
# print(f'Внешняя a: {a}')


def say_name(name):
    # name - local in say_name
    def say_goodbye():
        print(f"Привет {name}!")

    say_goodbye()
#
#
# say_name("Валера")


###
def say_name2(name: str) -> Callable[[], None]:
    # Олег тут
    def say_goodbye():
        print(f"Привет {name}!")

    return say_goodbye


# sn: Callable = say_name2("Олег")
# sn()
#
# sn = say_name2("Вася")
# sn2 = say_name2("Петя")
#
# sn()
# sn2()

"""
Пока sn ссылается на функцию say_name2, то она не будет удалена из памяти.
Соответственно и Олег останется в переменной name.

Почему замыкание?

Мы держим внутренние окружения и "замыкаем" их по цепочке
Обратившись к sn

sn -> say_name2 -> say_goodbye -> name = "Олег" 
"""

# def sum_a_b(a, b):
#     return a + b
#
#
# new_name: Callable[[int, int], int] = sum_a_b
#
# print(new_name(1, 2))
#
#
# def counter(start: int = 0) -> Callable[[], int]:
#     # Счетчик start
#     def step():
#         nonlocal start
#         start += 1
#         return start
#
#     return step
#
#
# c1: Callable = counter(10)
# c2: Callable = counter()
#
# print(c1())
# print(c1())
# print(c1())
#

# fruits = ["apple", "banana", "cherry", "kiwi", "mango", "lemon", "orange", "grape"]

"""
аннотация List[str] указывает, что fruits должен быть списком строк, 
и аннотация Callable[[], List[str]] указывает, что возвращаемое значение является функцией, 
которая не принимает аргументы (пустые скобки) и возвращает список строк.
"""


# Функция с кешем
# def sort_fruits(fruits: List[str]) -> Callable[[], List[str]]:
#     """
#     Сортируем список и сохраняем результат в кеш
#     :param fruits:
#     :return:
#     """
#     # fruits - local
#     cache: list = []
#
#     def sort() -> List[str]:
#         nonlocal cache
#         if not cache or len(cache) != len(fruits):
#             cache = sorted(fruits)
#         return cache
#
#     return sort
#
# # Тестируем функцию с кешем
#
# sorter: Callable = sort_fruits(fruits)
# print(sorter())
#
# # Вызываем повторно с этими же данными (сортировка не будет произведена - вернется кеш)
# print(sorter())
#
# # Добавляем новый фрукт
# fruits.append("apples")
#
# # Пересортируем
# print(sorter())
#
# print(fruits)


def print_decorator(func: Callable[[], None]) -> Callable[[], None]:
    # func - local
    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper


def some_func() -> None:
    print("Вызов функции some_func")


# some_func()
f: Callable = print_decorator(some_func)
f()

# Изменяем поведение функции some_func
some_func: Callable = print_decorator(some_func)
some_func()

@print_decorator
def some_func2() -> None:
    print("Вызов функции some_func2")


some_func2()



@print_decorator
def some_func3(name: str) -> None:
    print(f"Вызов функции some_func3 с параметром {name}")


some_func3("Матвей") # TypeError: wrapper() takes 0 positional arguments but 1 was given


# Частный случай. Но не универсальный.
def print_decorator2(func: Callable) -> Callable:
    def wrapper(name: str) -> None:
        print("Start")
        func(name)
        print("End")

    return wrapper


@print_decorator2
def some_func4(name: str) -> None:
    print(f"Вызов функции some_func4 с параметром {name}")


some_func4("Матвей")


@print_decorator2
def some_func5(name: str, last_name: str) -> None:
    print(f"Вызов функции some_func5 с параметром {name} и {last_name}")


some_func5("Матвей", "Петров") # TypeError: wrapper() takes 1 positional argument but 2 were given


def print_decorator3(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> None:
        print("Start")
        func(*args, **kwargs)
        print("End")

    return wrapper


@print_decorator3
def some_func6(name: str, last_name: str) -> None:
    print(f"Вызов функции some_func6 с параметром {name} и {last_name}")


@print_decorator3
def some_func7(name: str, last_name: str, age: int) -> None:
    print(f"Вызов функции some_func7 с параметром {name} и {last_name} и {age}")


some_func6("Матвей", "Петров")
some_func7("Матвей", "Петров", 30)


def logger_decorator(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> None:
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            # Запись в файл log.txt в кодировке utf-8
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"Произошла ошибка: {e}\n")


    return wrapper


@logger_decorator
def get_delimiter(a: int, b: int) -> float:
    return a / b


get_delimiter(1, 0)
