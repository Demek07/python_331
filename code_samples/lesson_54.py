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
__call__(self, *args, **kwargs) - вызывается когда объект вызывается как функция
мы можем вызвать объект, например, для запуска какой-то логики, будь то игра в 
Города или что-то другое
"""

# Экземпляры обычного класса не вызываются как функции
class SomeClass:
    pass


a = SomeClass()
# a()  # TypeError: 'SomeClass' object is not callable
