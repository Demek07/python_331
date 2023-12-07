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
- Миксины - классы, которые содержат в себе какую-то логику, которую можно добавить в другие классы
"""

from abc import ABC, abstractmethod


class AbstractMatryoshka(ABC):
    """
    Класс Матрешка.
    Методы:
    - open - открывает матрешку
    - display_info - печатает информацию о матрешке
    """

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def open(self):
        """
        Открывает матрешку
        :return:
        """
        pass

    def display_info(self):
        """
        Печатает информацию о матрешке
        :return:
        """
        print(f'Цвет: {self.color}')


class MetallMixin:
    """
    Миксин для металлических игрушек
    """
    def __init__(self):
        self.material = 'metal'

    def colorize_metall(self):
        """
        Метод для покраски металлических игрушек
        :return:
        """
        print('Colorize metall matryoshka')


class WoodenMixin:
    """
    Миксин для деревянных игрушек
    """
    def __init__(self):
        self.material = 'wood'

    def colorize_wooden(self):
        """
        Метод для покраски деревянных игрушек
        :return:
        """
        print('Colorize wooden matryoshka')


class BigMatryoshka(AbstractMatryoshka):
    """
    Большая Матрешка.
    Методы:
    - open - открывает матрешку
    """

    def __init__(self, color):
        super().__init__(color)
        self.size = 'big'

    def open(self):
        """
        Открывает матрешку
        """
        print('Opening the big matryoshka')


class BigMetallMatryoshka(BigMatryoshka, MetallMixin):
    """
    Большая металлическая Матрешка.
    Методы:
    - open - открывает матрешку
    """

    def __init__(self, color):
        super().__init__(color)
        self.size = 'big'
        self.colorize_metall()

    def open(self):
        """
        Открывает матрешку
        """
        print('Opening the big matryoshka')


"""
В данном примере у нас есть абстрактный класс AbstractMatryoshka
От которого будут наследоваться все остальные классы матрешек.

Есть миксины MetallMixin и WoodenMixin. Т.е. у нас может быть группа миксинов
связанных с материалом. Так же, у нас может быть группа миксинов, связанная с 
тематикой матрешки (политика, покемоны, мультфильмы и т.д.)

И конечно же с производственным оборудованием.

Миксины словно приправы, которые мы добавляем в нашу матрешку.

В итоге, конечная реализация - рабочий класс, экземпляры которого мы будем создавать
это будет класс BigMetallMatryoshka, который наследуется от BigMatryoshka и MetallMixin.

Таким образом, мы можем создавать разные комбинации матрешек, в зависимости от того,
какие миксины мы будем добавлять.

Например БольшаяМеталлическаяПокемонМатрешка
Или МаленькаяДеревяннаяПикачуМатрешка

И все это возможно благодаря миксинам. При этом каждый класс отвечает за свою логику.
И мы очень легко и быстро сможем её изменить, добавить или убрать.
"""