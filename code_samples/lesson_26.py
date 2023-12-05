"""
Lesson 26
30.11.2023
Инкапсуляция в Python

Инкапсуляция - это механизм языка, который позволяет ограничить доступ к данным и методам класса.

Зачем нужна инкапсуляция?
- чтобы скрыть данные от пользователя
- чтобы скрыть сложную логику от пользователя
- чтобы скрыть внутреннюю реализацию от пользователя

Какие есть виды инкапсуляции?
- public - публичные данные и методы
- protected - защищенные данные и методы
- private - приватные данные и методы

Protected - это когда в начале имени атрибута или метода стоит один нижнее подчеркивание
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

Сделали практику по инкапсуляции

@property - декоратор для создания геттера
@setter_name.setter - декоратор для создания сеттера
@setter_name.deleter - декоратор для создания делитера
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

    @property
    # геттер. Теперь мы можем обращаться к приватному атрибуту __name через свойство name
    # (как будто это обычный атрибут)
    def name(self) -> str:
        """
        Геттер для имени пользователя
        :return:
        """
        return self.__name

    @name.setter
    # setter - мы используем декоратор по имени функции геттера и добавляем к нему .setter
    # эта логика будет работать при попытке установить значение атрибута name
    def name(self, name: str) -> None:
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

    @name.deleter
    # deleter - мы используем декоратор по имени функции геттера и добавляем к нему .deleter
    # эта логика будет работать при попытке удалить атрибут name
    def name(self) -> None:
        """
        Дилитер для имени пользователя
        :return:
        """
        self.__name = 'Анонимус'


# Проверяем работу класса

user = User('Николай', 30)
print(user.name)
user.name = 'Никола'
# user.name = 'Ник0_ла!!'

print(user.name)

del user.name
print(user.name)

"""
Практика 2. Используем @property для модификации кода из прошлого примера.
Обновите геттер и сеттер для приватного атрибута __password
Опишите дилитер для приватного атрибута __password - который выставит пароль по умолчанию

Протестируйте установку пароля, получение пароля и удаление пароля
"""


class Password:
    def __init__(self):
        self.__password = None
        self.__min_password_len = 8

    def __check_min_password_len(self, new_password: str) -> bool:
        return len(new_password) >= self.__min_password_len

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, new_password: str) -> None:
        if self.__check_min_password_len(new_password):
            self.__password = new_password
        else:
            raise ValueError(f'Пароль должен быть длиннее {self.__min_password_len}\n'
                             f'Добавьте хотя бы еще {self.__min_password_len - len(new_password)} знаков')

    @password.deleter
    def password(self) -> None:
        self.__password = 'qwerty'


password = Password()
print(password.password)
password.password = 13216584
print(password.password)
del password.password
print(password.password)