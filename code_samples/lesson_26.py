"""
Lesson 26
30.11.2023
Инкасуляция в Python

Инкапсуляция - это механизм языка, который позволяет ограничить доступ к данным и методам класса.

Зачем нужна инкапсуляция?
- чтобы скрыть данные от пользователя
- чтобы скрыть сложную логику от пользователя
- чтобы скрыть внутреннюю реализацию от пользователя

Какие есть виды инкапсуляции?
- public - публичные данные и методы
- protected - защищенные данные и методы
- private - приватные данные и методы

Protected - это когда в начале имени атрибута или метода стоит один нижний подчеркивание
Private - это когда в начале имени атрибута или метода стоит два нижних подчеркивания
__dict__ - словарь с атрибутами экземпляра класса
"""


class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self._protected = 'protected'
        self.__private = 'private'

    @staticmethod
    def _protected_method():
        print(f'Это защищенный метод')

    @staticmethod
    def __private_method():
        print('Это приватный метод')

    @staticmethod
    def public_method():
        print('Это публичный метод')


# Создаем экземпляр класса
user = User('Вася', 20)

# Публичные атрибуты
print(user.name)
print(user.age)

# Защищенные атрибуты
print(user._protected)
# print(user.__private) # Вызовет ошибку AttributeError: 'User' object has no attribute '__private'


# Добудем имена всех атрибутов класса
print(user.__dict__)
print(user._User__private)
