"""
Lesson 56 -
Разбор ДЗ
Metaclasses
Inner Classes
21.12.2023

"""
"""
вот текстовая UML-диаграмма, описывающая отношения между object, type и пользовательским классом в Python:

lua

+------------+        +---------+
|            |        |         |
|    type    |<-------| MyClass |
|            |        |         |
+------+-----+        +---------+
       ^
       |
+------+------+
|             |
|   object    |
|             |
+-------------+

Объяснение:

    type: Это метакласс в Python, от которого наследуются все классы, включая сам type. 
    Он представляет собой тип всех классов и используется Python для создания новых классов.

    object: Это базовый класс для всех объектов в Python. Все классы, включая type, 
    неявно наследуются от object, обеспечивая базовый функционал объектов в Python.

    MyClass: Это пользовательский класс, который, как и все классы в Python, неявно наследуется 
    от type (потому что type — это метакласс для всех классов) и от object 
    (потому что все классы являются объектами и наследуют базовый функционал).
"""

# Определение метакласса
class AddHello(type):
    def __init__(cls, name, bases, dct):
        # Добавление метода hello к классу
        cls.hello = lambda self: print("Привет от", self.__class__.__name__)


# Определение класса с использованием метакласса AddHello
class MyClass(metaclass=AddHello):
    pass


# Использование класса
instance = MyClass()
instance.hello()  # Выведет: Привет от MyClass


# Определение метакласса
class SimpleMeta(type):
    """
    Метакласс, который добавляет метод greet и атрибут greeting к классу.
    Через переопределение метода __new__.
    cls - класс, который создается
    name - имя класса
    bases - базовые классы
    dct - атрибуты класса
    """

    def __new__(cls, name, bases, dct):
        # Добавляем новый метод к dct
        dct["greet"] = lambda self: print(f"Hello from {self.greeting}!")
        # Добавляем новый атрибут к dct
        dct["greeting"] = "SimpleClass"
        # Создаем новый класс с помощью type.__new__
        return super(SimpleMeta, cls).__new__(cls, name, bases, dct)


# Определение класса с использованием метакласса SimpleMeta
class MyClass(metaclass=SimpleMeta):
    pass


# Использование класса
my_instance = MyClass()
my_instance.greet()  # Вызывает метод, добавленный метаклассом
