"""
Lesson 36
23.01.2024
Паттерны поведения
- Strategy (стратегия)
- Observer (наблюдатель)
- Command (команда)
"""

from typing import List


class Command:
    """
    Абстрактный класс команды. Определяет интерфейс для выполнения команды.
    """

    def execute(self):
        raise NotImplementedError


class AddCommand(Command):
    """
    Конкретная команда для выполнения операции сложения.
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a + self.b


class SubtractCommand(Command):
    """
    Конкретная команда для выполнения операции вычитания.
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a - self.b


class Calculator:
    """
    Инициатор команд, выполняющий команды и возвращающий результат.
    """

    def execute_command(self, command: Command):
        return command.execute()


# Клиентский код
calculator = Calculator()
commands: List[Command] = [
    AddCommand(10, 5),  # команда сложения
    SubtractCommand(10, 5)  # команда вычитания
]

for cmd in commands:
    print(f"Результат операции: {calculator.execute_command(cmd)}")


class Light:
    """ Устройство: Свет """

    def turn_on(self):
        return "Свет включен"

    def turn_off(self):
        return "Свет выключен"


class TV:
    """ Устройство: Телевизор """

    def turn_on(self):
        return "Телевизор включен"

    def turn_off(self):
        return "Телевизор выключен"


class Command:
    """ Интерфейс команды """

    def execute(self):
        raise NotImplementedError


class TurnOnCommand(Command):
    """ Команда для включения устройства """

    def __init__(self, device):
        self.device = device

    def execute(self):
        return self.device.turn_on()


class TurnOffCommand(Command):
    """ Команда для выключения устройства """

    def __init__(self, device):
        self.device = device

    def execute(self):
        return self.device.turn_off()


class RemoteControl:
    """ Пульт управления, работающий с командами"""

    def submit(self, command):
        return command.execute()


# Клиентский код
light = Light()
tv = TV()

turn_on_light = TurnOnCommand(light)
turn_off_light = TurnOffCommand(light)

turn_on_tv = TurnOnCommand(tv)
turn_off_tv = TurnOffCommand(tv)

remote = RemoteControl()

print(remote.submit(turn_on_light))  # Включает свет
print(remote.submit(turn_off_light))  # Выключает свет
print(remote.submit(turn_on_tv))  # Включает телевизор
print(remote.submit(turn_off_tv))  # Выключает телевизор
