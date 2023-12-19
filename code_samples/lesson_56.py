"""
Lesson 56 - Dataclasses
19.12.2023

- Определение датакласса
- Разница между обычным классом и датаклассом
- Атрибуты по умолчанию
- Параметры декоратора dataclass
    - order=True - генерация дандер методов сравнения (по умолчанию генерируется только __eq__)
    - init=True - генерация метода __init__ (по умолчанию True - но в некоторых случаях может быть полезно отключить)
    - frozen=True - неизменяемый датакласс (по умолчанию False)

- field - параметры для атрибутов
-Параметры field:
    - compare - участвует ли атрибут в сравнении
    - default - значение по умолчанию
    - repr - участвует ли атрибут в repr
    - metadata - словарь с метаданными
    - __dataclass_fields__['category'].metadata - метаданные конкретного атрибута

__post_init__ - метод, который вызывается после инициализации объекта
abstract @dataclass и __post_init__
"""

from dataclasses import dataclass
from pprint import pprint

from data.cities import cities_list
import json

# записываем cities_list в cities.json encoding='utf-8', ensure_ascii=False, indent=4
with open('../data/cities.json', 'r', encoding='utf-8') as cities_file:
    cities_list = json.load(cities_file)

pprint(cities_list)

# TODO практика!
"""
Создайте датакласс City со следующими полями:
- name - название города
- population - население
- subject - субъект РФ
- district - федеральный округ
- latitude - широта
- longitude - долгота
- is_used = False - использован ли город в игре или нет
"""