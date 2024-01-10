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


class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Email()

user_data = {
    'id': 1,
    'name': 'Иван',
    'email': 'ivan@example.com',
}

user_schema = UserSchema()
result = user_schema.dump(user_data)
print(result)