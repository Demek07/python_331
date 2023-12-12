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

    __str__(self):
        Возвращает строковое представление объекта. Используется для пользовательского вывода.


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
        if isinstance(other, Kettlebell):
            return self.weight == other.weight
        return NotImplemented

    def __ne__(self, other):
        """
        Метод __ne__ определяет поведение оператора неравенства !=.
        :param other:
        :return:
        """
        if isinstance(other, Kettlebell):
            return self.weight != other.weight
        return NotImplemented

    def __lt__(self, other):
        """
        Метод __lt__ определяет поведение оператора "меньше" <.
        :param other:
        :return:
        """
        if isinstance(other, Kettlebell):
            return self.weight < other.weight

    def __le__(self, other):
        """
        Метод __le__ определяет поведение оператора "меньше или равно" <=.
        :param other:
        :return:
        """
        if isinstance(other, Kettlebell):
            return self.weight <= other.weight
        return NotImplemented

    def __gt__(self, other):
        """
        Метод __gt__ определяет поведение оператора "больше" >.
        :param other:
        :return:
        """
        if isinstance(other, Kettlebell):
            return self.weight > other.weight
        return NotImplemented

    def __ge__(self, other):
        """
        Метод __ge__ определяет поведение оператора "больше или равно" >=.
        :param other:
        :return:
        """
        if isinstance(other, Kettlebell):
            return self.weight >= other.weight
        return NotImplemented

    def __str__(self):
        """
        Метод __str__ возвращает строковое представление объекта.
        Используется для пользовательского вывода.
        :return:
        """
        return f'Гиря. Цвет: {self.color}. Вес: {self.weight} кг.'


# Создаем наследника дизайнерскую гирю (добавляем атрибут модель)

class DesignerKettlebell(Kettlebell):
    """
    Класс дизайнерских гирь для занятий спортом
    """

    def __init__(self, weight: int, color: str, model: str):
        super().__init__(weight, color)
        self.model = model

    def __str__(self):
        """
        Метод __str__ возвращает строковое представление объекта.
        Используется для пользовательского вывода.
        :return:
        """
        return f'Дизайнерская гиря. Модель: {self.model}. Цвет: {self.color}. Вес: {self.weight} кг.'


# Создаем наследника дизайнерскую гирю (добавляем атрибут модель)
d_kettlebell_1 = DesignerKettlebell(16, 'синий', 'Классическая')
d_kettlebell_2 = DesignerKettlebell(32, 'синий', 'С перламутровыми пуговицами')
d_kettlebell_3 = DesignerKettlebell(8, 'синий', 'Без пуговиц')


d_kettelbells = [d_kettlebell_1, d_kettlebell_2, d_kettlebell_3]
[print(kettlebell) for kettlebell in d_kettelbells]
d_kettelbells.sort()
[print(kettlebell) for kettlebell in d_kettelbells]
