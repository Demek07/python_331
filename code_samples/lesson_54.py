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

Обратные арифметические методы

__call__(self, *args, **kwargs) - вызывается когда объект вызывается как функция
"""

"""
Создаем собственное исключение AppleMathError
Для этого нам нужно создать класс AppleMathError который наследуется от класса Exception

"""


class AppleMathError(Exception):
    """
    Яблочно-математическое исключение
    """
    pass


class Apple:
    """Класс яблоко
    Да. Наши яблоки можно склеивать как пластелин... Но таков путь)
    """
    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        """Сложение двух яблок. Проверяем что второй объект тоже яблоко
        и возвращаем новое яблоко с размером равным сумме размеров двух яблок"""
        if isinstance(other, Apple):
            return Apple(self.size + other.size)
        else:
            raise AppleMathError("Нельзя складывать яблоки с другими объектами")

    def __sub__(self, other):
        """
        Вычитание двух яблок. Проверяем что второй объект тоже яблоко. Если нет - вызываем исключение.
        Проверяем что разность размеров больше нуля. Если нет - вызываем исключение.
        :param other:
        :return:
        """
        if isinstance(other, Apple):
            if self.size - other.size > 0:
                return Apple(self.size - other.size)
            else:
                raise AppleMathError("Разность размеров яблок должна быть больше нуля")
        else:
            raise AppleMathError("Нельзя вычитать из яблока другие объекты")


apple1 = Apple(10)
apple2 = Apple(20)
apple3 = Apple(30)

apple4 = apple1 + apple2
print(apple4.size)

try:
    apple5 = apple1 - apple3
except AppleMathError as e:
    print(e)
