"""
Lesson 24
22.11.2023
Повторение основных моментов связанных с Git и Github
Поговорили про:
- переключение между коммитами
- сравнение коммитов
- откат коммитов
- сброс коммитов
- stash и shelve

Ветки:
- создание веток
- переключение между ветками
- слияние веток

Разбор HW_14 - Декораторы
Как работают Any и All
"""
import csv
from typing import Tuple

"""
Необходимо создать два декоратора для валидации пользовательских данных перед их сохранением в CSV формате. 

Первый декоратор (`password_validator`) проверяет:
- сложность пароля
- включая его длину
- количество букв верхнего и нижнего регистра
- и количество спец-знаков. 

Второй декоратор (`username_validator`) проверяет, что в имени пользователя **отсутствуют** пробелы. Создайте функцию 
(`register_user`), которая принимает имя пользователя и пароль, и дозаписывает их в CSV файл, обернув ее **обоими** декораторами.

### Требования:

1. **Декоратор `password_validator`:**
   - Принимает параметры: `min_length` (минимальная длина пароля, по умолчанию 8), `min_uppercase` 
   (минимальное количество букв верхнего регистра, по умолчанию 1), `min_lowercase` 
   (минимальное количество букв нижнего регистра, по умолчанию 1), `min_special_chars` 
   (минимальное количество спец-знаков, по умолчанию 1).
   - Проверяет, соответствует ли пароль заданным критериям.
   - Если пароль не соответствует критериям, выбрасывает `ValueError` с описанием того, что именно не выполнено.

2. **Декоратор `username_validator`:**
   - Не принимает параметров.
   - Проверяет, что в имени пользователя отсутствуют пробелы.
   - Если в имени пользователя есть пробелы, выбрасывает `ValueError` с подробным описанием проблемы.

3. **Функция `register_user`:**
   - Принимает две строки: `username` (имя пользователя) и `password` (пароль).
   - Дозаписывает имя пользователя и пароль в CSV файл.
   - Оборачиваем функцию **обоими** декораторами для валидации введенных данных.
"""


def username_validator(func: callable) -> callable:
    """
    Декоратор для валидации имени пользователя
    :param func:  функция для оборачивания
    :return: обернутая функция
    """

    def wrapper(username: str, password: str) -> None:
        if ' ' in username:
            raise ValueError('В имени пользователя не должно быть пробелов')
        return func(username, password)

    return wrapper


# Декоратор для валидации пароля, который принимает параметры
# И выдает ошибку, если пароль не соответствует критериям или вызывает функцию, если все хорошо
def password_validator(min_length: int = 8, min_uppercase: int = 1, min_lowercase: int = 1,
                       min_special_chars: int = 1) -> callable:
    def decorator(func: callable) -> callable:
        def wrapper(username: str, password: str) -> None:
            if len(password) < min_length:
                raise ValueError(f'Пароль должен быть не короче {min_length} символов')
            if sum(1 for char in password if char.isupper()) < min_uppercase:
                raise ValueError(f'Пароль должен содержать не менее {min_uppercase} символов в верхнем регистре')
            if sum(1 for char in password if char.islower()) < min_lowercase:
                raise ValueError(f'Пароль должен содержать не менее {min_lowercase} символов в нижнем регистре')
            if sum(1 for char in password if not char.isalnum()) < min_special_chars:
                raise ValueError(f'Пароль должен содержать не менее {min_special_chars} спец-символов')
            return func(username, password)

        return wrapper

    return decorator


# Оборачиваем функцию декораторами
@username_validator
@password_validator()
def register_user(username: str, password: str) -> None:
    with open('users.csv', 'a', encoding='windows-1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([username, password])


# Тестируем
register_user('юзер1', 'pas"Афываsword')
