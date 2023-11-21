# Lesson 7
# 05.10.2023
"""
Разбор ДЗ с вложенным циклом
Мини-разбор ДЗ с проверкой пароля
for
while
while - else
try - except - else - finally
raise
exception
set
set methods
set operations
"""

# Разбор ДЗ с вложенным циклом
# """
# Вам пришло секретное послание. Оно содержит много странных символов, которые вы не можете понять.
# Но вы знаете, что в этом послании используются только маленькие русские буквы. Используйте знание языка Python
# а так же знание for i чтобы расшифровать его.
# """

# Секретное послание
# secret_letter = [['DFВsjl24sfFFяВАДОd24fssflj234'], ['asdfFп234рFFdо24с$#afdFFтasfо'],
#                  ['оafбasdf%^о^FFжа$#af243ю'], ['afпFsfайFтFsfо13н'],
#                  ['fн13Fа1234де123юsdсsfь'], ['чFFтF#Fsfsdf$$о'],
#                  ['и$##sfF'], ['вSFSDам'], ['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'],
#                  ['FFэasdfтDFsfоasdfFт'], ['FяDSFзFFsыSfкFFf']]

# Список с маленькими русскими буквами
# small_rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
#              'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
#              'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
#
# result = ''
#
# for list_ in secret_letter:
#     for string in list_:
#         result += ' '
#         for sym in string:
#             if sym.lower() in small_rus:
#                 result += sym

# Приводим результат к нижнему регистру, потом с заглавной буквы
# result = result.lower()
# result = result.capitalize()
# print(result)

# print sep - разделитель
# print end - окончание строки

# print('Привет', 'мир', sep='Я РАЗДЕЛИТЕЛЬ', end='\n')
# print('Привет', 'мир', sep=' ', end='|Я ЭНД|')

# While - Else
# Else - выполняется, если цикл завершился без break

# counter = 0
# while True:
#     counter += 1
#     # % - остаток от деления
#     if counter > 99:
#         break
#     elif counter % 2 != 0:
#         continue
#     print(counter)


# flag = True
# product_list = []
# jank_food = ['конФеты', 'пЕченье', 'чИпсы', 'шоколадка', 'пончики', 'пироженка', 'пирожок', 'пирожное',
#              'пироженка', 'пирожок', 'пирожное', 'тОрт', 'пироженка', 'пирожок', 'пирожное']
#
# while flag:
#     product = input('Введите название продукта: ')
#     if product == 'стоп':
#         flag = False
#     elif product.lower() in [item.lower() for item in jank_food]:
#         print(f'{product} - запрещёнка!')
#         break
#     else:
#         product_list.append(product)
#
# else:
#     print(f'Вы попали в else.\n'
#           f'Идем в магазин купить {product_list}')


# Try - Except
# try: # Попробуй
#     print(10 / 0)
# except ZeroDivisionError: # Если ошибка деления на ноль
#     print('На ноль делить нельзя!')
# except TypeError: # Если ошибка типа данных
#     print('Нельзя делить строку на число!')
# except Exception as e: # Если ошибка любая другая
#     print(f'Ошибка: {e}')

# int_a = input('Введите число a : ')
# int_b = input('Введите число b : ')
# result = None

# try:
#     int_a = int(int_a)
#     int_b = int(int_b)
# except ValueError:
#     print('Вы ввели не число!')
#     # int_a, int_b = None, None
#     exit()
#
# try:
#     result = int_a / int_b
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
#     result = None
#
#
# if result is not None:
#     print(f'Результат деления: {result}')
#


# int_a = input('Введите число a : ')
# int_b = input('Введите число b : ')
# result = None
#
# try:
#     int_a = int(int_a)
#     int_b = int(int_b)
#     result = int_a / int_b
#
# except ValueError:
#     print('Вы ввели не число!')
#
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
#
# except Exception as e:
#     print(f'Ошибка: {e}')
#
# if result is not None:
#     print(f'Результат деления: {result}')

# try - except - else - finally
# try: # Попробуй
# except: # Если ошибка
# else: # Если ошибки нет
# finally: # В любом случае

# int_a = input('Введите число a : ')
# int_b = input('Введите число b : ')
# result = None
#
# try:
#     int_a = int(int_a)
#     int_b = int(int_b)
#     result = int_a / int_b
#
# except ValueError:
#     print('Вы ввели не число!')
#
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
#
# except Exception as e:
#     print(f'Ошибка: {e}')
#
# else:
#     print(f'Результат деления: {result}')
#
# finally:
#     print('finally. Я выполняюсь в любом случае!')

