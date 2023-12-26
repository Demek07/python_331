"""
Тотальный разбор hw_19.py
Понятине сериализации и десериализации данных
pickle
"""
from dataclasses import dataclass
import pickle
"""
Сериализация - преобразование данных в строку (например, в json)
"снимаем сериал" - упрощаем

Десериализация - преобразование данных из строки в объект (например, из json в словарь)
"""

# pickle - библиотека для сериализации и десериализации данных в бинарном формате
"""
Плюсы pickle:
- Простота использования
- Поддержка всех типов данных
- Поддержка пользовательских классов

Минусы pickle:
- Небезопасен
- Не поддерживает многопоточность

"""

@dataclass
class City:
    name: str
    population: int
    subject: str
    district: str
    latitude: float
    longitude: float
    is_used: bool = False

    def __str__(self):
        return f'Город {self.name}. Население: {self.population}. Использование в игре: {self.is_used}'


# Создаем экземпляр класса City
city = City(name='Москва', population=10000000,
            subject='Москва', district='Центр',
            latitude=55.7558, longitude=37.6173, is_used=True)

# Печатаем экземпляр класса City до сериализации
print(f'City до сериализации: {city}')

# Сериализация в бинарный формат и запись в файл
with open('city.pickle', 'wb') as f:
    pickle.dump(city, f)

# Десериализация из бинарного формата
with open('city.pickle', 'rb') as f:
    city_from_pickle = pickle.load(f)


# Печатаем экземпляр класса City после десериализации
print(f'City после десериализации: {city_from_pickle}')