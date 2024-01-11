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
"""
import json
from dataclasses import dataclass
from pprint import pprint
from typing import Dict, Any

from marshmallow import Schema, fields, ValidationError, validate, post_load
from marshmallow_dataclass import class_schema
from marshmallow_jsonschema import JSONSchema

json_string = """[
    {
        "coords": {
            "lat": "52.65",
            "lon": "90.08333"
        },
        "district": "Сибирский",
        "name": "Абаза",
        "population": 14816,
        "subject": "Хакасия"
    },
    {
        "coords": {
            "lat": "53.71667",
            "lon": "91.41667"
        },
        "district": "Сибирский",
        "name": "Абакан",
        "population": -187239,
        "subject": "Хакасия"
    }
]"""


# Создадим dataclass для хранения данных о городах
@dataclass
class City:
    name: str
    subject: str
    district: str
    population: int
    coords: Dict[str, Any]


# Создаем схему marshmallow для валидации данных используя marshmallow-dataclass
CitySchema = class_schema(City)


# Расширяем базовую схему marshmallow для валидации данных через наследование
# Добавляем валидацию минимального значения для поля population

class DetailedCitySchema(CitySchema):
    population = fields.Integer(validate=validate.Range(min=0))


# Валидируем данные пачкой
valid_cities: list[City] = []
try:
    cities = DetailedCitySchema(many=True).loads(json_string)
except ValidationError as e:
    print(e.messages)


# Валидируем данные поштучно (но для этого придется превратить строку в список словарей)
# valid_cities: list[City] = []
#
# # Экземпляр схемы для валидации данных
# city_schema = DetailedCitySchema()
#
# # Валидация поштучно
# for city in json.loads(json_string):
#     try:
#         valid_city = city_schema.load(city)
#         valid_cities.append(valid_city)
#     except ValidationError as e:
#         print(e.messages)

# Генерируем json schema на основе схемы marshmallow CitySchema
# Тут было необходимо добавить () в DetailedCitySchema(), чтобы получить экземпляр класса
json_schema = JSONSchema().dump(DetailedCitySchema())
pprint(json_schema)
