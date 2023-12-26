"""
Lesson 56 -
Разбор ДЗ
Metaclasses
Inner Classes
21.12.2023

"""


class Car:
    class Engine:
        def __init__(self):
            self.rpm = 0

        def increase_rpm(self, amount):
            self.rpm += amount
            print(f"Текущие обороты двигателя: {self.rpm} RPM.")

    class AcceleratorPedal:
        def __init__(self, engine):
            self.engine = engine

        def press(self, pressure):
            # Предположим, что давление коррелирует с тем, на сколько увеличиваются обороты
            rpm_increase = pressure * 100
            self.engine.increase_rpm(rpm_increase)

    def __init__(self):
        self.engine = self.Engine()
        self.accelerator_pedal = self.AcceleratorPedal(self.engine)

# Создание экземпляра Car и взаимодействие с педалью газа
my_car = Car()
my_car.accelerator_pedal.press(0.5)  # Нажатие на педаль газа
my_car.accelerator_pedal.press(0.3)  # Нажатие на педаль газа еще раз
