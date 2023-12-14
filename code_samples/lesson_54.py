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
Агрегация
Композиция
"""
from typing import List

"""
__call__(self, *args, **kwargs) - вызывается когда объект вызывается как функция
мы можем вызвать объект, например, для запуска какой-то логики, будь то игра в 
Города или что-то другое
"""


class Message:
    def __init__(self, text: str):
        self.text = text


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


"""
Агрегация - это когда объект состоит из других объектов. Мы передаем
готовые объекты в конструктор и используем их внутри нашего объекта.

Композиция - это когда объект состоит из других объектов, но мы создаем
их внутри нашего объекта. То есть, мы создаем объекты внутри нашего объекта
"""


# Greeter - приветствующий вариант с агрегацией
class Greeter:
    def __init__(self, person: Person, message: Message):
        self.person = person
        self.message = message

    def greet(self):
        return f"{self.person.name} {self.message.text} вероятно тебе уже {self.person.age} лет"

    def __call__(self, prefix: str):
        return f"{prefix} {self.greet()}"


# Greeter - приветствующий вариант с композицией
class Greeter2:
    def __init__(self, name: str, age: int, text: str):
        self.person = Person(name, age)
        self.message = Message(text)

    def greet(self):
        return f"{self.person.name} {self.message.text} вероятно тебе уже {self.person.age} лет"

    def __call__(self, prefix: str):
        return f"{prefix} {self.greet()}"


# Создадим оба варианта исполнения
person = Person("Женя", 25)
message = Message("Как дела?")
greeter = Greeter(person, message)
print(greeter('Привет!'))

greeter2 = Greeter2("Женя", 25, "Как дела?")
print(greeter2('Привет!'))
