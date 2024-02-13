"""
Не грусти.
Рано или поздно все станет понятно,
все станет на свои места и выстроится в единую красивую схему,
как кружева.

Станет понятно, зачем все было нужно,
потому что все будет правильно.

Льюис Кэрролл. Алиса в стране чудес
"""
from abc import ABC, abstractmethod


class IngredientFactory(ABC):
    """
    Абстрактный класс фабрики для создания ингредиентов.
    """

    @abstractmethod
    def create_cheese(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass


class DodoIngredientFactory(IngredientFactory):
    """
    Конкретная фабрика для создания ингредиентов Додо Пиццы.
    """

    def create_cheese(self):
        return "Моцарелла"

    def create_sauce(self):
        return "Томатный соус"


class SizeFactory:
    """
    Фабрика для создания размеров пиццы.
    """

    def create_size(self, size):
        sizes = {
            'small': 'Маленькая',
            'medium': 'Средняя',
            'large': 'Большая'
        }
        return sizes.get(size.lower(), 'Неизвестный размер')


class PizzaBuilder:
    """
    Класс строителя, который помогает собрать пиццу с заданными параметрами.
    """

    def __init__(self, ingredient_factory, size_factory, pizza_type):
        self.ingredient_factory = ingredient_factory
        self.size_factory = size_factory
        self.pizza_type = pizza_type
        self.size = None

    def set_size(self, size):
        self.size = self.size_factory.create_size(size)

    def build(self):
        cheese = self.ingredient_factory.create_cheese()
        sauce = self.ingredient_factory.create_sauce()
        return f"Пицца '{self.pizza_type}' размера '{self.size}' с {cheese} и {sauce}"


def create_pizza():
    """
    Функция для создания заказа пиццы через консольный интерфейс.
    """
    ingredient_factory = DodoIngredientFactory()
    size_factory = SizeFactory()
    pizza_type = input("Выберите тип пиццы (Маргарита, Пепперони): ")
    size = input("Выберите размер пиццы (small, medium, large): ")

    builder = PizzaBuilder(ingredient_factory, size_factory, pizza_type)
    builder.set_size(size)

    return builder.build()


def main():
    """
    Основная функция для запуска консольного интерфейса.
    """
    order = create_pizza()
    print(f"Ваш заказ: {order}")


if __name__ == "__main__":
    main()
