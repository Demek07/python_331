"""
Lesson 35
18.01.2024

- Паттерны проектирования (Структурные паттерны)
- Adapter
"""

"""
У нас есть приложение для прогноза погоды, которое изначально разработано для использования 
с API погодного сервиса A. 

Теперь мы хотим интегрировать API погодного сервиса B, но его интерфейс отличается от API сервиса A.
"""


# Исходный сервис (например, старый API)
class WeatherServiceA:
    def get_temperature(self):
        # Возвращаем температуру от сервиса A
        return "20°C"


# Новый сервис с другим интерфейсом
class WeatherServiceB:
    def fetch_weather_info(self):
        # Возвращаем словарь с информацией о погоде
        return {"temperature": "18°C", "humidity": "80%"}


# Целевой интерфейс для нашего приложения
class WeatherServiceInterface:
    def get_temperature(self):
        raise NotImplementedError # raise NotImplementedError - это специальный метод, который говорит, что метод не реализован


# Адаптер, преобразующий WeatherServiceB к WeatherServiceInterface
class WeatherAdapter(WeatherServiceInterface):
    def __init__(self, service_b):
        self.service_b = service_b

    def get_temperature(self):
        # Извлекаем температуру из информации, предоставляемой сервисом B
        weather_info = self.service_b.fetch_weather_info()
        return weather_info["temperature"]


# Использование адаптера в приложении
service_a = WeatherServiceA()
print(f"Температура от сервиса A: {service_a.get_temperature()}")

service_b = WeatherServiceB()
adapter_b = WeatherAdapter(service_b)
print(f"Температура от сервиса B через адаптер: {adapter_b.get_temperature()}")
