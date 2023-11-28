"""
Lesson 25
28.11.2023
Знакомство с ООП в Python
Правила нейминга
Всё в Python - объекты, сравнили свой класс со строкой
Методы и атрибуты класса
Познакомились с __init__ и __new__
Посмотрели как создается экземпляр класса (сначала __new__, потом __init__)
Посмотрели что self позволяет работать с атрибутами и методами экземпляра класса
@staticmethod - декоратор для методов которые не работают с атрибутами класса и экземпляра класса
@classmethod - декоратор для методов которые работают с атрибутами класса
cls - аналог self, но для класса
Понятие полиморфизма на примере работы с файлами
"""


class JsonFile:
    def read_json(self):
        pass


class TxtFile:
    def read_txt(self):
        pass


class CsvFile:
    def read_csv(self):
        pass

# Полиморфизм
"""
У нас есть три разных файла, это экземпляры разных классов
Мы просто хотим пройтись по ним и прочитать данные из них
Как это сделать?

Для этого нам надо вызвать у них РАЗНЫЕ методы.
Т.е. нужно произвести проверку на тип файла и вызвать соответствующий метод
"""
file_1 = JsonFile()
file_2 = TxtFile()
file_3 = CsvFile()


files = [file_1, file_2, file_3]
result = []
for file in files:
    # isinstance - проверяет является ли объект экземпляром класса
    # isinstance(объект, класс)
    if isinstance(file, JsonFile):
        result.append(file.read_json())
    elif isinstance(file, TxtFile):
        result.append(file.read_txt())
    elif isinstance(file, CsvFile):
        result.append(file.read_csv())
    else:
        raise ValueError('Неизвестный тип файла')


class JsonFile:
    def read(self):
        print(f'Читаем файл {self.__class__.__name__}')


class TxtFile:
    def read(self):
        print(f'Читаем файл {self.__class__.__name__}')


class CsvFile:
    def read(self):
        print(f'Читаем файл {self.__class__.__name__}')


file_1 = JsonFile()
file_2 = TxtFile()
file_3 = CsvFile()

files = [file_1, file_2, file_3]

result = []
for file in files:
    """
    Так как у нас у всех файлов есть метод read, мы можем просто вызвать его
    """
    result.append(file.read())
