"""
Lesson 34
16.01.2024

- Паттерны проектирования (Порождающие паттерны)
- Singleton
"""


# Singleton - порождающий паттерн проектирования, который гарантирует, что у класса есть только один экземпляр
# и предоставляет к нему глобальную точку доступа.

class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance


# тестируем
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)
print(id(s1), id(s2))


# Реализация логгера с помощью Singleton

class Logger:
    _instance = None  # Статическая переменная для хранения единственного экземпляра

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.log_file = "log.txt"  # Создаем атрибут для хранения пути к файлу логов
        return cls._instance

    def log(self, message):
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(message + "\n")


# Использование Singleton логгера
logger1 = Logger()
logger1.log("Ошибка в приложении")

logger2 = Logger()  # Получаем тот же самый объект
logger2.log("Событие в приложении")

print(logger1 is logger2)  # True, это один и тот же объект
