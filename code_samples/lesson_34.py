"""
Lesson 34
16.01.2024

- Паттерны проектирования (Порождающие паттерны)
- Singleton
- Builder
"""
from typing import List


# Builder - паттерн, который позволяет создавать сложные объекты пошагово

class MarkdownDocument:
    def __init__(self):
        self.text = ''


class MarkdownBuilder:
    def __init__(self):
        self.document = MarkdownDocument()

    def add_frontmatter(self, fields) -> None:
        pass

    def add_header(self, text: str, level: int = 1) -> None:
        pass

    def add_paragraph(self, text: str) -> None:
        pass

    def write(self, file_name: str) -> None:
        pass


# Клиент - код, который использует билдер
builder = MarkdownBuilder()
builder.add_header('Заголовок')
builder.add_paragraph('Параграф')
builder.add_header('Заголовок 2', 2)
builder.add_paragraph('Параграф 2')
builder.write('markdown.md')


class Burger:
    def __init__(self):
        self.ingredients: List[str] = []

    def add_ingredient(self, ingredient: str) -> None:
        self.ingredients.append(ingredient)

    def __str__(self):
        return f'Бургер с ингредиентами: {self.ingredients}'


class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_lettuce(self) -> None:
        self.burger.add_ingredient("салат")

    def add_tomato(self) -> None:
        self.burger.add_ingredient("помидор")

    def add_cheese(self) -> None:
        self.burger.add_ingredient("сыр")

    def get_burger(self) -> Burger:
        return self.burger


# Клиентский код
builder = BurgerBuilder()
builder.add_cheese()
builder.add_lettuce()
burger = builder.get_burger()
print(burger)
