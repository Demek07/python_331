"""
Lesson 34
16.01.2024

- Паттерны проектирования (Порождающие паттерны)
- Singleton
- Builder
- Abstract Factory
"""

from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self) -> None:
        pass


class WindowsButton(Button):
    def render(self) -> None:
        print("Рендеринг кнопки в стиле Windows")


class MacOSButton(Button):
    def render(self) -> None:
        print("Рендеринг кнопки в стиле MacOS")


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()


class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()


# Клиентский код
def application(factory: GUIFactory) -> None:
    button = factory.create_button()
    button.render()


# Эмуляция выбора ОС
current_os = "MacOS"
if current_os == "Windows":
    factory = WindowsFactory()
elif current_os == "MacOS":
    factory = MacOSFactory()

application(factory)

