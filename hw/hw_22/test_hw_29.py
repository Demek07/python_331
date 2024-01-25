"""
Тесты запускаются командой: pytest файл.py
При этом название файла с тестами должно начинаться или заканчиваться на test или _test

Чтобы успешно запустить тесты:

1. Установить pytest: pip install pytest
2. Перейти в папку с файлом домашнего задания
3. Убедитесь, что тесты лежат рядом, и в них правильно импортировано решение
4. Запустить тесты командой: pytest файл.py
5. Получите "6 passed in ... seconds", если тесты прошли успешно

Если тесты не прошли, то вы увидите сообщение об ошибке и строку, в которой она произошла.
Не переживайте, для успешного прохождения тестов, все строки и названия методов и переменных должны совпадать с теми,
что в тестах.
"""
import pytest  # pip install pytest


from hw_29 import DodoIngredientFactory, SizeFactory, PizzaBuilder


# Тестирование DodoIngredientFactory
def test_dodo_ingredient_factory():
    factory = DodoIngredientFactory()
    assert factory.create_cheese() == "Моцарелла"
    assert factory.create_sauce() == "Томатный соус"


# Тестирование SizeFactory
@pytest.mark.parametrize("size, expected", [
    ("small", "Маленькая"),
    ("medium", "Средняя"),
    ("large", "Большая"),
    ("extra_large", "Неизвестный размер")
])
def test_size_factory(size, expected):
    factory = SizeFactory()
    assert factory.create_size(size) == expected


# Тестирование PizzaBuilder
def test_pizza_builder():
    ingredient_factory = DodoIngredientFactory()
    size_factory = SizeFactory()
    builder = PizzaBuilder(ingredient_factory, size_factory, "Маргарита")
    builder.set_size("medium")
    assert builder.build() == "Пицца 'Маргарита' размера 'Средняя' с Моцарелла и Томатный соус"
