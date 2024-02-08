"""
Тесты для проверки работы функции get_weather и погодного апи
Для запуска всего кроме медленного теста используйте команду pytest -m "not slow"
"""
from pprint import pprint

import pytest
import requests


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


cities = [
    ('Москва', {"lon": 37.6156, "lat": 55.7522}),
    ('Воронеж', {"lon": 39.17, "lat": 51.6664}),
    ('Санкт-Петербург', {"lon": 30.2642, "lat": 59.8944}),
    ('Краснодар', {"lon": 38.9769, "lat": 45.0328}),
    ('Сочи', {"lon": 39.7303, "lat": 43.6}),
]


@pytest.fixture(scope='module')
def weather_request():
    """Фикстура для создания экземпляра WeatherRequest"""
    return get_weather('Москва')


def test_weather_request_city_name(weather_request):
    """Проверка названия города в ответе API"""
    assert weather_request['name'] == 'Москва'


def test_weather_request_coord(weather_request):
    """Проверка координат в ответе API"""
    assert weather_request['coord'] == {"lon": 37.6156, "lat": 55.7522}


def test_weather_request_weather_key(weather_request):
    """Проверка наличия ключей в секции weather"""
    assert all(key in weather_request['weather'][0] for key in ['id', 'main', 'description', 'icon'])


def test_weather_request_main_key(weather_request):
    """Проверка наличия ключей в секции main"""
    assert all(key in weather_request['main'] for key in
               ['feels_like', 'temp', 'temp_min', 'temp_max', 'pressure', 'humidity'])


@pytest.mark.slow
@pytest.mark.parametrize("city_name, expected_coords", cities)
def test_weather_request_city_coodrd_name_parametrize_slow(city_name, expected_coords):
    """Проверка названия города и координат в ответе API"""
    response = get_weather(city_name)
    assert response['coord'] == expected_coords
