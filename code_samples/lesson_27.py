"""
Lesson 27
05.12.2023
Наследование в Python Часть 1
- Понятие родительского класса и дочернего класса
- Когда наследование имеет смысл?
- Синтаксис наследования
- Наследование без явного указания инициализатора родительского класса
- Переопределение методов и атрибутов родительского класса
- Работа с инициализатором и явное указание инициализатора родительского класса
- Super - вызов методов родительского класса
- Практика
- Решение практики
- Цепочка наследования
- Переопределение методов

"""


class BigMatryoshka:
    """
    Большая Матрешка.
    Методы:
    - open - открывает матрешку
    """

    def __init__(self):
        self.size = 'big'

    def open(self):
        """
        Открывает матрешку
        """
        print('Opening the big matryoshka')


class MediumMatryoshka(BigMatryoshka):
    """
    Средняя Матрешка.
    Методы:
    - open - открывает матрешку
    - display_info - печатает информацию о матрешке
    """

    def __init__(self, color):
        super().__init__()
        self.color = color

    def open(self):
        """
        Открывает матрешку и вызывает метод open из BigMatryoshka

        :return:
        """
        super().open()
        print('Opening the medium matryoshka')

    def display_info(self):
        """
        Печатает информацию о матрешке
        :return:
        """
        print(f'Размер: {self.size}, цвет: {self.color}')


# Создаем класс SmallMatryoshka
# Унаследованный от MediumMatryoshka

class SmallMatryoshka(MediumMatryoshka):
    """
    Маленькая Матрешка.
    Методы:
    - open - открывает матрешку
    - display_info - печатает информацию о матрешке
    """

    def __init__(self, color):
        super().__init__(color)
        self.size = 'small'

    def open(self):
        """
        Открывает матрешку и вызывает метод open из MediumMatryoshka

        :return:
        """
        super().open()
        print('Opening the small matryoshka')


# Создаем экземпляр класса SmallMatryoshka
# Проверяем работу методов
small_matryoshka = SmallMatryoshka('red')
small_matryoshka.open()


class MattrComplect(BigMatryoshka, MediumMatryoshka, SmallMatryoshka):
    """
    Матрешка комплект.
    Методы:
    - open - открывает матрешку
    - display_info - печатает информацию о матрешке
    """

    def __init__(self, color):
        super().__init__(color)


# Создаем экземпляр класса MattrComplect
# Проверяем работу методов
mattr_complect = MattrComplect('red')

