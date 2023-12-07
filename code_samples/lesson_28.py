"""
Lesson 28
07.12.2023
Наследование в Python Часть 2

- Повторение материала про наследование
- Цепочка наследования
- Множественное наследование
- MRO - Method Resolution Order
- Абстрактные классы
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


big_matryoshka = BigMatryoshka('red')
print(big_matryoshka.get_color())
