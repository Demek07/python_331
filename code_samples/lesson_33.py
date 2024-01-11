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

full_dict = [
    {
        'title': 'Железный человек',
        'year': 2008,
        'director': 'Джон Фавро',
        'screenwriter': {'names': ['Марк Фергус', 'Хоук Остби', 'Артур Маркам', 'Мэтт Холлоуэй'],
                         'count': 4},
        'producer': {'names': ['Ави Арад', 'Кевин Файги'],
                     'count': 2},
        'stage': 'Первая фаза'
    },

    {
        'title': 'Железный человек',
        'year': 2008,
        'director': 'Джон Фавро',
        'screenwriter': {'names': ['Марк Фергус', 'Хоук Остби', 'Артур Маркам', 'Мэтт Холлоуэй'],
                         'count': 4
                         },
        'producer': {'names': ['Ави Арад', 'Кевин Файги'],
                     'count': 2
                     },
        'stage': 'Первая фаза'
    }
]

from marshmallow import Schema, fields, ValidationError
from pprint import pprint


# Измененная схема NamesListSchema
class NamesListSchema(Schema):
    # Эта схема непосредственно обрабатывает список строк
    names = fields.List(fields.String(), required=True)
    # Добавляем новое поле count
    count = fields.Integer(required=True)


# Измененная схема MovieSchema
class MovieSchema(Schema):
    title = fields.String(required=True)
    year = fields.Integer(required=True)
    director = fields.String(required=True)
    screenwriter = fields.Nested(NamesListSchema, required=True)
    producer = fields.Nested(NamesListSchema, required=True)
    stage = fields.String(required=True)


# Создаем экземпляр схемы MovieSchema для обработки списка фильмов
movies_schema = MovieSchema(many=True)

# Пытаемся валидировать данные
try:
    validated_data = movies_schema.load(full_dict)
    pprint(validated_data)
except ValidationError as e:
    pprint(e.messages)
