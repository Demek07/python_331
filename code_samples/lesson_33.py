"""
Marshmallow - библиотека для сериализации и валидации данных
marshmallow-dataclass - расширение для Marshmallow, которое позволяет автоматически генерировать схемы на основе dataclass
marshmallow_jsonschema - расширение для Marshmallow, которое позволяет генерировать json schema на основе схемы Marshmallow

Установка
- pip install marshmallow marshmallow-dataclass marshmallow_jsonschema  - то, что нам сегодня понадобится

- Понятие schema - схема данных
- Понятие field - поле в схеме данных
- Понятие validation - валидация данных
- Основные методы Marshmallow:
    - dump - на выходе получаем строку (из объекта в строку)
    - dumps - для работы со строками (из объекта в строку)
    - load - для работы с файлами (из файла в объект)
    - loads - для работы со строками (из строки в объект)

- Field types:
    - string - строка
    - integer - целое число
    - float - число с плавающей точкой
    - boolean - булево значение
    - list - список
    - dict - словарь
    - datetime - дата и время
    - url - ссылка
    - email - email
    - uuid - уникальный идентификационный номер
    - nested - вложенная схема
    - function - функция
    - date - дата
    - time - время

Field options:
    - required - обязательное поле
    - default - дефолтное значение поля - если в данных нет такого поля, то оно будет заполнено дефолтным значением
    - allow_none - разрешить None в качестве значения поля
    - load_only - поле будет использоваться только при загрузке данных
    - dump_only - поле будет использоваться только при выгрузке данных
    - validate - валидация данных
    - missing - значение по умолчанию, если в данных нет такого поля
    - error_messages - сообщения об ошибках валидации
    - metadata - метаданные

- Возможный вариант проверки номеров телефонов - phonenumbers

- Nested schema - вложенная схема
- validate - валидация данных
    - Length - проверка длины
    - Range - проверка диапазона
    - OneOf - проверка на вхождение в список
    - Regexp - проверка регулярным выражением
    - Equal - проверка на равенство
    - Email - проверка email
    - URL - проверка ссылки

@post_load - декоратор, который позволяет обрабатывать данные после валидации
@pre_load - декоратор, который позволяет обрабатывать данные до валидации

Создание экземпляра дата класса после успешной валидации данных, используя @post_load

Создание базовой схемы на основе dataclass
Расширение базовой схемы через наследование
Генерация json schema на основе схемы marshmallow
"""
from pprint import pprint
from typing import Dict, Any

from marshmallow import Schema, fields, ValidationError

# Nested schema - вложенная схема

full_dict = {
    0: {
        'title': 'Железный человек',
        'year': 2008,
        'director': 'Джон Фавро',
        'screenwriter': 'Марк Фергус и Хоук Остби, Артур Маркам и Мэтт Холлоуэй',
        'producer': 'Ави Арад и Кевин Файги',
        'stage': 'Первая фаза'
    },

    'Номер 1': {
        'title': 'Железный человек',
        'year': 2008,
        'director': 'Джон Фавро',
        'screenwriter': 'Марк Фергус и Хоук Остби, Артур Маркам и Мэтт Холлоуэй',
        'producer': 'Ави Арад и Кевин Файги',
        'stage': 'Первая фаза'
    }
}


class FilmSchema(Schema):
    title = fields.Str(required=True)
    year = fields.Int(required=True,
                      validate=lambda x: 1900 < int(x) < 2022)

    director = fields.Str(required=True)
    screenwriter = fields.Str(required=True)
    producer = fields.Str(required=True)
    stage = fields.Str(required=True)


"""
Проверяем ключи в словаре, и вложенной схемой их значения
"""


class FullSchema(Schema):
    films = fields.Dict(keys=fields.Int(),
                        values=fields.Nested(FilmSchema))


# Создаем экземпляр схемы
full_schema = FullSchema()
"""
Когда я предложил использовать {'films': full_dict} в коде, это был способ адаптации ваших данных 
к ожидаемой структуре FullSchema. В FullSchema, мы определили,
 что есть поле films, которое является словарем с фильмами. 
 
 Чтобы данные соответствовали этой структуре, мы обернули ваш исходный 
 словарь full_dict в другой словарь с ключом films.
"""
try:
    validated_data = full_schema.load({'films': full_dict})
    pprint(validated_data)
except ValidationError as e:
    pprint(e.messages)

