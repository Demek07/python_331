"""
Lesson 20
14.11.2023
Python331

1. Разбор ДЗ №13
2. Декораторы
"""
import time
from pprint import pprint
from typing import List, Dict, Any, Callable

# 1. Сделайте импорт `full_dict` из документа `Marvel.py`
from marvel import full_dict

# 2. Напишите пользовательский ввод цифр через пробел, разбейте его на список,
# и примените к каждому элементу списка `int` используя `map`, но только в том случае,
# если этот элемент списка число, иначе замените его на `None`

# user_input: List[str] = input('Введите числа через пробел: ').split(' ')
# user_input_int: List[int | None] = list(map(lambda x: int(x) if x.isdigit() else None, user_input))
# pprint(user_input_int)

# 3. Используйте `filter` и получите аналогичный по структуре словарь,
# который будет содержать исходные `id` и остальные ключи, но только
# тех фильмов, `id` которых есть в полученном списке в п.2

# filtered_by_id: dict = dict(filter(lambda x: x[0] in user_input_int, full_dict.items()))
# pprint(filtered_by_id)
# 4. Составьте `set comprehension` (генератор множества) собрав множество содержимого ключа
#  `director` словаря дата-сета

# directors_set_comprehansion: set = {movie['director'] for movie in full_dict.values() if movie['director'] != 'TBA'}
# pprint(directors_set_comprehansion)

# 5. Составьте `dict comprehension` (генератор словаря) сделав копию исходного словаря `full_dict`,
# при этом применим в к каждому `'year'` значению, функцию `str`

# str_dict_comprehansion: Dict[int, Dict[str, str]] = {key: {k: str(v) if k == 'year' else v
#                                                            for k, v in value.items()} for key, value in
#                                                      full_dict.items()}
#
# # Второй вариант где мы вручную указываем ключи вложенного словаря
# # pprint(str_dict_comprehansion)
#
# str_dict_comprehansion2: Dict[int, Dict[str, str]] = {key:
#                                                           {'title': value['title'],
#                                                            'year': str(value['year']),
#                                                            'director': value['director'],
#                                                            'screenwriter': value['screenwriter'],
#                                                            'producer': value['producer'],
#                                                            'stage': value['stage']}
#                                                       for key, value in full_dict.items()}
#
#
#
# # pprint(str_dict_comprehansion2)
#
# # 6. Используйте `filter` и получите аналогичный по структуре словарь, который будет содержать
# #  исходные `id` и остальные ключи, но только тех фильмов, которые начинаются на букву `Ч`
#
# filtered_by_ch: Dict[int, Dict[str, Any]] = dict(filter(lambda x: x[1]['title'].startswith('Ч'), full_dict.items()))
# # pprint(filtered_by_ch)
# # 7. Сделайте сортировку словаря `full_dict` по одному (любому) параметру,
# # с использованием `lambda` на выходе аналогичный по структуре словарь.
# # Обязательно подпишите, по какому параметру вы делаете сортировку!
#
# # Вариант 1. Сортировка по одному параметру ("title" - название фильма)
# sorted_by_title: Dict[int, Dict[str, str | int]] = dict(sorted(full_dict.items(), key=lambda x: x[1]['title']))
# # pprint(sorted_by_title, sort_dicts=False)
#
# # Вариант 2. Соритровка по 2 параметрам. В первую очередь по году выпуска year, во вторую по названию фильма title
# # sorted_by_year_and_title: Dict[int, Dict[str, str | int]] = dict(sorted(full_dict.items(), key=lambda x: (x[1]['year'], x[1]['title'])))
#
# # 9. Опционально: напишите однострочник, в котором мы получаем аналогичный по структуре
# # `full_dict` но отфильтрованный через `filter` и с использованием в этой же строке `sorted`
#
# # Фильтруем а потом сортируем фильмы. Добываем фильмы на букву "Ч" и сортируем по году выпуска
# filtered_by_ch_and_sorted_by_year: Dict[int, Dict[str, str]] = dict(
#     sorted(filter(lambda x: x[1]['title'].startswith('Ч'), full_dict.items()),
#            key=lambda x: 3000 if x[1]['year'] == 'TBA' else x[1]['year']))
#
# pprint(filtered_by_ch_and_sorted_by_year, sort_dicts=False)

