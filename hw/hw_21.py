"""
Решение домашнего задания №21

Функция get_weather(city_name) принимает название города и возвращает данные о погоде в этом городе.



"""
from dataclasses import dataclass
from pprint import pprint
from marshmallow import Schema, fields, post_load, INCLUDE, validate
from marshmallow_jsonschema import JSONSchema
import requests


def get_weather(city_name: str) -> dict:
    """
    Функция принимает название города и возвращает данные о погоде в этом городе.
    :param city_name: Название города
    :return: Данные о погоде в этом городе
    """
    api_key = "23496c2a58b99648af590ee8a29c5348"  # Можете взять мой. 23496c2a58b99648af590ee8a29c5348
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'lang': 'ru',
        'units': 'metric',
        'appid': api_key
    }
    response = requests.get(base_url, params=params)
    return response.json()


# Формируем Датакласс
@dataclass
class CurrentWeather:
    city_name: str
    weather_icon: str
    description: str
    temperature: float
    feels_like: float
    wind_speed: float

    def __str__(self):
        return f"Погода в городе {self.city_name}:\n" \
               f"Температура: {self.temperature}°C\n" \
               f"Ощущается как: {self.feels_like}°C\n" \
               f"Скорость ветра: {self.wind_speed} м/с\n" \
               f"Погодные условия: {self.description}"


"""
Marshmallow схема, которая проверяет только те поля,
 которые нам нужны (все остальные игнорируются)
 мы явно указываем местонахождение каждого поля в JSON
 после чего, в @post_load мы указываем создаем экземпляр класса CurrentWeather

мы допускаем что в JSON могут быть поля, которые нам не нужны на всех уровнях вложенности
"""


class CurrentWeatherSchema(Schema):
    city_name = fields.Str(data_key='name')  # data_key - путь к данным в JSON
    weather_icon = fields.Str(data_key='weather.0.icon')
    description = fields.Str(data_key='weather.0.description')
    # Проверяем температуру на диапазон от -70 +70 через range validate=validate.Range(min=18)
    temperature = fields.Float(data_key='main.temp', validate=validate.Range(min=-10, max=70))
    feels_like = fields.Float(data_key='main.feels_like')
    wind_speed = fields.Float(data_key='wind.speed')

    @post_load
    def make_current_weather(self, data, **kwargs):
        return CurrentWeather(
            city_name=data['city_name'],
            weather_icon=data['weather'][0]['icon'],
            description=data['weather'][0]['description'],
            temperature=data['main']['temp'],
            feels_like=data['main']['feels_like'],
            wind_speed=data['wind']['speed']
        )

    class Meta:
        unknown = INCLUDE


def main():
    user_city = input("Введите название города: ")
    weather_data = get_weather(user_city)
    schema = CurrentWeatherSchema()
    current_weather = schema.load(weather_data)
    print(current_weather)

    # Генерация JSON схемы из Marshmallow схемы
    pprint(JSONSchema().dump(schema))


if __name__ == "__main__":
    main()
