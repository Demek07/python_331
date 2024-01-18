"""
Lesson 35
18.01.2024

- Паттерны проектирования (Структурные паттерны)
- Adapter (адаптер)
- Facade (фасад)
- Composite (композит)
"""

"""
Паттерн "Компоновщик" используется для построения иерархических структур объектов, 
где объекты могут быть обработаны одинаковым образом, независимо от того, являются ли они отдельными 
объектами или составными элементами (композитами).
"""


# Базовый класс компонента
class GraphicComponent:
    def render(self):
        raise NotImplementedError


# Лист - Простой графический компонент, например, кнопка
class Button(GraphicComponent):
    def render(self):
        return "Кнопка отрисована"


# Лист - Ещё один простой графический компонент, например, текстовое поле
class TextField(GraphicComponent):
    def render(self):
        return "Текстовое поле отрисовано"


# Композит - Контейнер для графических компонентов
class Panel(GraphicComponent):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def render(self):
        return "Панель с элементами: " + ", ".join(child.render() for child in self.children)


# Клиентский код
button = Button()
textField = TextField()
panel = Panel()

panel.add(button)
panel.add(textField)

print(panel.render())  # Отрисовка панели с кнопкой и текстовым полем
