# Lesson 12. 19.10.2023
import json
from pprint import pprint

"""
1. Повторение материала
2. JSON - JavaScript Object Notation - описание данных в виде объектов JavaScript
3. Работа с JSON
- Что такое JSON?
- Встроенная библиотека json
- Получаем данные с погодного API
- https://api.openweathermap.org/data/2.5/weather?q=СВОЙГОРОД&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru
- Парсим строку в объекты Python
- Пробуем обратное преобразование
- Записываем в файл с отступами
- Записываем в файл с отключенной кодировкой ASCII
- Читаем из файла

4. Повторение словарей
"""
import csv

data_list = [
    ['Год', 'Фильм', 'Рейтинг'],
    ['2012', 'Marvel\'s The Avengers', '8'],
    ['2023', 'Avengers: Endgame', '8.5'],
    ['2018', 'Black Panther', '7.3'],
    ['2017', 'Thor: Ragnarok', '7.9'],
    ['2016', 'Captain America: Civil War', '7.8'],
    ]

# JSON - JavaScript Object Notation - описание данных в виде объектов JavaScript

# weather_json_string = """
# {"coord":{"lon":82.6103,"lat":49.9789},"weather":[{"id":801,"main":"Clouds","description":"небольшая облачность","icon":"02n"}],"base":"stations","main":{"temp":5.96,"feels_like":5.96,"temp_min":5.96,"temp_max":5.96,"pressure":1026,"humidity":87},"visibility":10000,"wind":{"speed":1,"deg":90},"clouds":{"all":23},"dt":1697730306,"sys":{"type":1,"id":8831,"country":"KZ","sunrise":1697676991,"sunset":1697715146},"timezone":21600,"id":1520316,"name":"Усть-Каменогорск","cod":200}
# """

# Встроенная библиотека json
# import json

# Методы json
# json.loads() - преобразует строку в объекты Python
# json.dumps() - преобразует объекты Python в строку
# json.load() - преобразует файл в объекты Python
# json.dump() - преобразует объекты Python в файл

# Преобразуем строку в объекты Python
# weather_dict = json.loads(weather_json_string)
# print(type(weather_json_string))
# print(type(weather_dict))
# pprint(weather_dict['main']['temp'])

# TODO Практика
"""
1. Берем УРЛ https://api.openweathermap.org/data/2.5/weather?q=СВОЙГОРОД&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru
- %20 - пробел при кодировании URL в кодировке UTF-8
2. Подставляем свой город
3. Идем в браузер и получаем JSON
4. Помещаем полученное в переменную в многострочных кавычках
5. Преобразуем в объекты Python
6. Выводим температуру в консоль
"""

# Импортурием модуль requests
# import requests

# Запрашиваем город у пользователя
# input_city = input('Введите город: ').replace(' ', '%20')

# Формируем URL
# url = (f'https://api.openweathermap.org/data/2.5/weather?q={input_city}'
#        f'&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru')

# Отправляем запрос в API
# response = requests.get(url)

# Преобразуем в объекты Python
# weather_dict = json.loads(response.text)
# print(weather_dict['main']['temp'])

# Преобразуем объекты Python в строку
# weather_json_string = json.dumps(weather_dict, ensure_ascii=False)
# print(type(weather_json_string))
# print(weather_json_string)

# Записываем в файл
# with open('weather.json', 'w', encoding='UTF-8') as file:
#     json.dump(weather_dict, file)


# Записываем в файл
# with open('weather.json', 'w', encoding='UTF-8') as file:
#     # ensure_ascii=False - отключает кодировку в ASCII (киррилица отображается нормально)
#     # indent=4 - отступы в 4 пробела
#     json.dump(weather_dict, file, ensure_ascii=False, indent=4)

# TODO Практика 2
"""
В прошлых сериях))
1. Берем УРЛ https://api.openweathermap.org/data/2.5/weather?q=СВОЙГОРОД&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru
- %20 - пробел при кодировании URL в кодировке UTF-8
2. Подставляем свой город
3. Идем в браузер и получаем JSON
4. Помещаем полученное в переменную в многострочных кавычках
5. Преобразуем в объекты Python
6. Выводим температуру в консоль

Сейчас...
7. Сохраните JSON строку в файл weather.json и откройте её в PyCharm
"""

