import pytest

from code_samples.lesson_38 import check_game_rules, is_palindrome, divide


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


# Параметризация тестов
# pytest.mark.parametrize - позволяет передавать параметры в тестовую функцию

@pytest.mark.parametrize('string, result', [
    ('Казак', True),
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


@pytest.fixture(scope='module')
def cities():
    with open(r'C:\Users\user\Syncthing\Работа\Academy_Top\ПРИМЕРЫ КОДА\python_331\data\cities.json', 'r', encoding='utf-8') as f:
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
