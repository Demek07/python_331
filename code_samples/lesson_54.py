"""
Lesson 54
14.12.2023

Магические методы для арифметических операций

- Exception - исключение
- __add__(self, other) - сложение
- __sub__(self, other) - вычитание
- __mul__(self, other) - умножение
- __truediv__(self, other) - деление
- __floordiv__(self, other) - целочисленное деление
- __mod__(self, other) - остаток от деления
- __pow__(self, other) - возведение в степень

Операции "на месте" - inplace. Изменяют объект на месте. Например +=, -=, *=, /=, //=, %=, **=
- __iadd__(self, other) - сложение
- __isub__(self, other) - вычитание
- __imul__(self, other) - умножение
- __itruediv__(self, other) - деление
- __ifloordiv__(self, other) - целочисленное деление
- __imod__(self, other) - остаток от деления
- __ipow__(self, other) - возведение в степень


Обратные арифметические методы
- __radd__(self, other) - сложение
- __rsub__(self, other) - вычитание
- __rmul__(self, other) - умножение
- __rtruediv__(self, other) - деление
- __rfloordiv__(self, other) - целочисленное деление
- __rmod__(self, other) - остаток от деления
- __rpow__(self, other) - возведение в степень


__call__(self, *args, **kwargs) - вызывается когда объект вызывается как функция
"""
from typing import List

"""
Мы можем складывать и вычитать и делать другие математические операции с экземплярами классов,
И это вовсе не обязательно должны быть экземпляры одного и того же класса.

Мы можем описать любую логику в этих методах, которая нам нужна.

Пример с классом Книга и классом Книжная полка. Мы можем описать логику, которая будет
позволять прибавлять книги к книжной полке, вычитать книги из книжной полки.

Опишем исключение BookMathException, которое будет вызываться, когда мы попытаемся умножить, делить,
возвести в степень книгу. Так как это не имеет смысла.

Будем использовать методы in-place, которые изменяют объект на месте. Например +=, -=, для остальных
сделаем заглушку в виде raise BookMathException
"""


class BookMathException(Exception):
    """
    Исключение, которое вызывается, когда мы пытаемся умножить, делить, возвести в степень книгу.
    """
    pass


class Book:
    """
    Класс Книга
    """

    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f'Книга "{self.title}" автора {self.author}. Цена: {self.price} рублей.'

    def __repr__(self):
        return f'Книга "{self.title}" автора {self.author}. Цена: {self.price} рублей.'


class BookShelf:
    """
    Класс Книжная полка
    """
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self):
        return (f'Книг на полке: {len(self.books)}'
                f'\n{self.books}')

    def __repr__(self):
        return f'Книжная полка с книгами: {self.books}'

    def __iadd__(self, other):
        """
        Метод сложения в-place
        """
        if isinstance(other, Book):
            self.books.append(other)
            return self
        else:
            raise BookMathException("Можно складывать только книги")

    def __isub__(self, other):
        """
        Метод вычитания в-place
        """
        if isinstance(other, Book):
            self.books.remove(other)
            return self
        else:
            raise BookMathException("Можно вычитать только книги")

    def __add__(self, other):
        raise BookMathException("Можно складывать только книги")




# Создадим несколько экземпляров класса Книга
book_1 = Book("Война и мир", "Лев Толстой", 2000)
book_2 = Book("Преступление и наказание", "Федор Достоевский", 1500)
book_3 = Book("Мастер и Маргарита", "Михаил Булгаков", 1800)
book_4 = Book("Гарри Поттер и философский камень", "Джоан Роулинг", 1200)
book_5 = Book("Гарри Поттер и тайная комната", "Джоан Роулинг", 1300)

# Создадим экземпляр класса Книжная полка
book_shelf = BookShelf([book_1, book_2, book_3])

# Проверим методы
print(book_shelf)

book_shelf += book_4
print(book_shelf)

book_shelf -= book_2
print(book_shelf)