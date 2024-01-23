"""
Lesson 35
18.01.2024

- Паттерны проектирования (Структурные паттерны)
- Adapter (адаптер)
- Facade (фасад)
- Composite (композит)
- Proxy (заместитель)
- Практический пример использования паттернов Фасад + Прокси + marshmallow в  погодном приложении
"""
import time

"""
Реализация погодного приложения. 
Классы:
- CurrentWeatherRequest - класс, который делает запрос к API погоды и возвращает текущую погоду в виде словаря
- CurrentWeatherRequestProxy - класс, который хеширует запросы к API, и если запрос был выполнен в течении последних 
10 минут, то возвращает сохраненный результат, а не делает новый запрос к API
- CurrentWeatherFacade - класс, который оборачивает логику работы с API погоды и предоставляет простой интерфейс для
- получения погоды
- CurrentWeather - класс, который хранит в себе данные о погодe (датакласс)
"""

from dataclasses import dataclass
from pprint import pprint
from marshmallow import Schema, fields, post_load, INCLUDE, validate
from marshmallow_jsonschema import JSONSchema
import requests

API_KEY = "23496c2a58b99648af590ee8a29c5348"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
TIME_FORMAT = "%d.%m.%Y %H:%M:%S"
TIME_TRESHOLD = 30  #  30 секунд

# Формируем Датакласс
@dataclass
class CurrentWeather:
    city_name: str
    weather_icon: str
    description: str
    temperature: float
    feels_like: float
    wind_speed: float
    request_time = None

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


class CurrentWeatherRequest:
    """
    Класс для запроса погоды через API
    """

    def __init__(self, api_key: str = API_KEY, base_url: str = BASE_URL):
        self.schema = CurrentWeatherSchema()
        self.api_key = api_key
        self.base_url = base_url
        self.params = {
            'q': None,
            'lang': 'ru',
            'units': 'metric',
            'appid': api_key
        }

    def __call__(self, city_name: str) -> "CurrentWeather":
        """
        Метод для получения данных о погоде.
        Возвращает валидированный экземпляр класса CurrentWeather
        :param city_name: Название города
        :return: Данные о погоде
        """
        self.params['q'] = city_name
        response = requests.get(self.base_url, params=self.params)
        if response.status_code == 200:
            data = response.json()
            return self.schema.load(data)
        else:
            raise Exception(f"Ошибка при запросе к API: {response.status_code}")


class CurrentWeatherRequestProxy(CurrentWeatherRequest):
    """
    Класс для запроса погоды через API с использованием кэширования
    Запросы кешируются в списке cache который хранит экземпляры
    """

    def __init__(self, api_key: str = API_KEY, base_url: str = BASE_URL):
        super().__init__(api_key, base_url)
        self.cache = []

    def __call__(self, city_name: str) -> "CurrentWeather":
        """
        Метод для получения данных о погоде.
        Возвращает валидированный экземпляр класса CurrentWeather
        :param city_name: Название города
        :return: Данные о погоде
        """
        for item in self.cache:
            if item.city_name == city_name:
                if time.time() - item.request_time < TIME_TRESHOLD:
                    print(f"Данные о погоде в городе {city_name} получены из кэша\n"
                          f"Время запроса: {time.strftime(TIME_FORMAT, time.localtime(item.request_time))}")
                    return item
        weather = super().__call__(city_name)
        weather.request_time = time.time()
        self.cache.append(weather)
        print(f"Данные о погоде в городе {city_name} получены из API")
        return weather


class CurrentWeatherFacade:
    """
    Класс для получения данных о погоде в городе
    """

    def __init__(self, api_key: str = API_KEY, base_url: str = BASE_URL):
        self.api_key = api_key
        self.base_url = base_url
        self.request = CurrentWeatherRequestProxy(api_key, base_url)

    def get_weather(self, city_name: str) -> "CurrentWeather":
        """
        Метод для получения данных о погоде.
        Возвращает валидированный экземпляр класса CurrentWeather
        :param city_name: Название города
        :return: Данные о погоде
        """
        return self.request(city_name)


if __name__ == '__main__':
    weather_facade = CurrentWeatherFacade()
    while True:
        city = input("Введите название города: ")
        weather = weather_facade.get_weather(city)
        print(weather)