# Raise - генерация исключений
# Пишем программу для расшифровки оценок

# Если это число не входит в диапазон от 1 до 12 - генерируем исключение

# grade = input('Введите оценку: ')
#
# grade = int(grade)
#
# if not 1 <= grade <= 12:
#     raise ValueError(f'Оценка {grade} не входит в диапазон от 1 до 12')

# Популярные исключения
# ValueError - ошибка типа данных
# ZeroDivisionError - ошибка деления на ноль
# NameError - ошибка имени
# TypeError - ошибка типа данных
# IndexError - ошибка индекса
# KeyError - ошибка ключа
# AttributeError - ошибка атрибута
# FileNotFoundError - ошибка файла не найден
# ModuleNotFoundError - ошибка модуля не найден
# ImportError - ошибка импорта
# KeyboardInterrupt - ошибка прерывания пользователем

# Если пользователь ввел число вне диапазона который мы ждем - генерируем исключение ValueError

# Todo - Проверка длины пользовательского ввода
"""
Просим пользователя ввести строку не более 5 символов
Если длина строки больше 5 символов - генерируем исключение ValueError с сообщением:
"Длина строки больше 5 символов"
"""

# Мы знакомы со следующими типами данных
# - NoneType - тип данных None
# - int - целое число
# - float - число с плавающей точкой
# - str - строка
# - bool - булевый тип данных (True / False)
# - list - список

# Set - множество. Неупорядоченная коллекция уникальных элементов
# set() - создание пустого множества
# {} - создание пустого словаря

# set1 = {1, 2, 2}  # {1, 2} - уникальные элементы
# print(set1)
#
# set2 = set()
# set3 = {}  # ПУСТОЙ СЛОВАРЬ!!!

# Хеширование - превращение объекта в хеш.
# Хеш - уникальное число, которое соответствует объекту в памяти.
# Хеш - неизменяемый объект, поэтому его можно использовать
# в качестве ключа словаря или элемента множества

# Сет может хранить только неизменяемые объекты. Такие как:
# int, float, str, bool, tuple

# Методы множества
# add - добавление элемента в множество
# remove - удаление элемента из множества, если элемента нет - генерирует исключение KeyError
# discard - удаление элемента из множества, если элемента нет - ничего не делает
# pop - возвращает и удаляет случайный элемент из множества
# clear - очищает множество
# copy - копирует множество
# union - объединение множеств (|) - возвращает новое множество
# intersection - пересечение множеств (&) - возвращает новое множество
# difference - разность множеств (-) - возвращает новое множество
# symmetric_difference - симметричная разность множеств (^) - возвращает новое множество
# issubset - является ли множество подмножеством другого множества (<=)
# issuperset - является ли множество надмножеством другого множества (>=)
# isdisjoint - являются ли множества непересекающимися (если нет общих элементов - True, иначе - False)

# menu = ['pasta', 'eggs', 'milk', 'bread', 'meat', 'meat', 'meat']
# menu_set = set(menu)
#
# print(menu)
# print(menu_set)
#
# print(menu_set.pop())
# print(menu.pop())

# Ребята встретились и обсуждают своих знакомых. Есть ли общие знакомые, если да - то кто это?
# Кто кого знает, и кто кого не знает?

friends_1 = {'Алексей', 'Андрей', 'Антон', 'Артём', 'Александр', 'Елена', 'Сергей'}
friends_2 = {'Алексей', 'Андрей', 'Антон', 'Артём', 'Александр', 'Анна', 'Алина', 'Алёна', 'Максим'}

# Сколько мы знаем человек в сумме всего? - объединение множеств
all_friends = friends_1.union(friends_2)
all_friends = friends_1 | friends_2

print(all_friends)

# Ищем общих знакомых, которых знаем мы оба - пересечение множеств
common_friends = friends_1.intersection(friends_2)
common_friends = friends_1 & friends_2

print(common_friends)

# Ищем кого знаем мы, но не знает другой - разность множеств
friends_1_only = friends_1.difference(friends_2)
friends_1_only = friends_1 - friends_2

print(friends_1_only)

# Ищем кого знает другой, но не знаем мы - разность множеств
friends_2_only = friends_2.difference(friends_1)
friends_2_only = friends_2 - friends_1

print(friends_2_only)

# Ищем кого знает только один из нас - симметричная разность множеств
friends_only_one = friends_1.symmetric_difference(friends_2)
friends_only_one = friends_1 ^ friends_2

print(friends_only_one)
