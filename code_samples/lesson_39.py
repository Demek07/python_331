"""
Посмотреть pytest.assume - Почему module pytest has no attribute assume


Lesson 39
- Разбор домашнего задания
- Повторение материала
    - @pytest.mark.parametrize
    - @pytest.mark.xfail
    - @pytest.raises
    - @pytest.fixture
    - @pytest.fixture(scope='module')



- Моки?
- @pytest.mark.slow - маркировка тестов
- Вспоминаем генераторы и yield
- Фикстуры и yield
- Разбор тестов с фикстурами + yield
- Тестовые классы
-
"""
from random import randint as random

import pytest

"""
Делаем фикстуру возвращающую 2 рандомных числа с yield
scope = function
После yield - print('Фикстура умерла. Да здравствует фикстура!')

Код после yield выполняется после окончания "срока годности" фикстуры
"""


@pytest.fixture(scope='function')
def random_numbers():
    # pytest.assume('Фикстура родилась')
    yield random(0, 10), random(0, 10)
    # pytest.assume('Фикстура умерла. Да здравствует фикстура!')


def test_is_int(random_numbers):
    assert isinstance(random_numbers[0], int) and isinstance(random_numbers[1], int)


def test_is_positive_int(random_numbers):
    assert random_numbers[0] >= 0 and random_numbers[1] >= 0