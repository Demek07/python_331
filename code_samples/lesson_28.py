"""
Lesson 28
07.12.2023
Наследование в Python Часть 2

- Повторение материала про наследование
- Цепочка наследования
- Множественное наследование
"""


# Многоуровневое наследование
class BigMattrioshka:
    pass


class MediumMattrioshka(BigMattrioshka):
    pass


class SmallMattrioshka(MediumMattrioshka):
    pass


# Множественное наследование
class BigMattrioshka:
    pass


class MediumMattrioshka:
    pass


class Smallmatrrioska:
    pass


class ComplectMattrioshka(BigMattrioshka, MediumMattrioshka, Smallmatrrioska):
    pass
