"""
Lesson 52
12.12.2023

Магические методы. Dunder methods.
Dunder - double underscore

__init__ - конструктор класса
Как сравниваются строки
Методы Сравнения
NotImplemented - когда мы не можем сравнить объекты - возвращаем NotImplemented
Как работает сравнение у наследников

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

    Методы Строкового Представления

    __str__(self):
        Определяет поведение функции str(), используемой для неформального строкового представления объекта.
        Пример: def __str__(self): ...

    __repr__(self):
        Определяет поведение функции repr(), используемой для формального строкового представления объекта.
        Пример: def __repr__(self): ...

Другие Полезные Методы

    __bool__(self):
        Определяет поведение преобразования объекта в булево значение, используемое в условных выражениях.
        Пример: def __bool__(self): ...

    __len__(self):
        Определяет поведение функции len(), используемой для определения длины объекта.
        Пример: def __len__(self): ...

@total_ordering - декоратор, который позволяет определить все методы сравнения
Но нам по прежнему надо описать хоть что-то из методов сравнения


Для использования декоратора functools.total_ordering в Python необходимо определить,
как минимум, два метода: __eq__

и один из методов сравнения (__lt__, __le__, __gt__, или __ge__).
"""
from functools import total_ordering
from typing import List


@total_ordering
class City:
    def __init__(self, name:str, population: int, length: int):
        self.name = name
        self.population = population
        self.is_used: bool = False
        self.length = length

    def __str__(self):
        return f"Город: {self.name}, Население: {self.population}"

    def __eq__(self, other):
        """
        Сравнение на равенство будет происходить и по названию и по населению
        В этом случае, ломается логика остальных проверок, сделанных автоматически
        Т.е. тогда надо их прописать вручную
        """
        return self.name == other.name and self.population == other.population

    def __lt__(self, other):
        return self.population < other.population

    def __bool__(self):
        """
        Проверка, был ли использован ли этот город в игре или нет
        :return: True если город использован, False если нет
        """
        return self.is_used

    def __len__(self):
        return self.length

    def is_city_used(self):
        return self.is_used


city1 = City("Moscow", 20000000, 30)
city2 = City("Saint-Petersburg",20000000,  25)
city3 = City("Vologda", 500000, 10)
city4 = City("Krasnodar", 1200000, 7)
city1.is_used = True
city2.is_used = True


cities: List[City] = [city1, city2, city3, city4]

# Как бы могла выглядить проверка на использование города в игре (при условии, что город - это объект класса City)
# Идем циклом по списку и проверяем города на использование

for city in cities:
    if not city:
        print(f'Город {city.name} не использован\n'
              f'Может быть использован в игре\n\n')