"""
Lesson 35
18.01.2024

- Паттерны проектирования (Структурные паттерны)
- Adapter (адаптер)
- Facade (фасад)
- Composite (композит)
- Proxy (заместитель)
"""

"""
#### Цели и Задачи
Паттерн "Прокси" в программировании предназначен для предоставления заместителя или плейсхолдера для другого объекта,
 чтобы контролировать доступ к нему. Основные задачи паттерна:

- **Управление доступом**: Прокси может контролировать доступ к объекту, например, если объект требует защиты из-за 
высоких ресурсных требований или по причинам безопасности.
- **Отложенная инициализация (ленивая загрузка)**: Прокси может отложить создание объекта до тех пор, пока он 
действительно не будет нужен, тем самым улучшая производительность.
- **Логирование и аудит**: Прокси может записывать операции, выполняемые на объекте, для целей аудита или логирования.
- **Контроль за ресурсами**: Прокси может управлять ресурсами, связанными с объектом, например, закрывать соединения
 с базой данных или освобождать память.

#### Структура
Паттерн прокси включает в себя следующие компоненты:

1. **Субъект (Subject)**: Общий интерфейс для реального объекта и прокси. Это позволяет использовать прокси вместо
 реального объекта.
2. **Реальный Объект (Real Object)**: Объект, для которого создается прокси. Это может быть объект, работа с которым 
связана с большими ресурсными затратами или требует защиты.
3. **Прокси (Proxy)**: Объект, который управляет доступом к реальному объекту. Он содержит ссылку на реальный объект
 и может управлять его созданием и удалением, а также предварительно обрабатывать или кэшировать запросы к нему.

"""


# Пример 1
class Image:
    def __init__(self, url):
        self.url = url
        self.image_data = None

    def load_image(self):
        self.image_data = f"Изображение загружено с {self.url}"
        return self.image_data


class ImageProxy:
    def __init__(self, url):
        self.url = url
        self._image = None

    def load_image(self):
        if not self._image:
            self._image = Image(self.url)
            return self._image.load_image()
        return "Изображение уже загружено"


# Клиентский код
proxy_image = ImageProxy("http://example.com/image.png")
print(proxy_image.load_image())  # Загружает изображение
print(proxy_image.load_image())  # Изображение уже загружено


# Пример 2

# Интерфейс для реального объекта и прокси
class DataInterface:
    def get_data(self):
        raise NotImplementedError


# Реальный объект, содержащий конфиденциальную информацию
class SensitiveData(DataInterface):
    def get_data(self):
        return "Конфиденциальные данные"


# Прокси, контролирующий доступ к реальному объекту
class DataProxy(DataInterface):
    def __init__(self, data):
        self.data = data
        self.is_authenticated = False

    def authenticate(self, password):
        if password == "секрет":
            self.is_authenticated = True

    def get_data(self):
        if self.is_authenticated:
            return self.data.get_data()
        return "Доступ запрещен"


# Клиентский код
real_data = SensitiveData()
proxy_data = DataProxy(real_data)

print(proxy_data.get_data())  # Доступ запрещен

proxy_data.authenticate("секрет")
print(proxy_data.get_data())  # Конфиденциальные данные