# TODO Практика
"""
Напишите функцию которая делает принт (ничего не принимает, ничего не отдает
Напишите декоратор который будет делать принт до и после вызова функции
Опцоинально: тайпхинты
"""


def simply_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')

    return wrapper


@simply_decorator
def some_func():
    print(f'Hello')


some_func()

# TODO Практика
"""
Добавьте арги и кварги в декоратор и функцию
"""


def simply_decorator(func):
    def wrapper(*args, **kwargs):
        print('Start')
        func(*args, **kwargs)
        print('End')

    return wrapper


@simply_decorator
def some_func(name, middle_name):
    print(f'Hello {name} {middle_name}')


some_func('Матвей', 'Прохорович')

"""
time.perf_counter() — это функция из модуля time в стандартной библиотеке Python, которая предоставляет доступ к 
монотонному счётчику времени с наивысшим доступным разрешением для измерения коротких промежутков времени. 
Вот несколько ключевых моментов об time.perf_counter():

Монотонность: Этот счетчик является монотонным, что означает, что его значения никогда не уменьшаются. 
Это важно для измерения временных интервалов, так как это гарантирует, что разница между концом и началом 
интервала всегда будет положительной или нулевой, даже если системные часы изменяются.

Высокое разрешение: Функция предоставляет время с высокой точностью, что делает ее идеальной для замера 
времени выполнения операций, особенно когда требуется измерить очень короткие промежутки времени.

Независимость от системного времени: Значение, возвращаемое time.perf_counter(), не зависит от системного 
времени и не подвержено изменениям из-за корректировки часов или перехода на летнее/зимнее время.

Использование: Эта функция часто используется для бенчмаркинга и профилирования кода, поскольку 
она предоставляет более точные измерения времени, чем time.time() или time.clock().

Платформонезависимость: time.perf_counter() работает на различных платформах, 
предоставляя стабильный интерфейс для замера времени.

Возвращаемое значение: Функция возвращает время в секундах как число с 
плавающей точкой. С момента запуска Python (или от момента первого вызова time.perf_counter(), 
точное определение зависит от реализации) до момента вызова функции.


start_time = time.perf_counter()
finish_time = time.perf_counter()
"""


def check_time_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        finish_time = time.perf_counter()
        result_time = finish_time - start_time
        print(f'Прошло {result_time:.10f} секунд')

    return wrapper


from cities import cities_list


# Функция которая пробегает по списку городов и возвращает список городов в котором есть буква (которую принимает функция)
# Работа в цикле

@check_time_decorator
def get_city_by_letter_in_for(letter: str) -> List[str]:
    result_list: List[str] = []
    for city in cities_list:
        if letter in city:
            result_list.append(city)
    return result_list


# Это же в списковом включении
@check_time_decorator
def get_city_by_letter_in_comprehension(letter: str) -> List[str]:
    return [city for city in cities_list if letter in city]


# Вызываем функцию 1
# get_city_by_letter_in_for('а')
# Вызываем функцию 2
# get_city_by_letter_in_comprehension('а')


# Декораторы с параметрами
# Декораторы с параметрами - это функции, которые принимают параметры и возвращают декоратор.

def print_decorator(func: Callable) -> Callable:
    def wrapper() -> None:
        print("Start")
        func()
        print("End")

    return wrapper


# Этот же декоратор, но чтобы он принимал 2 параметра, это префикс и постфикс
# Первая функция передает параметры декоратора в обвертку
def print_decorator2(prefix: str, postfix: str) -> Callable:
    # Вторая функция передает обворачиваемую функцию в обвертку
    def decorator(func: Callable) -> Callable:
        # Третья функция - сама обвертка
        def wrapper(name) -> None:
            print(prefix)
            func(name)
            print(postfix)

        return wrapper

    return decorator


def print_hello(name: str) -> None:
    print(f'Hello {name}')

print('start')
f: Callable = print_decorator2("Start", "End")(print_hello)
f("Олег")

"""
f -> wrapper отрабатывает внутри декоратора print_decorator2("Start", "End")
"""


# Используем синтаксис декораторов

@print_decorator2("Ад", "Рай")
def print_hello2(name: str) -> None:
    print(f'Hello {name}')


print_hello2('Прохор Шаляпин')