# Давайте допишем в файл weather.json еще данных
# with open('weather.json', 'a', encoding='UTF-8') as file:
#     file.write('\n')
#     json.dump(weather_dict, file, ensure_ascii=False, indent=4)

# Давайте попробуем это прочитать
# Это успешно сломает файл, потому что мы не можем прочитать несколько JSON объектов в одном файле
# with open('weather.json', 'r', encoding='UTF-8') as file:
#     json_data = json.load(file)


# with open('weather.json', 'r', encoding='UTF-8') as file:
#     weather_dict = json.load(file)
#
# pprint(weather_dict)



# data_list = [
#     ['Год', 'Фильм', 'Рейтинг'],
#     ['2012', 'Marvel\'s The Avengers', '8'],
#     ['2023', 'Avengers: Endgame', '8.5'],
#     ['2018', 'Black Panther', '7.3'],
#     ['2017', 'Thor: Ragnarok', '7.9'],
#     ['2016', 'Captain America: Civil War', '7.8'],
#     ]

# Записываем в JSON файл

# with open('marvel.json', 'w', encoding='UTF-8') as file:
#     json.dump(data_list, file, ensure_ascii=False, indent=4)
#
# # Читаем из JSON файла
# with open('marvel.json', 'r', encoding='UTF-8') as file:
#     marvel_list = json.load(file)
#
# print(type(marvel_list))
# pprint(marvel_list)

# СЛОВАРИ

empty_dict = {}
empty_dict = dict()

person_dict = {
    'name': 'John',
    'age': 30,
    'phone': '+380501234567',
}

# print(person_dict['name'])
# print(person_dict['age'])
# print(person_dict['phone'])
# print(person_dict['hobbies'])  # KeyError
# print(person_dict.get('hobbies'))  # None


# Добавление нового ключа
person_dict['is_married'] = False

# Метод update() - добавляет новые ключи и значения в словарь
person_dict.update(
    {
        'is_married': True,
        'is_student': False
    }
)

# pprint(person_dict, sort_dicts=False)

# Удаление ключа
# del person_dict['is_student']

# Метод pop() - удаляет ключ и возвращает значение
# print(person_dict.pop('is_married'))
# Метод popitem() - удаляет и возвращает пару (ключ, значение)
# print(person_dict.popitem())
#

# pprint(person_dict, sort_dicts=False)

# Метод keys() - возвращает ключи в словаре
# Метод values() - возвращает значения в словаре
# Метод items() - возвращает пары (ключ, значение)

# print(person_dict.keys())
# print(person_dict.values())
# print(person_dict.items())
#
# print(type(person_dict.keys()))
# print(type(person_dict.values()))
# print(type(person_dict.items()))

# Превращаем это в списки
# print(list(person_dict.keys()))
# print(list(person_dict.values()))
# print(list(person_dict.items()))

# Как происходит распаковка кортежа по переменным
# key, value = ('name', 'John')
# print(key, value)

# Цикл for в словарях
# for key, value in person_dict.items():
#     print(f'key: {key}, value: {value}')
#
from marvel import small_dict
# TODO Практика 3
"""
1. Импорт from marvel import small_dict
2. Объявляем пустой список
3. Объявляем цикл по ключам и значениям
4. Проверяем дату выхода фильма (Значение словаря)
5. Если она равна 2023, добавляем название фильма в список

* Можно через list comprehension
"""

# print(small_dict.values())
# print(small_dict.keys())
# print(small_dict.items())

result = []

for title, year in small_dict.items():
    if year == 2023:
        result.append(title)

pprint(result)
result = [film for film, year in small_dict.items() if year == 2023]
pprint(result)

# TODO Практика 4
"""
1. Импорт from marvel import full_dict
2. Собрать из него список словарей типа 
[
    {
        'title': 'Железный человек',
        'year': 2008,
        'director': 'Джон Фавро',
        'screenwriter': 'Марк Фергус и Хоук Остби, Артур Маркам и Мэтт Холлоуэй',
        'producer': 'Ави Арад и Кевин Файги',
        'stage': 'Первая фаза'
    },
    ....
]
3. Записать это в файл marvel.json
"""