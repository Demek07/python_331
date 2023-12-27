"""
Тотальный разбор hw_19.py
Понятине сериализации и десериализации данных
pickle
json
yaml формат
pyYAML - yaml
pip install pyyaml
"""
from pprint import pprint

"""
Что такое YAML?
YAML - это формат сериализации данных, 
который может быть использован для представления данных в виде структуры данных Python.

Используется в:
- Docker
- GitActions
- Obsidian
- Много-много где еще :)

Методы:
- dump - для работы с файлами
- dumps - для работы со строками
- load - для работы с файлами
- loads - для работы со строками
"""



# Возьмем json строку из файла с городами и запишем ее в yaml файл

json_string = """[
    {
        "coords": {
            "lat": 52.65,
            "lon": 90.08333
        },
        "district": "Сибирский",
        "name": "Абаза",
        "population": 14816,
        "subject": "Хакасия"
    },
    {
        "coords": {
            "lat": 53.71667,
            "lon": 91.41667
        },
        "district": "Сибирский",
        "name": "Абакан",
        "population": 187239,
        "subject": "Хакасия"
    }
]"""

# Десериализуем json строку в python объект
import json

cities = json.loads(json_string)

# Посмотрим что получилось
print(type(cities))
pprint(cities)

# Сериализуем python объект в yaml строку
import yaml


yaml_string = yaml.dump(cities, allow_unicode=True)
print(type(yaml_string))
print(yaml_string)

# Сериализуем python объект в yaml файл
with open('cities.yaml', 'w') as yaml_file:
    # allow_unicode=True - для того, чтобы можно было писать кириллицей
    # encoding='utf-8' - для того, чтобы можно было писать кириллицей
    yaml.dump(cities, yaml_file, encoding='utf-8-sig', allow_unicode=True, indent=8)

# Десериализуем yaml строку в python объект из файла
with open('cities.yaml', 'r') as yaml_file:
    cities_from_yaml = yaml.load(yaml_file, Loader=yaml.Loader)


# Посмотрим что получилось
print(type(cities_from_yaml))
pprint(cities_from_yaml)