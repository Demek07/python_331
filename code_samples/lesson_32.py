"""
Lesson 32
10.01.2024

- Тотальный разбор HW_20
- Знакомство с Marshmallow
- pip install marshmallow marshmallow-dataclass

"""
from dataclasses import dataclass

from marshmallow import Schema, fields, validate, ValidationError


# Schema - описание того, как должны выглядеть данные (структура данных - поля, типы полей, обязательные поля и т.д.)
# fields - описание того, как должны выглядеть поля в данных (типы, валидация, дефолтные значения и т.д.)
# validate - валидация данных
# ValidationError - исключение, которое выбрасывается при ошибке валидации

@dataclass
class Person:
    name: str
    age: int
    email: str
    is_married: bool


class PersonSchema(Schema):
    name = fields.Str()
    age = fields.Int()
    email = fields.Email()
    is_married = fields.Bool()


persons_list = [
    {
        "name": "John",
        "age": 30,
        "email": "vm@mail.ru",
        "is_married": True
    },
    {
        "name": "Kate",
        "age": '30',
        "email": "123@s.ru",
        "is_married": "True"
    }
]

# Поштучная валидация
# person_schema = PersonSchema()
#
# for person in persons_list:
#     try:
#         person_schema.load(person)
#     except ValidationError as e:
#         print(e.messages)

# Валидация списка
persons_schema = PersonSchema(many=True)

try:
    persons_schema.load(persons_list)
except ValidationError as e:
    print(e.messages)

# Методы dump и load
"""
dump - Сериализует объекты Python в простые типы данных Python, которые затем могут быть легко сериализованы
 в любой JSON-подобный формат.
 
load - Десериализует объекты Python из строки, содержащей данные JSON.

Dumps и loads - напрямую для работы со строками
"""

person_1 = Person(name=243, age=30, email="123@mail.ru", is_married=True)
# TODO: Где исключения, Либовски?


# dump и dumps
person_schema = PersonSchema()

person_1_dumped = person_schema.dump(person_1)
person_1_dumped_str = person_schema.dumps(person_1)
print(f"{person_1_dumped=}")
print(f"{type(person_1_dumped)=}")
print(f"{person_1_dumped_str=}")
print(f"{type(person_1_dumped_str)=}")

person_str = '{"name": "243", "age": 30, "email": "123@mail.ru", "is_married": true}'
person_dict = {'name': 30, 'age': 30, 'email': '123@mail.ru', 'is_married': True}

# load и loads

person_1_loaded = person_schema.load(person_dict)
person_1_loaded_str = person_schema.loads(person_str)
print(f"{person_1_loaded=}")
print(f"{type(person_1_loaded)=}")
print(f"{person_1_loaded_str=}")
print(f"{type(person_1_loaded_str)=}")

