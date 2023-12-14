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

"""
Мы можем складывать и вычитать и делать другие математические операции с экземплярами классов,
И это вовсе не обязательно должны быть экземпляры одного и того же класса.

Мы можем описать любую логику в этих методах, которая нам нужна.

Пример с классом Книга и классом Книжная полка. Мы можем описать логику, которая будет
позволять прибавлять книги к книжной полке, вычитать книги из книжной полки.

Опишем исключение BookMathException, которое будет вызываться, когда мы попытаемся умножить, делить,
возвести в степень книгу. Так как это не имеет смысла.
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

    def __init__(self, books: list):
        self.books: list = books

    def __add__(self, other):
        """
        Метод __add__ позволяет добавлять книги к книжной полке. Проверяет что второй объект - это книга.
        Если это не книга - вызывает исключение BookMathException.
        Если это книга - возвращает новую книжную полку с книгами из первой и второй книжной полки.
        """
        if isinstance(other, Book):
            return BookShelf(self.books + [other])
        raise BookMathException("Нельзя складывать книжные полки с чем-то, кроме книг")

    def __str__(self):
        return ''.join([str(book) + '\n' for book in self.books])

    # Описываем остальные методы и ставим заглушку в виде raise BookMathException

    def __sub__(self, other):
        """
        Метод __sub__ позволяет вычитать книги из книжной полки. Проверяет что второй объект - это книга.
        Если это не книга - вызывает исключение BookMathException.
        :param other:
        :return:
        """
        if isinstance(other, Book):
            # BookShelf([book for book in self.books if book != other]) - создаем новый экземпляр класса BookShelf
            # и в него передаем список книг, которые не равны книге other
            return BookShelf([book for book in self.books if book != other])
        raise BookMathException("Нельзя вычитать из книжной полки что-то, кроме книг")

    def __mul__(self, other):
        raise BookMathException("Нельзя умножать книги")

    def __truediv__(self, other):
        raise BookMathException("Нельзя делить книги")

    def __floordiv__(self, other):
        raise BookMathException("Нельзя делить книги")

    def __mod__(self, other):
        raise BookMathException("Нельзя делить книги")

    def __pow__(self, other):
        raise BookMathException("Нельзя возводить книги в степень")




# Создаем экземпляры классов книг
book_1 = Book("Война и мир", "Лев Толстой", 2000)
book_2 = Book("Преступление и наказание", "Федор Достоевский", 1500)
book_3 = Book("Мертвые души", "Николай Гоголь", 1800)
book_4 = Book("Мастер и Маргарита", "Михаил Булгаков", 1900)

# Создаем экземпляр класса книжная полка
book_shelf_1 = BookShelf([book_1, book_2])

print(book_shelf_1)

book_shelf_2 = book_shelf_1 + book_3
print(book_shelf_2)

# book_shelf_3 = book_shelf_2 / book_4 # вызовет исключение BookMathException