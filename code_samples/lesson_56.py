"""
Lesson 56 - Dataclasses
19.12.2023

- Определение датакласса
- Разница между обычным классом и датаклассом
- Атрибуты по умолчанию
- Параметры декоратора dataclass
    - order=True - генерация дандер методов сравнения (по умолчанию генерируется только __eq__)

- field - параметры для атрибутов
-Параметры field:
    - compare - участвует ли атрибут в сравнении
    - default - значение по умолчанию
    - repr - участвует ли атрибут в repr
    - metadata - словарь с метаданными
    - __dataclass_fields__['category'].metadata - метаданные конкретного атрибута

"""
from dataclasses import dataclass, field


@dataclass(order=True)
class Book:
    title: str
    author: str = field(compare=False)
    year: int = field(compare=False)
    category: str = field(default='Без категории',  # значение по умолчанию
                          compare=False,  # участвует ли атрибут в сравнении
                          repr=False,  # участвует ли атрибут в repr
                          # метаданные (могут быть использованы в других библиотеках)
                          metadata={'marshmallow': {'load_only': True}}
                          )


book_1 = Book('Война и мир', 'Лев Толстой', 1869)
book_2 = Book('Преступление и наказание', 'Федор Достоевский', 1866)
book_3 = Book('Мастер и Маргарита', 'Михаил Булгаков', 1966)

books = [book_1, book_2, book_3]

print(book_1)

# печатаем метадату - вероятно это никогда не пригодится, но пусть будет
# print(book_1.__dataclass_fields__['category'].metadata)
