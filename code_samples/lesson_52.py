"""
Lesson 52
12.12.2023

Магические методы. Dunder methods.
Dunder - double underscore

__init__ - конструктор класса

Методы Сравнения

    __eq__(self, other):
        Определяет поведение оператора равенства ==.
        Пример: def __eq__(self, other): ...

    __ne__(self, other):
        Определяет поведение оператора неравенства !=.
        Пример: def __ne__(self, other): ...

    __lt__(self, other):
        Определяет поведение оператора "меньше" <.
        Пример: def __lt__(self, other): ...

    __le__(self, other):
        Определяет поведение оператора "меньше или равно" <=.
        Пример: def __le__(self, other): ...

    __gt__(self, other):
        Определяет поведение оператора "больше" >.
        Пример: def __gt__(self, other): ...

    __ge__(self, other):
        Определяет поведение оператора "больше или равно" >=.
        Пример: def __ge__(self, other): ...

"""


class Kettlebell:
    """
    Класс гирь для занятий спортом
    """
    def __init__(self, weight: int, color: str):
        self.weight = weight
        self.color = color

    def __eq__(self, other):
        """
        Метод __eq__ определяет поведение оператора равенства ==.
        :param other:
        :return:
        """
        return self.weight == other.weight

    def __ne__(self, other):
        """
        Метод __ne__ определяет поведение оператора неравенства !=.
        :param other:
        :return:
        """
        return self.weight != other.weight

    def __lt__(self, other):
        """
        Метод __lt__ определяет поведение оператора "меньше" <.
        :param other:
        :return:
        """
        return self.weight < other.weight

    def __le__(self, other):
        """
        Метод __le__ определяет поведение оператора "меньше или равно" <=.
        :param other:
        :return:
        """
        return self.weight <= other.weight

    def __gt__(self, other):
        """
        Метод __gt__ определяет поведение оператора "больше" >.
        :param other:
        :return:
        """
        return self.weight > other.weight

    def __ge__(self, other):
        """
        Метод __ge__ определяет поведение оператора "больше или равно" >=.
        :param other:
        :return:
        """
        return self.weight >= other.weight

    def __str__(self):
        """
        Метод __str__ возвращает строковое представление объекта.
        Используется для пользовательского вывода.
        :return:
        """
        return f'Гиря. Цвет: {self.color}. Вес: {self.weight} кг.'


kettlebell_1 = Kettlebell(16, 'черный')
kettlebell_2 = Kettlebell(24, 'розовый')
kettlebell_3 = Kettlebell(8, 'оранжевый')
kettlebell_4 = Kettlebell(36, 'синий')
kettlebell_5 = Kettlebell(16, 'бирюзовый')

my_kettlebells = [kettlebell_1, kettlebell_2, kettlebell_3, kettlebell_4, kettlebell_5]

# Сортировка списка kettlebells по весу
# "print comprehension" - как list comprehension, только без создания списка
[print(kettlebell) for kettlebell in my_kettlebells]
my_kettlebells.sort()
print(f'Сортировка по весу:')
[print(kettlebell) for kettlebell in my_kettlebells]

# Проверка приналежности объекта к классу с помощью isinstance()
print(isinstance(kettlebell_1, Kettlebell))