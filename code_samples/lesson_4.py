# Lesson 4 26.09
"""
СЕГОДНЯ
- Сокращенная запись условий
- Bool и встроенные типы данных
- Вложенные условия
- Методы строк
- Условные операторы + методы строк
- Практика
- Реализация сложных проверок (вложенные условия) VS плоская структура
"""

# Сокращенная запись условий
# flag

# is_vegan = True
#
# if is_vegan:
#     print('Веган')

# Bool и встроенные типы данных
# 0 - False
# -n... +n... - True
# '' - False
# ' ' - True
# None - False

# На будущее (еще не проходили)
# [] - False
# [1, 2, 3] - True
# {} - False
# {'key': 'value'} - True
# () - False
# (1, 2, 3) - True

# int_input = int(input('Введите 1 если да, и 0 если нет: '))
#
# if int_input:
#     print('Вы сказали ДА')
# else:
#     print('Вы сказали НЕТ')

# Методы строк.

# Методы - это функции, которые привязаны к объекту
# len() - функция!!!!! возвращает длину строки
# split() - разделяет строку на подстроки по указанному разделителю
# join() - объединяет строки в одну строку, вставляя указанный разделитель между ними
# replace() - заменяет все вхождения подстроки в строку на указанную подстроку
# count() - считает количество вхождений подстроки в строку
# find() - возвращает индекс первого вхождения подстроки в строку
# lower() - приводит строку к нижнему регистру
# upper() - приводит строку к верхнему регистру
# strip() - удаляет пробельные символы в начале и в конце строки
# capitalize() - приводит строку к виду, где первая буква заглавная, а остальные строчные
# title() - приводит строку к виду, где первые буквы каждого слова заглавные, а остальные строчные
# lstrip() - удаляет пробельные символы в начале строки
# rstrip() - удаляет пробельные символы в конце строки
# isdigit() - проверяет, что строка состоит только из цифр
# isalpha() - проверяет, что строка состоит только из букв
# isalnum() - проверяет, что строка состоит только из букв и цифр
# islower() - проверяет, что строка состоит только из символов в нижнем регистре
# isupper() - проверяет, что строка состоит только из символов в верхнем регистре
# isspace() - проверяет, что строка состоит только из пробелов
# startswith() - проверяет, что строка начинается с указанной подстроки
# endswith() - проверяет, что строка заканчивается указанной подстрокой
# rfind() - возвращает индекс последнего вхождения подстроки в строку
# swapcase() - меняет регистр всех символов в строке

some_string = 'Привет, мир!'
sub_string = 'Привет'
# len() - функция!!!!! возвращает длину строки
# print(len(some_string))

# count() - считает количество вхождений подстроки в строку
# print(some_string.count(sub_string))

# find() - возвращает индекс первого вхождения подстроки в строку
# print(some_string.find(sub_string))

# replace() - заменяет все вхождения подстроки в строку на указанную подстроку
new_string = "пока"
replaced_string = some_string.replace(sub_string, new_string).capitalize()
# print(replaced_string)

# TODO Практика 1. Методы строк. Count и Find
"""
1. Объявите переменную со строкой из 2-3 слов (тоже можно на пользовательском вводе)
2. Запросите пользовательский ввод
3. С помощью метода count() проверьте сколько раз в строке 
встречается введенное пользователем слово
4. Если больше 0 - выведите на экран сообщение:
"Слово <слово> встречается в строке <количество> раз"
"Первое вхождение <слово> в строке начинается с индекса <индекс>" - метод find()
5. Если 0 - выведите на экран сообщение:
"Слово <слово> не встречается в строке"
"""

first_string = """
Скажи ка дядя ведь не даром
Москва спаленная пожаром
Французу отдана

Ведь были ж схватки боевые
Да говорят еще какие
Недаром помнит вся Россия
Про день Бородина
"""
# search_string = input('Введите слово или словосочетание для поиска: ').lower()
# first_string = first_string.lower()
# count_result = first_string.count(search_string)
#
# if count_result > 0:
#     first_index = first_string.find(search_string)
#     print(f'Место где было найдено слово: {first_string[first_index-10:first_index+10]}')
#     if first_index < 20:
#         pass
#         # Тут новый срез
#
#     print(f'Искомый запрос встречается впервые с индекса {first_index}')
#
# else:
#     print(f'Искомый запрос не встречается в строке')

# TODO (Самостоятельно вне пары) - сложная версия
"""
Попробуйте сделать вывод диапазона текста в котором встречается искомое слово
Главное учтите, что если оно встречается в начале или в конце текста, то
надо сделать проверку на выход за границы строки

"""

# Strip() - удаляет пробельные символы в начале и в конце строки
# По умолчанию удаляет пробелы и переносы строк
# Можно передать в качестве аргумента символ, который нужно удалить
some_str = ' Привет, мир!\n '
# print(some_str)
# print(some_str.strip())
# print(some_str.strip().strip('мир!'))
# print(some_str.replace('мир!', ''))


