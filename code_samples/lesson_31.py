"""
Lesson 31
Класс сериализации и класс валидации
сериализация - преобразование объекта в строку
де-сериализация - преобразование строки в объект
валидация - проверка данных на корректность
json schema - формат для описания json данных
pip install jsonschema
"""
from dataclasses import dataclass
from pprint import pprint
from typing import List

from jsonschema import validate, ValidationError
from jsonschema._format import FormatChecker

# data = [1, 2, None]
#
# schema = {
#     "type": "array",
#     "items": {
#         "type": "integer"
#     }
# }

data = {
    "name": "John",
    "last_name": "Iva",
    "age": 30,
    "email": "vasa_ivanov@mail.ru",  # 1@ пройдет все проверки (кроме регулярки)
    "is_active": True,
    "web-site": "https://vasa-ivanov.ru"
}

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string",
                 "minLength": 3,
                 "maxLength": 10
                 },
        "age": {"type": "integer",
                "minimum": 18,
                "maximum": 100
                },
        # last_name - ссылка на name
        "last_name": {"$ref": "#/properties/name"},
        "email": {
            "type": "string",
            "format": "email",
            "pattern": r"""^(?=.{1,254}$)(?=.{1,64}@)[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}|(\[(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))(\.(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])){2}\.[0-9]{1,3}\]))$"""
        },
        "is_active": {"type": "boolean"},

        "web-site": {"type": "string",
                     "format": "uri",
                     "pattern": r"""^(https?:\/\/)?(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}$"""
                     }
    },
    "required": ["name", "age", "email", "is_active"],
}

try:
    validate(instance=data, schema=schema, format_checker=FormatChecker())
    # format_checker=FormatChecker() - для запускает "улучшенную" валидацию, которая не особо решает проблему
except ValidationError as e:
    print(e)
