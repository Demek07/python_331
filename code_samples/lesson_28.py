"""
Lesson 28
07.12.2023
Наследование в Python Часть 2

- Повторение материала про наследование
- Цепочка наследования
- Множественное наследование
- MRO - Method Resolution Order
"""


# Множественное наследование
"""
Что это такое?
MRO — это список классов, который Python использует для определения порядка поиска методов и атрибутов. 
Если вам нужно найти определённый метод или атрибут в классе, 
Python будет искать его в порядке, заданном MRO.

Зачем это нужно?
Когда у вас есть множественное наследование, может возникнуть вопрос: если один и тот же метод 
или атрибут определён в нескольких родительских классах, 
откуда Python должен взять его? MRO помогает решить эту проблему, указывая чёткий порядок.

Как это работает?
Python использует алгоритм C3 Linearization для создания MRO. 
Этот алгоритм обеспечивает, что порядок будет однозначным и консистентным.
 В общем случае, Python сначала ищет в самом классе, затем в его родителях, согласно порядку MRO.
 
"""
class BigMattrioshka:

    def __init__(self):
        self.size = 'big'

    def open(self):
        print(f'Opening the {self.size} mattrioshka')


class MediumMattrioshka:

        def __init__(self):
            self.size = 'medium'

        def open(self):
            print(f'Opening the {self.size} mattrioshka')

        def is_medium(self):
            return self.size == 'medium'

class Smallmatrrioska:

        def __init__(self):
            self.size = 'small'

        def open(self):
            print(f'Opening the {self.size} mattrioshka')

        def is_small(self):
            return self.size == 'small'


class ComplectMattrioshka(BigMattrioshka, MediumMattrioshka, Smallmatrrioska):
    pass

# Проверяем работу класса
mattrioshka = ComplectMattrioshka()
mattrioshka.open()
print(mattrioshka.is_small())
print(mattrioshka.is_medium())
print(mattrioshka.size)
print(ComplectMattrioshka.__mro__)