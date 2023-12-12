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
    def __init__(self, weight):
        self.weight = weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def __str__(self):
        return f'Гиря весом {self.weight} кг.'


kettlebell_1 = Kettlebell(16)
kettlebell_2 = Kettlebell(24)

print(f'{kettlebell_1} == {kettlebell_2} - {kettlebell_1 == kettlebell_2}')
print(f'{kettlebell_1} != {kettlebell_2} - {kettlebell_1 != kettlebell_2}')
print(f'{kettlebell_1} < {kettlebell_2} - {kettlebell_1 < kettlebell_2}')
print(f'{kettlebell_1} <= {kettlebell_2} - {kettlebell_1 <= kettlebell_2}')
print(f'{kettlebell_1} > {kettlebell_2} - {kettlebell_1 > kettlebell_2}')
print(f'{kettlebell_1} >= {kettlebell_2} - {kettlebell_1 >= kettlebell_2}')