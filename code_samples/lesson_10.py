import csv
from pprint import pprint

from marvel import full_dict
from cities import cities_list
from tabulate import tabulate
# Lesson 10 (Пары 19-20)
# 17.10.2023

"""

**1. Разбор домашних заданий:**
   - Полный разбор поиск фильмов "по фазе" HW_8
   - Comprehension
   - Sep и end
   - Разбор начала домашнего задания HW_9
   - Полный разбор HW_6
   - Vusion theme - settings - Editor - Inlay Hints

**2. Чтение и запись в файл:**
   - Открытие файла для записи: `open("my_file.txt", "w")`
   - Запись текста в файл: `file.write("Привет, мир!")`
   - Закрытие файла: `file.close()`

**3. Флаги открытия файла:**
   - r: режим чтения
   - w: режим записи
   - a: режим дозаписи
   - b: бинарный режим (для работы с бинарными данными)

**4. Работа с контекстным менеджером (конструкция with):**
   - Открытие файла в контексте: `with open("my_file.txt", "w", encoding='UTF-8') as file:`
   - Запись данных в файл внутри контекста
   - Автоматическое закрытие файла после окончания блока контекста

**5. Построчное чтение файла:**
   - Метод `readline()` для чтения одной строки
   - Метод `readlines()` для чтения всех строк и получения списка строк

**6. Построчная запись в файл:**
   (Укажите соответствующие методы или примеры, если необходимо)

**7. Работа с CSV (Comma-Separated Values):**
   - Импорт библиотеки csv
   - Использование методов для чтения и записи CSV файлов:
     * `csv.reader(file)`
     * `csv.writer(file)`
     * `csv.DictReader(file)`
     * `csv.DictWriter(file, fieldnames)`

**8. Примеры работы с CSV:**
   - Запись и чтение данных в/из CSV файлов
   - Использование разделителя для CSV файлов


tabulate 

"""

# Поиск фильмов "по фазе" HW_8

# stage_dict = {
#     1: "Первая фаза",
#     2: "Вторая фаза",
#     3: "Третья фаза",
#     4: "Четвертая фаза",
#     5: "Пятая фаза",
#     6: "Шестая фаза",
# }

# input_user_stage = input('Введите номер фазы: ')
# if not input_user_stage.isdigit():
#     raise TypeError('Вы ввели не число')
#
# user_stage = int(input_user_stage)
#
# if user_stage not in stage_dict.keys():
#     raise ValueError('Такой фазы не существует')
#
# stage_string = stage_dict[user_stage]
# Comprehension
# result = {film_dict['title'] for film, film_dict in full_dict.items() if film_dict['stage'] == stage_string}
#
# pprint(result)

# Sep и end
# print('1', '2', 3, sep='|')
# print('1', '2', 3, sep='|', end='!')


# Разбор начала домашнего задания HW_9


# cities_set = set()
#
# for city in cities_list:
#     cities_set.add(city['name'])
#
# cities_set2 = {item['name'] for item in cities_list}
#
# print(len(cities_set))
# print(len(cities_set2))


# proverbs = [
#     "Ум хорошо, а два лучше.",
#     "Ум — горячая штука.",
#     "Ум всё голова.",
#     "Умом Россию не понять.",
#     "Ум бережет, а глупость губит.",
#     "Ум в голову приходит.",
#     "Ум от ума не горит.",
#     ]
#
# variants = [
#         'кот',
#         'шеф',
#         'мозг',
#         'лес',
#     ]


# proverbs_set = set(proverbs)
# variants_set = set(variants)
#
# result_list = []
#
# user_input = int(input('Сколько пословиц вывести? '))
#
# while proverbs_set and variants_set and len(result_list) != user_input:
#     random_proverb = proverbs_set.pop().lower()
#     random_variant = variants_set.pop().lower()
#     new_proweb = random_proverb.replace('ум', random_variant).capitalize()
#     result_list.append(new_proweb)
#
# print(result_list)


# Кодировки текста в Python.
# UTF-8 - Unicode Transformation Format
# ASCII - American Standard Code for Information Interchange

# Кодировка - это таблица символов и их соответствующих числовых значений
# Кодировка - это набор правил, по которым символы переводятся в байт-код

# Работа с TXT файлами
# open() - открытие файла

"""
r - режим чтения (Если файла не существует - ошибка)
w - режим записи (Если файла не существует - создается новый, если существует - перезаписывается)
a - режим дозаписи(Если не существует - создается новый, если существует - дозаписывается)
b - бинарный режим (для работы с бинарными данными)

"""
# data = 'Привет, мир!'

# file = open('my_file.txt', 'a', encoding='UTF-8')
# file.write(data+'\n')
# file.close()

# Работа с контекстным менеджером (конструкция with)
# with open('my_file.txt', 'a', encoding='UTF-8') as file:
#     file.write(data+'\n')

