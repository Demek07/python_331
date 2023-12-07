"""
Lesson 28
07.12.2023
Наследование в Python Часть 2

- Повторение материала про наследование
- Цепочка наследования
- Множественное наследование
- MRO - Method Resolution Order
- mro() - метод для получения порядка разрешения методов
- Абстрактные классы
- ABC - Abstract Base Class
- @abstractmethod - декоратор для методов которые должны быть реализованы в потомках
- isinstance() - функция для проверки является ли объект экземпляром класса или его потомком
- issubclass() - функция для проверки является ли класс потомком другого класса
- Миксины - классы, которые содержат в себе какую-то логику, которую можно добавить в другие классы
"""

from abc import ABC, abstractmethod


# Абстрактный класс Матрешка
class Matryoshka(ABC):
    counter = 0

    def __init__(self):
        self.id = Matryoshka.counter
        Matryoshka.counter += 1


# Класс Большая Матрешка
class BigMatryoshka(Matryoshka):
    counter = 0

    def __init__(self):
        super().__init__()
        self.id = Matryoshka.counter
        BigMatryoshka.counter += 1


# Класс Средняя Матрешка
class MediumMatryoshka(BigMatryoshka):
    counter = 0

    def __init__(self):
        super().__init__()
        self.id = Matryoshka.counter
        MediumMatryoshka.counter += 1


# Класс Маленькая Матрешка
class SmallMatryoshka(MediumMatryoshka):
    counter = 0

    def __init__(self):
        super().__init__()
        self.id = Matryoshka.counter
        SmallMatryoshka.counter += 1


# Миксин для деревянных матрешек
class WoodenMixin:
    material = "Wood"

    def varnish(self):
        print("Applying varnish")

    def paint(self):
        print("Painting with wood paint")


# Миксин для металлических матрешек
class MetalMixin:
    material = "Metal"

    def paint_for_metal(self):
        print("Painting with metal paint")


# Класс Деревянной Маленькой Матрешки
class WoodenSmallMatryoshka(SmallMatryoshka, WoodenMixin):
    def __init__(self):
        super().__init__()


# Класс Металлической Маленькой Матрешки
class MetalSmallMatryoshka(SmallMatryoshka, MetalMixin):
    def __init__(self):
        super().__init__()


# Создание экземпляров
wooden_small = WoodenSmallMatryoshka()
metal_small = MetalSmallMatryoshka()

wooden_small_1 = WoodenSmallMatryoshka()
metal_small_1 = MetalSmallMatryoshka()

wooden_small_2 = WoodenSmallMatryoshka()
metal_small_2 = MetalSmallMatryoshka()

# Тестирование методов и атрибутов
wooden_small.paint()
metal_small.paint_for_metal()
print(wooden_small.material, wooden_small.id)
print(metal_small.material, metal_small.id)

# Добудем Matryoshka.counter
print(wooden_small.counter)  # 6
print(wooden_small.id)  # 1

print(wooden_small.counter)  # 6

print(wooden_small_2.id)  # 5
print(metal_small_2.id)  # 6
print(metal_small_2.counter)  # 6
print(metal_small.counter)  # 6

# Counter для big, medium, small
print(BigMatryoshka.counter)

# Создадим экземпляр BigMatryoshka
big = BigMatryoshka()
print(BigMatryoshka.counter)
print(metal_small.counter)

# Mro - Method Resolution Order
print(WoodenSmallMatryoshka.mro())
print(MetalSmallMatryoshka.mro())

# Порядок подмешивания миксинов (в Джанго, есть ли там приоритеты очередности?)
# Почему с миксинами мы не увидели в mro что ABC наследуется от object? (а без них видели)