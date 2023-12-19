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
"""
from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Book:
    title: str
    author: str
    year: int = field(compare=False)


book_1 = Book('Гарри Поттер и философский камень', 'Джоан Роулинг', 1997)
# book_1.title = 'Гарри Поттер и тайная комната' # dataclasses.FrozenInstanceError: cannot assign to field 'title'

