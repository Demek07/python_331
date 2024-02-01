"""
Pytest для тестирования hw_16.TxtFileHandler класса
Тесты:
1. Создаем фикстуру с экземпляром класса TxtFileHandler
- фикстура с yield
- в конце теста удаляем файл
2. Вызываем метод write_file c пустым списком (проверяем, что файл создался)
3. Вызваем метод append_file с данными (проверяем, что данные дописались в файл)
4
"""
import time

from hw.hw_16 import TxtFileHandler
import pytest
import os

#
# @pytest.fixture(scope='module')
# def txt_handler():
#     txt_handler = TxtFileHandler('test.txt')
#     yield txt_handler
#     try:
#         time.sleep(5)
#         os.remove('test.txt')
#     except FileNotFoundError:
#         pass
#
#
# def test_write_file(txt_handler):
#     txt_handler.write_file([])
#     assert os.path.exists('test.txt')
#
#
# def test_append_file(txt_handler):
#     txt_handler.append_file(['test'])
#     with open('test.txt', 'r', encoding='utf-8') as file:
#         assert file.read() == 'test'
#

"""
Эти же тесты в ООП стиле:
Создаем класс TxtFileHandlerTest
- Поле фикстуры для экземпляра класса TxtFileHandler = None
- Метод setup_class, в котором создаем экземпляр класса TxtFileHandler
- Метод teardown_class, в котором удаляем файл
- Метод test_write_file, в котором вызываем метод write_file c пустым списком (проверяем, что файл создался)
- Метод test_append_file, в котором вызываем метод append_file с данными (проверяем, что данные дописались в файл)
"""

import os
from hw.hw_16 import TxtFileHandler
import pytest


class TestTxtFileHandler:
    @classmethod
    def setup_class(cls):
        """Создание экземпляра класса TxtFileHandler."""
        cls.txt_handler = TxtFileHandler('test.txt')

    @classmethod
    def teardown_class(cls):
        """Удаление файла после выполнения всех тестов."""
        try:
            os.remove('test.txt')
        except FileNotFoundError:
            pass

    def test_write_file(self):
        """Тестирование метода write_file с пустым списком."""
        self.txt_handler.write_file([])
        assert os.path.exists('test.txt')

    def test_append_file(self):
        """Тестирование метода append_file с добавлением данных."""
        self.txt_handler.append_file(['test'])
        with open('test.txt', 'r', encoding='utf-8') as file:
            assert file.read() == 'test'
