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
import dataclasses
from dataclasses import dataclass, field
from pprint import pprint

from data.cities import cities_list
import json

# записываем cities_list в cities.json encoding='utf-8', ensure_ascii=False, indent=4
with open('../data/cities.json', 'r', encoding='utf-8') as cities_file:
    cities_list = json.load(cities_file)

# pprint(cities_list)

# TODO практика!
"""
Можно использовать (order=True) для генерации всех методов сравнения
Можно выключить field(compare=False) для того, чтобы некоторые поля не участвовали в сравнении

Создайте датакласс City со следующими полями:
- name - название города
- population - население
- subject - субъект РФ
- district - федеральный округ
- latitude - широта
- longitude - долгота
- is_used = False - использован ли город в игре или нет
"""


@dataclass
class City:
    name: str
    population: int
    subject: str
    district: str
    latitude: float = field(metadata={'data_key': 'coords.lat'})
    longitude: float = field(metadata={'data_key': 'coords.lon'})
    is_used: bool = False

    def __post_init__(self):
        self.name = self.name.capitalize()
        self.subject = self.subject.capitalize()
        self.district = self.district.capitalize()

    def __str__(self):
        """
        Метод для приведения объекта к строке. Вызывается функцией str()
        Так же мы видим его работу когда выводим объект в консоль через print()
        :return:
        """
        return f"Город: {self.name}, Население: {self.population}"

    def __bool__(self):
        """
        Проверка, был ли использован ли этот город в игре или нет
        :return: True если город использован, False если нет
        """
        return self.is_used

    def __repr__(self):
        """
        Метод для отладки. Он вызывается, когда мы выводим объект в консоль
        Может быть использован для воссоздания объекта из консоли.
        :return:
        """
        return f"City(name='{self.name}', population={self.population}, subject='{self.subject}', " \
               f"district='{self.district}', latitude={self.latitude}, longitude={self.longitude}, " \
               f"is_used={self.is_used})"

    def __eq__(self, other):
        """
        Сравнение на равенство будет происходить и по названию и по населению
        В этом случае, ломается логика остальных проверок, сделанных автоматически
        Т.е. тогда надо их прописать вручную
        """
        return (self.name == other.name
                and self.latitude == other.latitude)

    def __lt__(self, other):
        return self.population < other.population


# Получаем список дата классов
def deserialize_city(data):
    city_data = {field.name: (data.get(field.metadata.get('data_key', field.name), field.default)
                              if field.default is not dataclasses.MISSING else data.get(field.metadata.get('data_key', field.name), None))
                 for field in City.__dataclass_fields__.values()}
    return City(**city_data)


# Десериализация списка городов
cities = [deserialize_city(city_data) for city_data in cities_list]
pprint(cities)
