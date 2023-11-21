# Lesson 6 03-09-2023
"""
СЕГОДНЯ

- Повторение материала
- For
- Операторы управления циклом (break, continue)
- Повторили join и split
- For - Else
- List Comprehension
- pop, remove (методы списков)
- Random (randint, shuffle, choice) - встроенный модуль random
- While
- While True
- While list - пока существует список
- While True + break (купи слона)
"""
from random import shuffle

# For
# shop_list = ['milk', 'bread', 'eggs', 'sugar', 'salt', 'apples']

# for item in shop_list:
#     if len(item) > 4:
#         print(f'{item.capitalize()} - {len(item)} символов')


# Операторы управления циклом (break, continue)
# break - прерывает цикл
# continue - прерывает текущую итерацию и переходит к следующей

# stop_item = 'sugar'
# for item in shop_list:
#     if item == stop_item:
#         print(f'Мы нашли {item}!')
#         break
#     print(item)

# Continue
# for item in shop_list:
#     if item == stop_item:
#         continue
#     print(f'{item} не является {stop_item}')

# Практика. Картавая задачка
"""
0. Сделайте переменную bad_letter = 'р'
1. Примите у пользователя слова через пробел
2. Разбейте их на список (split)
3. Пройдите по списку. Сделайте проверку на наличие буквы bad_letter в слове
4. Если такая буква есть, то сделайте break и напишите "плохое слово: {слово}"

"""
bad_letter = 'р'
# Todo Разобрать к концу пары однострочник
# [print(f'Плохое слово: {word}') for word in input('Введите слова через пробел: ').split() if bad_letter in word]

# Переменная с "плохой буквой"
# bad_letter = 'р'
# пользовательский ввод (получили строку)
# users_words = input('Введите слова через пробел: ')
# разбили строку на список по пробелу (пробел по умолчанию)
# users_words_list = users_words.split()
#
# for word in users_words_list:
#     if bad_letter in word:
#         print(f'Плохое слово: {word}')
#         break

# split - разбивает строку на список по разделителю
# some_string = 'дед;бабка;внучка;жучка;репка;картошка'
# some_string_lst = some_string.split(";")
# print(some_string_lst) # По умолчанию разделитель = пробел

# join - соединяет элементы списка в строку
# some_string_lst_joined = ' тянет '.join(some_string_lst)
# print(some_string_lst_joined)


#
# bad_letter = 'р'
# пользовательский ввод (получили строку)
# users_words = 'дед бабка внучка жучка репка картошка'
# разбили строку на список по пробелу (пробел по умолчанию)
# users_words_list = users_words.split()

# Используем continue для пропуска слова
# for word in users_words_list:
#     if bad_letter in word:
#         continue
#     print(f'Хорошее слово: {word}')

# TODO - Картавая задачка 2
"""
Проходим циклом по пользовательскому вводу
Если в списке есть больше 2х букв р - останавливаем цикл
Если цикл завершается успешно - выводим сообщение "Все слова хорошие"
"""

# bad_letter = 'р'
# user_words = input('Введите слова через пробел: ').split() # INPUT - ВСЕГДА ВОЗВРАЩАЕТ СТРОКИ!!!!
#
# for word in user_words:
#     if word.count(bad_letter) > 2:
#         print(f'Я не буду это говорить!)')
#         break
# else:
#     print('Все слова хорошие')

# TODO - Практика. Проверка всех чисел на четность
"""
1. Пользователь вводит числа через пробел
2. Мы проходим циклом по списку чисел и проверяем каждое число на четность
(проверка на четность - 10 % 2 == 0)
3. Если попалось нечетное число - пишем "Нечетное число: {число}" и выходим из цикла
4. Если цикл завершился успешно в блоке else пишем "Все числа четные"
"""

# [print(f'Нечетное число: {num}') for num in input('Введите числа через пробел: ').split() if int(num) % 2 != 0]

# user_numbers = input('Введите числа через пробел: ').split()
# not_int = []
#
# for item in user_numbers:
#     if item.isdigit():
#         num = int(item)
#         if num % 2 != 0:
#             print(f'Нечетное число: {num}')
#             break
#     else:
#         not_int.append(item)
# else:
#     print('Все элементы списка являются четными числами')
#     if not_int:
#         print(f'Элементы {not_int} вообще не являются числами')

# List Comprehension (Списковое включение) или Списковое выражение

# str_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'letter']
# res = []
# for item in str_nums:
#     if item.isdigit():
#         res.append(int(item))
#     else:
#         res.append(None)
# print(res)

# res_2 = [int(item) for item in str_nums]
# print(res_2)

# Тернарный оператор if - else
# item if item.isdigit() else 0

# res_3 = [int(item) if item.isdigit() else None for item in str_nums]
# print(res_3)

# Random ranint
# from random import randint # Импорт из модуля - правильно это делать в самом начале файла
#
# menu = ['pasta', 'eggs', 'milk', 'bread', 'meat']
# num = randint(0, len(menu) - 1)
# print(num)
# food = menu.pop(num)
# print(food)
# print(menu)

# if not menu: - если список НЕ пустой
# num = randint(0, len(menu) - 1)
# print(num)
# food = menu.pop(num)
# print(food)
# print(menu)

# .shuffle() - перемешивает список (изменяет существующий список)
# menu = ['pasta', 'eggs', 'milk', 'bread', 'meat']
# Импортируем shuffle
# from random import shuffle
# shuffle(menu) # Изменяет исходный список
# print(menu.pop()) # pop() - возвращает последний элемент списка и удаляет его из списка
# print(menu.pop())
# print(menu.pop())
# print(menu.pop())
# print(menu.pop())

# .choice() - возвращает случайный элемент из списка
# from random import choice
#
# menu = ['pasta', 'eggs', 'milk', 'bread', 'meat']
# random_food = choice(menu)
# print(random_food)
# # удалить значение из списка
# menu.remove(random_food)
# print(menu)

# While - цикл с предусловием (ПОКА!)

# while True: - бесконечный цикл

# count = 0
# while True:
#     print(f'Купи слона! прошу уже в {count} раз!')
#     count += 1
#

# count = 0
# while count < 10:
#     print(f'Купи слона! прошу уже в {count} раз!')
#     count += 1
#
# menu = ['pasta', 'eggs', 'milk', 'bread', 'meat']
# alcohol = []

# print(bool(menu)) # Непустой список - True
# print(bool(alcohol)) # Пустой список - False
#
# while menu:
#     shuffle(menu)
#     print(menu.pop())

# TODO Практика - все говорят {word} а ты купи слона!
"""
While True:
answer = input()
print(f'Все говорят {answer} а ты купи слона!')
"""
stop_list = ['да', 'хорошо', 'куплю', 'ок']
# answer = None while answer not in stop_list: answer = input('Ответ: ') print(f'Все говорят {answer}. А ты купи слона!')
while True:
    answer = input('Ответ: ')
    if answer.lower() in stop_list:
        print('Я знал, что я отлично умею продавать!')
        break
    print(f'Все говорят {answer}. А ты купи слона!')