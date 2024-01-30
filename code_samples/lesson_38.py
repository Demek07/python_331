"""
Lesson 38
Pytest
- pip install pytest
- assert - assert, process, message
- pytest (простой запуск тестов) - но нам надо передать файл, где искать тесты!
- xfail - помечает тест как ожидаемо падающий
- parametrize - позволяет передавать параметры в тестовую функцию
- parametrize + xfail - позволяет передавать параметры в тестовую функцию и помечать тест как ожидаемо падающий
- pytest.raises - проверяет, что в блоке with возбуждается исключение
- fixtures - фикстуры, которые можно использовать в тестах
- параметризация тестов с использованием фикстур
- расположение тестов в проекте?
"""
import pytest

print("Lesson 38")

# assert - проверка условия, если условие не выполняется, то вызывается исключение AssertionError
# assert, process, message
# assert 1 == 1
# assert 1 != 1, "1 != 1" # AssertionError: 1 != 1
# assert all([1 == 100, 2 == 2, 3 == 3]), "Кажется что одно из условий не выполняется"
# assert 'python332' == 'python331', "Строки не равны"


# def is_palindrome(string):
#     return string == string[::-1]
#

# def test_is_palindrome():
#     assert is_palindrome('radar') == False, "Строка не является палиндромом"
#     assert is_palindrome('rafr') == True, "Строка является палиндромом"
#     assert is_palindrome('level') == True, "Строка является палиндромом"
#     assert is_palindrome('sum summus mus') == True, "Строка является палиндромом"


# TODO:
"""
Напишите функцию проверяющую условия игры в Города (последняя буква в названии города должна совпадать 
с первой буквой следующего города):
check_game_rules('first_city', 'second_city') -> True/False

Напишите 1 тест для этой функции, используйте assert. Перед этим установите pytest.
"""


def check_game_rules(first_city, second_city):
    return first_city[-1] == second_city[0].lower()


def test_check_game_rules():
    assert check_game_rules('Москва', 'Астрахань') == True, "Города не подходят"


# Негативное тестирование.
# pytest.mark.xfail - помечает тест как ожидаемо падающий

@pytest.mark.xfail
def test_check_game_rules_negative():
    """
    Негативное тестирование. Тест ожидаемо упадет, т.к. города подходят и функция вернет True
    :return:
    """
    assert check_game_rules('Москва', 'Астрахань') == False, "Города не подходят"


def is_palindrome(string):
    row_string = string.lower().replace(' ', '')
    return row_string == row_string[::-1]


# Параметризация тестов
# pytest.mark.parametrize - позволяет передавать параметры в тестовую функцию

@pytest.mark.parametrize('string, result', [
    ('казак', True),
    ('радар', True),
    ('А роза упала на лапу Азора', True),
    ("Аргентина манит негра", True),
    ("репа", False),
    ("дед", True),

])
def test_is_palindrome(string, result):
    assert is_palindrome(string) == result, "Строка не является палиндромом"


# Выносим параметры в отдельную переменную

test_data = [
    ('казак', True),
    ('радар', True),
    ('А роза упала на лапу Азора', True),
    ("Аргентина манит негра", True),
    ("репа", False),
    ("дед", True),
]


@pytest.mark.parametrize('string, result', test_data)
def test_is_palindrome(string, result):
    assert is_palindrome(string) == result, "Строка не является палиндромом"


# TODO: Параметризуйте тесты для функции check_game_rules

test_data = [
    ('Москва', 'Астрахань', True),
    ('Астрахань', 'Новосибирск', False),
    ('Новосибирск', 'Красноярск', True),
    ('Красноярск', 'Калининград', True),
    ('Калининград', 'Днепропетровск', True),
    ('Днепропетровск', 'Киев', True),
    ('Киев', 'Воронеж', True),
    ('Воронеж', 'Житомир', True),
    ('Житомир', 'Ростов', True),
    ('Ростов', 'Волгоград', True),
    ('Волгоград', 'Донецк', True),
    ('Донецк', 'Киев', True),
    ('Киев', 'Воронеж', True),
    ('Воронеж', 'Житомир', True),
    ('Житомир', 'Ростов', True),
    ('Ростов', 'Волгоград', True),
    ('Волгоград', 'Донецк', True),
    ('Донецк', 'Киев', True),
    ('Киев', 'Воронеж', True),
    ('Воронеж', 'Житомир', True),
    pytest.param("Омск", "Санкт-Петербург", True,
                 marks=pytest.mark.xfail(reason="Города не подходят")),
    ('Житомир', 'Ростов', True),
]


@pytest.mark.parametrize('first_city, second_city, result', test_data)
def test_check_game_rules(first_city, second_city, result):
    assert check_game_rules(first_city, second_city) == result, "Города не подходят"


def divide(a: int, b: int):
    if b == 0:
        raise ZeroDivisionError(f'Вы не можете поделить {a} на 0')
    return a / b


def test_zero_division():
    with pytest.raises(ZeroDivisionError) as exc_info:
        divide(1, 0)
    assert exc_info.type == ZeroDivisionError
    assert str(exc_info.value) == 'Вы не можете поделить 1 на 0'


# Фикстуры - фиксированные данные, которые можно использовать в тестах
# похоже на домашние заготовки

# pytest.fixture - позволяет создавать фикстуры

# Опишем фикстуру, которая читает cities.json и возвращает список городов
import json


@pytest.fixture
def cities():
    with open('../data/cities.json', 'r', encoding='utf-8') as f:
        cities = json.load(f)
    return cities


# Тестовая функция использует фикстуру cities
# проверяет что cities - это список
def test_is_cities_list(cities):
    assert isinstance(cities, list), "cities не является списком"


# # Тестовая функция использует фикстуру cities
# # проверяет что cities[0]- это словарь
def test_is_cities_list_dict(cities):
    assert isinstance(cities[0], dict), "cities[0] не является словарем"


# Проверяем что есть ключ name
def test_is_key_name_in_cities(cities):
    assert 'name' in cities[0], "В cities[0] нет ключа name"


# Пробуем сделать тест с фикстурой + параметризацию
# data = [index, содержимое lat, содержимое lon]
data = [
    (0, '52.65', '90.08333'),
    (1, '53.71667', '91.41667'),
    (2, '53.68333', '53.65'),
]


@pytest.mark.parametrize('index, lat, lon', data)
def test_is_key_name_in_cities(index, lat, lon, cities):
    assert cities[index]['coords']['lat'] == lat, "lat не совпадает"
    assert cities[index]['coords']['lon'] == lon, "lon не совпадает"
