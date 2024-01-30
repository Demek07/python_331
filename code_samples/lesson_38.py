"""
Lesson 38
Pytest
- pip install pytest
- assert - assert, process, message
- pytest (простой запуск тестов) - но нам надо передать файл, где искать тесты!
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
    ('Москва', 'Астрахань', False),
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
    ]
