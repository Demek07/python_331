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
"""
from pprint import pprint
from typing import Dict, Any

from marshmallow import Schema, fields, ValidationError, validate

# Nested schema - вложенная схема


full_dict = [
    {
        'title': 'Железный человек',
        'year': 2008,
        'director': 'Джон Фавро',
        'screenwriter': ['Марк Фергус', 'Хоук Остби', 'Артур Маркам', 'Мэтт Холлоуэй'],
        'producer': ['Ави Арад', 'Кевин Файги'],
        'stage': 'Первая фаза'
    },

    {
        'title': 'Железный человек',
        'year': 2023,
        'director': 'Джон Фавро',
        'screenwriter': ['Марк Фергус', 'Хоук Остби', 'Артур Маркам', 'Мэтт Холлоуэй'],
        'producer': ['Ави Арад', 'Кевин Файги'],
        'stage': 'Первая фаза'
    }
]


class MovieSchema(Schema):
    title = fields.Str()
    year = fields.Int(validate=validate.Range(1900, 2099))
    director = fields.Str()
    screenwriter = fields.List(fields.Str())
    producer = fields.List(fields.Str())
    stage = fields.Str()

# Валидация данных
# Создание схемы
movie_schema = MovieSchema(many=True)

# Валидация данных
try:
    movie_schema.load(full_dict)
except ValidationError as e:
    print(e.messages)