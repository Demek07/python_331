"""
Lesson 56 - Dataclasses
19.12.2023

- Определение датакласса
- Разница между обычным классом и датаклассом
- Атрибуты по умолчанию
- Параметры декоратора dataclass
    - order=True - генерация дандер методов сравнения (по умолчанию генерируется только __eq__)
    - init=True - генерация метода __init__ (по умолчанию True - но в некоторых случаях может быть полезно отключить)

- field - параметры для атрибутов
-Параметры field:
    - compare - участвует ли атрибут в сравнении
    - default - значение по умолчанию
    - repr - участвует ли атрибут в repr
    - metadata - словарь с метаданными
    - __dataclass_fields__['category'].metadata - метаданные конкретного атрибута

__post_init__ - метод, который вызывается после инициализации объекта
"""
from dataclasses import dataclass, field


@dataclass(init=True)
class Book:
    title: str
    author: str = field(compare=False)
    year: int = field(compare=False)

    # def __init__(self, title: str, author: str, year: int):
    #     self.title = title
    #     self.author = author
    #     self.year = year + 1

    # post_init - метод, который вызывается после инициализации объекта
    # перестает работать, если мы переопределяем __init__
    def __post_init__(self):
        """
        __post_init__ - метод, который вызывается после инициализации объекта
        В нашем случае происходит проверка типов и значений атрибутов
        :return:
        """
        if not isinstance(self.title, str):
            raise TypeError(f'Значение title должно быть строкой, а не {type(self.title)}')

        if not isinstance(self.author, str):
            raise TypeError(f'Значение author должно быть строкой, а не {type(self.author)}')

        if not isinstance(self.year, int):
            raise TypeError(f'Значение year должно быть числом, а не {type(self.year)}')

        if self.year < 0:
            raise ValueError(f'Значение year должно быть положительным числом, а не {self.year}')


book_1 = Book('Война и мир', 'Лев Толстой', -5)
# book_2 = Book('Незнайка на луне', 'Николай Носов', 1965)

print(book_1)
