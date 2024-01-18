"""
Lesson 35
18.01.2024

- Паттерны проектирования (Структурные паттерны)
- Adapter (адаптер)
- Facade (фасад)
"""

"""
Паттерн "Фасад" в программировании представляет собой структурный шаблон проектирования, цель которого - предоставление
 простого интерфейса к сложной системе классов, библиотеке или фреймворку. Основные задачи фасада:

- **Упрощение интерфейса**: Скрыть сложность системы, предоставляя простой интерфейс для взаимодействия с ней.
- **Уменьшение зависимостей**: Снизить зависимость внешнего кода от множества классов в системе, сосредоточив 
взаимодействие через одну точку доступа.

- **Повышение гибкости**: Облегчить изменение и обновление внутренних компонентов системы, не затрагивая клиентский код.
"""


# Подсистема 1: Управление питанием
class PowerManager:
    def turn_on(self):
        return "Питание включено"

    def turn_off(self):
        return "Питание выключено"


# Подсистема 2: Управление звуком
class SoundManager:
    def sound_up(self):
        return "Звук увеличен"

    def sound_down(self):
        return "Звук уменьшен"


# Подсистема 3: Управление сетью
class NetworkManager:
    def connect(self):
        return "Сеть подключена"

    def disconnect(self):
        return "Сеть отключена"


# Фасад: Объединяющий интерфейс для подсистем
class ComputerFacade:
    def __init__(self):
        self.power = PowerManager()
        self.sound = SoundManager()
        self.network = NetworkManager()

    def start_computer(self):
        return self.power.turn_on(), \
            self.sound.sound_up(), \
            self.network.connect()

    def stop_computer(self):
        return self.network.disconnect(), \
            self.sound.sound_down(), \
            self.power.turn_off()


# Клиентский код
facade = ComputerFacade()
print(facade.start_computer())  # Включение компьютера
print(facade.stop_computer())  # Выключение компьютера
