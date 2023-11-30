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

getattr(), setattr(), hasattr() и delattr() - функции для работы с атрибутами класса
getattr(объект, имя_атрибута) - получить значение атрибута
setattr(объект, имя_атрибута, значение) - установить значение атрибута
hasattr(объект, имя_атрибута) - проверить есть ли атрибут у объекта
delattr(объект, имя_атрибута) - удалить атрибут у объекта

Getters, setters и deleters - методы для работы с атрибутами класса
getter - получить значение атрибута
setter - установить значение атрибута
deleter - удалить атрибут
"""


class User:
    """
    Класс для работы с пользователем. Допустим мы пишем программу учета для паспортного стола
    Вот так просто взять и переписать данные пользователя нельзя.
    Нужно сделать проверку данных, перед тем как их записать
    """

    def __init__(self, name: str, age: int):
        self.__min_name_len = 2
        self.__max_name_len = 20
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        """
        Получить имя пользователя. Имя пользователя отдать мы можем и так.
        :return:
        """
        return self.__name

    def __check_len_name(self, name: str) -> bool:
        """
        Приватный метод для проверки длины имени пользователя. Его нет смысла вызывать извне.
        Это внутренний метод, который используется только внутри класса.
        :param name:
        :return:
        """
        return self.__min_name_len <= len(name) <= self.__max_name_len

    @staticmethod
    def __check_is_alpha(name: str) -> bool:
        """
        Приватный метод для проверки имени пользователя на наличие только букв.

        :param name:
        :return:
        """
        return name.isalpha()

    def set_name(self, name: str) -> None:
        """
        Установить имя пользователя. Перед тем как установить имя пользователя, мы должны проверить его.
        Таким образом, мы разрешаем пользователю установить новое имя, но только если оно соответствует нашим требованиям.
        :param name:
        :return:
        """
        if not self.__check_len_name(name):
            raise ValueError(f'Имя должно быть от {self.__min_name_len} до {self.__max_name_len} символов')
        if not self.__check_is_alpha(name):
            raise ValueError('Имя должно состоять только из букв')
        self.__name = name


# Проверяем работу класса

user = User('Николай', 30)
print(user.get_name())
user.set_name('Никола')
print(user.get_name())

"""
Практика!
Создайте класс Password
Который будет хранить пароль пользователя
__password - приватный атрибут для хранения пароля

Создайте методы:
get_password - получить пароль пользователя (просто вернуть значение атрибута)

__check_len_password - приватный метод для проверки длины пароля
set_password - установить пароль пользователя (перед тем как установить пароль, проверить его на длину)

Проведите тестирование.
Результат в чат в виде скриншота терминала :)
"""


class Password:
    def __init__(self):
        self.__password = None
        self.__min_password_len = 8

    def get_password(self) -> str:
        return self.__password

    def __check_len_password(self, password: str) -> bool:
        return len(password) >= self.__min_password_len

    def set_password(self, password: str) -> None:
        if not self.__check_len_password(password):
            raise ValueError(f'Пароль должен быть не короче {self.__min_password_len} символов')
        self.__password = password


password = Password()
password.set_password('1234679546')
print(password.get_password())
