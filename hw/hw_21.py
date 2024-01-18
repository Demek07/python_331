"""
Решение домашнего задания №21 №2
С использованием Marshmallow и вложенных схем

Функция get_weather(city_name) принимает название города и возвращает данные о погоде в этом городе.



"""
from pprint import pprint

import requests
from dataclasses import dataclass
from marshmallow import Schema, fields, ValidationError, post_load, INCLUDE
from marshmallow_jsonschema import JSONSchema


def get_weather(city_name: str) -> dict:
    """Получение данных о погоде по названию города"""
    api_key = "0758d753c26b07efcd064735ac96b206"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'lang': 'ru',
        'units': 'metric',
        'appid': api_key
    }
    response = requests.get(base_url, params=params)
    return response.json()


@dataclass
class CurrentWeather:
    """
    Класс для хранения данных о погоде в конкретном городе
    """
    city_name: str
    description: str
    temp: float
    humidity: float
    wind_speed: float
    pressure: int
    feels_like: float

    def __str__(self) -> str:
        """
        Вывод информации о погоде в читаемом виде
        :return: str
        """
        return f'Погода в городе {self.city_name}:\n' \
               f'Температура: {self.temp} °C\n' \
               f'Ощущается как: {self.feels_like} °C\n' \
               f'Влажность: {self.humidity} %\n' \
               f'Скорость ветра: {self.wind_speed} м/с\n' \
               f'Давление: {self.pressure} мм.рт.ст.\n' \
               f'Описание: {self.description}'


class MainSchema(Schema):
    """
    Схема для валидации данных о погоде, относящихся к основной информации (ключ main в ответе API)
    """
    temp = fields.Float(required=True)
    pressure = fields.Int(required=True)
    humidity = fields.Int(required=True)
    feels_like = fields.Float(required=True)

    class Meta:
        """
        Параметр unknown указывает, что в ответе API могут быть и другие поля, которые не указаны в схеме.
        """
        unknown = INCLUDE


class WeatherSchema(Schema):
    """
    Схема для валидации данных о погоде, относящихся к погодным условиям (ключ weather в ответе API)
    """
    description = fields.String(required=True)

    class Meta:
        """
        Параметр unknown указывает, что в ответе API могут быть и другие поля, которые не указаны в схеме.
        """
        unknown = INCLUDE


class WindSchema(Schema):
    """
    Схема для валидации данных о погоде, относящихся к ветру (ключ wind в ответе API)
    """
    speed = fields.Float(required=True)
    deg = fields.Int()  # не всегда может быть доступен

    class Meta:
        """
        Параметр unknown указывает, что в ответе API могут быть и другие поля, которые не указаны в схеме.
        """
        unknown = INCLUDE


class CurrentWeatherSchema(Schema):
    """
    Основная схема для валидации данных о погоде. Обрабатывает сам ответ API
    Использует другие схемы для валидации данных о погоде, как вложенные схемы
    """
    name = fields.String(required=True)
    main = fields.Nested(MainSchema, required=True)
    weather = fields.List(fields.Nested(WeatherSchema), required=True)
    wind = fields.Nested(WindSchema, required=True)

    class Meta:
        unknown = INCLUDE  # Разрешаем неизвестные поля

    @post_load  # Декоратор для метода, который будет вызван после валидации данных
    # **kwargs хоть и не используется, но необходим для работы декоратора
    def make_current_weather(self, data, **kwargs) -> CurrentWeather:
        """
        Создание экземпляра класса CurrentWeather из словаря
        Используется после валидации данных
        """
        weather_info = data['weather'][0]  # первый элемент списка погоды
        main_info = data['main']  # основная информация
        wind_info = data['wind']  # информация о ветре

        return CurrentWeather(
            city_name=data['name'],
            description=weather_info['description'],
            temp=main_info['temp'],
            humidity=main_info['humidity'],
            wind_speed=wind_info['speed'],
            pressure=main_info['pressure'],
            feels_like=main_info['feels_like']
        )


def main():
    # Ввод названия города
    city_name = input("Введите город: ")

    # Получение данных о погоде
    weather_data = get_weather(city_name)

    # Создание схемы для валидации данных
    schema = CurrentWeatherSchema()

    # Сохранение JSON схемы на основе c помощью библиотеки marshmallow_jsonschema
    json_schema = JSONSchema().dump(schema)

    # Вывод JSON схемы
    pprint(json_schema)

    try:
        # Десериализация и валидация данных, создание экземпляра CurrentWeather
        # В случае ошибки валидации будет выброшено исключение ValidationError
        # В случае успешной валидации будет создан экземпляр класса CurrentWeather с помощью метода make_current_weather
        current_weather_instance = schema.load(weather_data)

        # Вывод информации о погоде
        print(current_weather_instance)
    except ValidationError as e:
        print(f'Ошибка валидации данных: {e.messages}')


if __name__ == "__main__":
    main()