# mail_string = '@name@'
# print(mail_string.strip('@'))
# print(mail_string.rstrip('@'))
# print(mail_string.lstrip('@'))
#
# user_name = input('Введите ваш @username: ')
#
# if user_name.startswith('@'):
#     print('Все ок')
# else:
#     print('Нужно ввести @username')

# is_digit() - проверяет, что строка состоит только из цифр
# is_alpha() - проверяет, что строка состоит только из букв
# is_alnum() - проверяет, что строка состоит только из букв и цифр

str_1 = '123'
str_2 = '123abc'
str_3 = 'abc'
str_4 = "*&^*`~"
str_5 = "123abc "
str_6 = '1234afb&(&^ '
str_7 = 'ABC'
str_8 = 'abc'
str_9 = "ABc"
str_10 = '123ABC'
str_11 = '*:?:%?AV'
str_12 = '123(&(%&^'

# print(f'{str_1.isdigit()=}')
# print(f'{str_2.isdigit()=}')
# print(f'{str_3.isdigit()=}')
# print(f'{str_4.isdigit()=}')
# print(f'{str_5.isdigit()=}')
# print(f'{str_6.isdigit()=}')
# print(f'{str_7.isdigit()=}')
# print(f'{str_8.isdigit()=}')
# print(f'{str_9.isdigit()=}')
#
# print(f'{"="*20}\n'
#       f'isalpha()\n')
# print(f'{str_1.isalpha()=}')
# print(f'{str_2.isalpha()=}')
# print(f'{str_3.isalpha()=}')
# print(f'{str_4.isalpha()=}')
# print(f'{str_5.isalpha()=}')
# print(f'{str_6.isalpha()=}')
# print(f'{str_7.isalpha()=}')
# print(f'{str_8.isalpha()=}')
# print(f'{str_9.isalpha()=}')
#
#
# print(f'{"="*20}\n'
#       f'isalnum()\n')
# print(f'{str_1.isalnum()=}')
# print(f'{str_2.isalnum()=}')
# print(f'{str_3.isalnum()=}')
# print(f'{str_4.isalnum()=}')
# print(f'{str_5.isalnum()=}')
# print(f'{str_6.isalnum()=}')
# print(f'{str_7.isalnum()=}')
# print(f'{str_8.isalnum()=}')
# print(f'{str_9.isalnum()=}')
#
# print(f'{"="*20}\n'
#       f'islower()\n')
#
# print(f'{str_1.islower()=}')
# print(f'{str_2.islower()=}')
# print(f'{str_3.islower()=}')
# print(f'{str_4.islower()=}')
# print(f'{str_5.islower()=}')
# print(f'{str_6.islower()=}')
# print(f'{str_7.islower()=}')
# print(f'{str_8.islower()=}')
# print(f'{str_9.islower()=}')
# print(f'{str_10.islower()=}')
#
# print(f'{"="*20}\n'
#         f'isupper()\n')
#
# print(f'{str_1.isupper()=}')
# print(f'{str_2.isupper()=}')
# print(f'{str_3.isupper()=}')
# print(f'{str_4.isupper()=}')
# print(f'{str_5.isupper()=}')
# print(f'{str_6.isupper()=}')
# print(f'{str_7.isupper()=}')
# print(f'{str_8.isupper()=}')
# print(f'{str_9.isupper()=}')
# print(f'{str_10.isupper()=}')
# print(f'{str_11.isupper()=}')
# print(f'{str_12.isupper()=}')


# Проверка на длину строки + на то, что в ней есть буквы разных регистров
#
# input_string = input('Введите пароль: ')
#
# if len(input_string) >= 8:
#     # Длина строки больше 8 символов
#     if not (input_string.islower() or input_string.isupper()):
#         # Проверка на то, что строка не состоит только из символов одного регистра
#         print('Пароль подходит')
#     else:
#         print('В пароле должны быть символы разных регистров')
# else:
#     print('Пароль должен быть не менее 8 символов')
#
# Пишем то же, но в плоском виде

# Флаги
is_len = False
is_reg = False

# Строка для лога ошибок
res_str = ''

input_string = input('Введите пароль: ')

# Проверка на длину строки
if len(input_string) >= 8:
    is_len = True  # Меняем флаг длины на True
else:
    res_str += 'Пароль должен быть не менее 8 символов\n'

# Проверка на регистр в плоской структуре
if not (input_string.islower() or input_string.isupper()):
    is_reg = True  # Меняем флаг регистра на True
else:
    res_str += 'В пароле должны быть символы разных регистров\n'


if is_len and is_reg:
    res_str += 'Пароль подходит\n'
else:
    res_str += 'Пароль не подходит\n'

print(res_str)

# Проверка в одну строку

if (len(input_string) >= 8 and
        not (input_string.islower() or input_string.isupper())):
    print('Пароль подходит')