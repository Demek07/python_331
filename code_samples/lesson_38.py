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


def is_palindrome(string):
    row_string = string.lower().replace(' ', '')
    return row_string == row_string[::-1]


def divide(a: int, b: int):
    if b == 0:
        raise ZeroDivisionError(f'Вы не можете поделить {a} на 0')
    return a / b





