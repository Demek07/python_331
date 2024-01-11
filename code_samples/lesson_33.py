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


- Возможный вариант проверки номеров телефонов - phonenumbers
"""
from marshmallow import Schema, fields, ValidationError

"""
Создадим список словарей с данными о людях и попробуем валидировать их с помощью Marshmallow
На выходе у нас будет список словарей с данными о людях, но уже валидированный с помощью Marshmallow

Используемый метод:
?
"""
people_data = [
    {'name': 'Alexander',
     'surname': 'Clark',
     'email': 'dellis@e.com',
     'phone_number': '354-462-9819x59090',
     'address': '187 Justin Skyway\nPort Wesleyberg, NC 78817',
     'hobby': 'gaming',
     'work_place': 'Watson-Boyer'},

    {'name': 'Kathy',
     'surname': 'Boyd',
     'email': 'pcolon@example.net',
     'phone_number': '8192903898',
     'address': '8689 Harper Walks\nNorth Danamouth, CT 14062',
     'hobby': 'sports',
     'work_place': 'Curtis, Alvarez and Watkins'},

    {'name': 'Darren',
     'surname': 'Sanchez',
     'email': 'omontgomery@example.net',
     'phone_number': '928-214-2541x5276',
     'address': '22233 Mejia Junctions\nLake Katherine, GU 35948',
     'hobby': 'gaming',
     'work_place': 'Dawson Group'},
]


# Создадим схему для валидации данных об одном человеке (PersonSchema)

class PersonSchema(Schema):
    name = fields.Str()
    surname = fields.Str()
    email = fields.Email()
    phone_number = fields.Str()
    address = fields.Str()
    hobby = fields.Str()
    work_place = fields.Str()


# Создадим экземпляр схемы
person_schema = PersonSchema()

# Список валидных данных
valid_people_data = []

# Валидация данных об одном человеке в цикле
for person in people_data:
    try:
        person_schema.load(person)
    except ValidationError as e:
        print(e.messages)
        print('---')
    else:
        valid_people_data.append(person)
        print('.', end='')
