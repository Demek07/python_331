"""
Lesson 56 - Dataclasses
19.12.2023

- Определение датакласса
- Разница между обычным классом и датаклассом
- Атрибуты по умолчанию
- Параметры декоратора dataclass
    - order=True - генерация дандер методов сравнения (по умолчанию генерируется только __eq__)
"""
from dataclasses import dataclass

# TODO Практика!
"""
Опишите датакласс для описания книги.
Книга имеет следующие атрибуты:
- Название
- Автор
- Год издания

Создайте 3 экземпляра класса книга.
Создайте список книг.
Сортируйте список книг.
"""


@dataclass(order=True)
class Book:
    title: str
    author: str
    year: int


book_1 = Book('Война и мир', 'Лев Толстой', 1869)
book_2 = Book('Преступление и наказание', 'Федор Достоевский', 1866)
book_3 = Book('Мастер и Маргарита', 'Михаил Булгаков', 1966)

books = [book_1, book_2, book_3]
books.sort()
print(books)  # TypeError: '<' not supported between instances of 'Book' and 'Book'
print(sorted(books, key=lambda book: book.year))
