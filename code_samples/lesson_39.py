"""
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
import json
import pytest
from unittest.mock import Mock


class JSONReader:
    def read_json(self, json_file_path):
        with open(self.json_file_path, 'r') as json_file:
            return json.load(json_file)


class ItemSearcher:
    def __init__(self, json_reader: JSONReader):
        self.json_reader = json_reader

    def find_item(self, file_name, key, value):
        data = self.json_reader.read_json(file_name)
        return [item for item in data if item[key] == value]


# Фикстура мокирования чтения json файла
@pytest.fixture(scope='module')
def mock_json_reader():
    mock_reader = Mock(spec=JSONReader)  # spec - ограничивает поведение мока
    mock_reader.read_json.return_value = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 35},
        {'name': 'Charlie', 'age': 40}
    ]
    return mock_reader


# Фикстура ItemSearcher с использованием мокирования JSONReader
@pytest.fixture(scope='module')
def item_searcher(mock_json_reader):
    return ItemSearcher(mock_json_reader)


PARAMS = [
    ('users.json', 'name', 'Alice', [{'name': 'Alice', 'age': 30}]),
    ('users.json', 'age', 35, [{'name': 'Bob', 'age': 35}]),
    ('users.json', 'age', 100, [])
]


# Параметризованный тест
@pytest.mark.parametrize('file_name, key, value, expected', PARAMS)
def test_item_searcher(item_searcher, file_name, key, value, expected):
    assert item_searcher.find_item(file_name, key, value) == expected
