"""
Lesson 56 - Dataclasses
19.12.2023

- Определение датакласса
- Разница между обычным классом и датаклассом
- Атрибуты по умолчанию
- Параметры декоратора dataclass
    - order=True - генерация дандер методов сравнения (по умолчанию генерируется только __eq__)
    - init=True - генерация метода __init__ (по умолчанию True - но в некоторых случаях может быть полезно отключить)
    - frozen=True - неизменяемый датакласс (по умолчанию False)

- field - параметры для атрибутов
-Параметры field:
    - compare - участвует ли атрибут в сравнении
    - default - значение по умолчанию
    - repr - участвует ли атрибут в repr
    - metadata - словарь с метаданными
    - __dataclass_fields__['category'].metadata - метаданные конкретного атрибута

__post_init__ - метод, который вызывается после инициализации объекта
abstract @dataclass и __post_init__
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod


# абстрактный класс - печатное издание

@dataclass(order=True)
class PrintedEdition(ABC):
    title: str
    type: str
    author: str
    pages: int
    price: int
    issued: bool
    can_issue: bool

    # __post_init__ - метод, который вызывается после инициализации объекта
    # проверяем что при can_issue = False, issued != True
    # нельзя выдать книгу которая НЕ выдается на руки!
    def __post_init__(self):
        if self.can_issue is False and self.issued is True:
            raise ValueError('Нельзя выдать экземпляр который НЕ выдается на руки!')

    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    def get_full_description(self):
        pass


# Делаем наследника - класс книга
"""
У наследника так же, должен быть декоратор @dataclass, потому что именно он генерирует дандер методы сравнения
И что ещё более важно - __init__ который принимает все аргументы, и часть из них передаёт в родительский класс
"""


@dataclass(order=True)
class Book(PrintedEdition):
    genre: str
    year: int

    def get_status(self):
        return 'В наличии' if self.issued else 'Нет в наличии'

    def get_full_description(self):
        return f'{self.title} - {self.author} ({self.year})'


# Экземпляр класса книга
book = Book(title='Война и мир', type='Книга',
            author='Л.Н. Толстой',
            pages=1000, price=1000,
            issued=True,
            can_issue=False,
            genre='Роман', year=1869) # value error - нельзя выдать экземпляр который НЕ выдается на руки!

print(book)
print(book.get_status())
print(book.get_full_description())