# data_list = ['Привет', 'мир', '!', 1974]
#
# # Запишем список строк в файл
# with open('my_file.txt', 'a', encoding='UTF-8') as file:
#     for line in data_list:
#         file.write(str(line)+'\n')
#
# # Пример чтения файла построчно:
# with open('my_file.txt', 'r', encoding='UTF-8') as file:
#     for line in file:
#         # Один перенос строк из файла, другой - из print end
#         print(line.strip(), end='')
#
#
#
#
# # Пример чтения файла одной строкой:
# with open('my_file.txt', 'r', encoding='UTF-8') as file:
#     data = file.read()
# print(data)
#
#
#
# # Пример чтения файла списком строк:
# with open('my_file.txt', 'r', encoding='UTF-8') as file:
#     data = file.readlines()
# print(data)
# new_data = [data_string.strip() for data_string in data]
# print(new_data)
#
#
# # from tabulate import tabulate
#
#
# # Список словарей из full_dict состоящий из values
# result_lst = [value for value in full_dict.values()]
#
# html_table = tabulate(result_lst, headers='keys', tablefmt='html')
# # Запись в HTML файл
#
# css_styles_table = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Marvel Table</title>
#     <style>
#     table {
#         border-collapse: collapse;
#     }
#     td, th {
#         border: 1px solid black;
#         padding: 5px;
#     }
#     </style>
# </head>
# <body>
# """
#
# end_html = """
# </body>
# </html>
# """
#
# # Пишем файл HTML
# with open('marvel.html', 'w', encoding='UTF-8') as file:
#     file.write(css_styles_table)
#     file.write(html_table)
#     file.write(end_html)

# Работа с CSV
# CSV - Comma-Separated Values (значения разделенные запятыми)
# Импорт библиотеки csv
# Использование методов для чтения и записи CSV файлов:
# csv.reader(file)
# csv.writer(file)
# csv.DictReader(file)
# csv.DictWriter(file, fieldnames)

# Примеры работы с CSV:

data_list = [
    ['Год', 'Фильм', 'Рейтинг'],
    ['2012', 'Marvel\'s The Avengers', '8'],
    ['2023', 'Avengers: Endgame', '8.5'],
    ['2018', 'Black Panther', '7.3'],
    ['2017', 'Thor: Ragnarok', '7.9'],
    ['2016', 'Captain America: Civil War', '7.8'],
    ]

# Запись и чтение данных в/из CSV файлов
# with open('marvel.csv', 'w', encoding='UTF-8') as file:
#     writer = csv.writer(file)
#     for row in data_list:
#         writer.writerow(row)


# # Записываем в кодировке Винды + разделитель ; убираю черезстрочную запись
# with open('marvel.csv', 'w', encoding='windows-1251', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerows(data_list)
#
# new_csv_string = ['2012', 'Marvel\'s The Avengers', '8']
#
#
# # Добавляем новую строку в файл
# with open('marvel.csv', 'a', encoding='windows-1251', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(new_csv_string)
#
# # Прочитаем данные из файла marvel.csv
# with open('marvel.csv', 'r', encoding='windows-1251') as file:
#     reader = csv.reader(file, delimiter=';')
#     for row in reader:
#         print(row)

# CSV Dict
# Читаем в словарь

# with open('marvel.csv', 'r', encoding='windows-1251') as file:
#     reader = csv.DictReader(file, delimiter=';')
#     for row in reader:
#         print(row)



# new_marvel_dict_list = [
#     {'Год': '2029', 'Фильм': 'Чебурашка против Таноса', 'Рейтинг': '10'},
#     {'Год': '2028', 'Фильм': 'Чебурашка спасает галактику', 'Рейтинг': '10'}
# ]
#
# # Дозаписываем данные в файл
# with open('marvel.csv', 'a', encoding='windows-1251', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=['Год', 'Фильм', 'Рейтинг'], delimiter=';')
#     writer.writerows(new_marvel_dict_list)
#
#
# # Получаем список словарей из файла
# with open('marvel.csv', 'r', encoding='windows-1251') as file:
#     reader = csv.DictReader(file, delimiter=';')
#     marvel_list = [row for row in reader]
#
# pprint(marvel_list)

# TODO Практика по CSV
"""
1. Получаем список словарей Марвел
2. Пишем в файл marvel.csv
"""

marvel_list_dict = []

for item in full_dict.values():
    marvel_list_dict.append(item)

# ЗАПИСЬ В CSV
"""
Ключи словаря:
- title
- year
- director
- screenwriter
- producer
- stage
"""
# Записываем данные в файл с указанием заголовков столбцов
with open('marvel.csv', 'w', encoding='windows-1251', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'year', 'director', 'screenwriter', 'producer', 'stage'],
                            delimiter=';')
    writer.writeheader() # Записываем заголовки столбцов
    writer.writerows(marvel_list_dict) # Записываем данные