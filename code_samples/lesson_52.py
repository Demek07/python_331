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

# Как сравниваются строки на примере метода __eq__

string1 = 'Hello'
string2 = 'hellO'

print(string1 == string2)  # False
print(string1 > string2)  # False
print(string1 < string2)  # True

# Печатаем индексы символов в строках
[print(f'{string1[i]} - {ord(string1[i])}') for i in range(len(string1))]
[print(f'{string2[i]} - {ord(string2[i])}') for i in range(len(string2))]

"""
Сравнение строк в Python происходит лексикографически, что похоже на сравнение в словаре или телефонной книге. 
При этом сравнении используется порядковый номер каждого символа в Unicode.

Как Происходит Сравнение Строк:

    Посимвольное Сравнение:
        Сравнение начинается с первых символов двух строк.
        Если первые символы равны, сравнение продолжается со следующими символами, и так далее.

    Остановка Сравнения:
        Сравнение прекращается, когда найдены различные символы в соответствующих позициях.
        Если одна строка является началом другой, более короткая строка считается "меньшей".
"""

index_list_1 = [ord(string1[i]) for i in range(len(string1))]
index_list_2 = [ord(string2[i]) for i in range(len(string2))]

# Сравнение по индексам в цикле, как только один из символов будет больше, цикл прервется

for i in range(len(index_list_1)):
    if index_list_1[i] > index_list_2[i]:
        print(f'{string1[i]} > {string2[i]}')
        break
    elif index_list_1[i] < index_list_2[i]:
        print(f'{string1[i]} < {string2[i]}')
        break
    else:
        print(f'{string1[i]} = {string2[i]}')