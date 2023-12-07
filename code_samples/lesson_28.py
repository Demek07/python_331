"""
Lesson 28
07.12.2023
Наследование в Python Часть 2

- Повторение материала про наследование
- Цепочка наследования
- Множественное наследование
- MRO - Method Resolution Order
- mro() - метод для получения порядка разрешения методов
- Абстрактные классы
- ABC - Abstract Base Class
- @abstractmethod - декоратор для методов которые должны быть реализованы в потомках
- isinstance() - функция для проверки является ли объект экземпляром класса или его потомком
- issubclass() - функция для проверки является ли класс потомком другого класса
"""

from abc import ABC, abstractmethod


class AbstractMatryoshka(ABC):
    """
    Абстрактный класс Матрешка.
    Методы:
    - open - открывает матрешку
    - display_info - печатает информацию о матрешке
    """

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def open(self, *args, **kwargs):
        """
        Открывает матрешку
        :return:
        """
        pass

    @abstractmethod
    def display_info(self, *args, **kwargs):
        """
        Печатает информацию о матрешке
        :return:
        """
        pass

    def get_color(self):
        """
        Получить цвет матрешки
        :return:
        """
        return self.color


# TypeError: Can't instantiate abstract class AbstractMatryoshka with abstract methods display_info, open
# abstract_matryoshka = AbstractMatryoshka('red')

class BigMatryoshka(AbstractMatryoshka):
    """
    Большая Матрешка.
    Методы:
    - open - открывает матрешку
    - display_info - печатает информацию о матрешке
    """

    def __init__(self, color):
        super().__init__(color)
        self.size = 'big'

    def open(self):
        """
        Это может быть даже просто заглушка
        Но без этого метода мы не сможем создать экземпляр класса
        :return:
        """
        pass

    def display_info(self):
        """
        Это может быть даже просто заглушка
        Но без этого метода мы не сможем создать экземпляр класса
        :return:
        """
        pass


class MediumMatryoshka(BigMatryoshka):
    """
    Средняя Матрешка.
    Методы:
    - open - открывает матрешку
    - display_info - печатает информацию о матрешке
    """

    def __init__(self, color):
        super().__init__(color)
        self.size = 'medium'


big_matryoshka = BigMatryoshka('red')
medium_matryoshka = MediumMatryoshka('blue')
print(big_matryoshka.get_color())
print(medium_matryoshka.get_color())

# MRO - Method Resolution Order
# mro() - метод для получения порядка разрешения методов

print(MediumMatryoshka.mro())

# isinstance() - функция для проверки является ли объект экземпляром класса или его потомком
print(isinstance(big_matryoshka, BigMatryoshka))  # True
print(isinstance(big_matryoshka, MediumMatryoshka))  # False
print(isinstance(big_matryoshka, AbstractMatryoshka))  # True
print(isinstance(medium_matryoshka, AbstractMatryoshka))  # True

# issubclass() - функция для проверки является ли класс потомком другого класса
print(issubclass(BigMatryoshka, MediumMatryoshka))  # False
print(issubclass(MediumMatryoshka, BigMatryoshka))  # True
print(issubclass(MediumMatryoshka, MediumMatryoshka))  # True
print(issubclass(BigMatryoshka, AbstractMatryoshka))  # True
