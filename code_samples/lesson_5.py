# Lesson 5
"""
Понятие итерируемый элемент
Цикл for
Итерация по строке - Цикл for
If in
Индексы строк
Range
Списки
Методы списков (обозначили какие существуют)
append()
split()
Циклы в циклах
Списки в списке


"""
# Строка - упорядоченная последовательность символов, итерируемый элемент.
# Неизменяемый тип данных

# Цикл for - цикл со счетчиком
# Итерация происходит до тех пор, пока не закончится итерируемый элемент

# string = 'HellO!'

# Простой цикл который выводит каждый символ строки по отдельности
# for symbol in string:
#     print(symbol)

# Это похоже на то, как если бы мы написали:
# print(string[0])
# print(string[1])
# print(string[2])
# print(string[3])
# print(string[4])
# print(string[5])


# счетчик, который считает количество букв в верхнем регистре
# upper_count = 0
#
# for symbol in string:
#     На каждой новой итерации в переменную symbol записывается новый символ
#     print(f'Работаем с символом {symbol}')
#     Мы можем проверить символ на соответствие какому-то условию
#     if symbol.isupper():
#         print(f'{symbol} - буква в верхнем регистре')
#         Если условие выполняется, то мы можем увеличить счетчик на 1
#         upper_count += 1

# print(f'Количество букв в верхнем регистре в строке {string} - {upper_count}')

# in - оператор проверки на вхождение элемента в последовательность
# if - in - проверка на вхождение элемента в последовательность

# fruits = "apple banana mango orange pear"
# check_fruit = "Apple"

# if check_fruit.lower() in fruits.lower():
#     print(f'Фрукт {check_fruit} есть в списке')
# else:
#     print(f'Фрукта {check_fruit} нет в списке')


# for index in range(100):
#     letter = fruits[index]
#     print(letter)

# fruits_len = len(fruits)

# for index in range(len(fruits)):
#     letter = fruits[index]
#     print(f'Индекс: {index}, буква: {letter}')

# Todo Практика 1. Итерация по строке
"""
Программа запрашивает у пользователя пароль
и считает количество чисел в пароле

Если в пароле 3 числа и более - выводит сообщение:
"True"
Если в пароле 2 числа и менее - выводит сообщение:
"False"

Инпут, счетчик, цикл с проверкой на число, и принт после.
"""

# password_input = input('Введите пароль: ')

# count = 0
#
# for item in password_input:
#     if item.isdigit():
#         count = count + 1  # count += 1

# print(f'Пароль надёжен: {count >= 3}')

# if count >= 3:
#     print(f'Пароль надёжен')
# else:
#     print(f'Пароль плох')


# Списки - list() - упорядоченная, изменяемая последовательность не уникальных элементов
# Список ссылается на элементы по индексу

# Создание списка
# empty_list = []
# empty_list = list()

# fruits = []
# fruits = ['apple', 'banana',
#           'mango', 'orange', 'pear']

# Индексы списков
# print(fruits[0])
# print(fruits[1])

# for fruit in fruits:
#     print(fruit)


# for i in range(len(fruits)):
#     print(fruits[i])


# print(f'Сегодня в меню фруктов: {len(fruits)}')
# for i in range(len(fruits)):
#     print(f'{i + 1}. {fruits[i].capitalize()}')


# Списки могут содержать в себе любые типы данных
# Даже другие списки

# mixed_list = [1, 2, 3, None, 0.2,
#               'mango', False, 'pear', [1, 2, 3]]

# Методы строк (для работы со списками)
# split() - разделяет строку на элементы списка по указанному разделителю
# join() - объединяет строки в одну строку, вставляя указанный разделитель между ними

# Методы списков
# append() - добавляет элемент в конец списка
# extend() - расширяет список другим списком
# count() - возвращает количество элементов, которые равны указанному
# sort() - сортирует список на основе функции сравнения
# insert() - добавляет элемент в список по указанному индексу
# remove() - удаляет первый элемент из списка, который равен указанному
# pop() - удаляет элемент из списка по указанному индексу и возвращает его
# clear() - очищает список
# index() - возвращает индекс первого элемента, который равен указанному
# reverse() - разворачивает список

# Получаем строку и разбиваем по пробелу на список
# user_passwords = '1а 22б 333в 4444г 55555д 666666е'
# pass_list = user_passwords.split() # Разделитель по умолчанию - пробел
# Проходим циклом по списку паролей и выводим их длину
# for password in pass_list:
#     print(f'Длина пароля {password} - {len(password)}')
# Проходим циклом по списку паролей, берем каждый пароль и проходим по нему циклом!
# for password in pass_list:
#     for symbol in password:
#         print(symbol)


# Создаем пустой список
# user_passwords = []
# fruits_list = ['apple', 'banana', 'mango', 'orange', 'pear']
#
# fruit_str = 'apple banana mango orange pear'
# fruits_list = fruit_str.split()


# fruits_list = ['apple', 'banana', 'mango', 'orange', 'pear']
# shugar_bombs = ['coca-cola', 'pepsi', 'sprite', 'candy', 'chocolate', 'cookies']
#
# user_menu = input('Введите то, что хотите съесть: ')
#
# good_menu = []

# for item in user_menu.split():
#     if item.lower() in fruits_list:
#         good_menu.append(item)
#
# print(f'Одобренное меню: {good_menu}')

# Список в списке для таблицы CSV меню с калорийностью
menu = [
    ['product', 'calories'],
    ['apple', 50],
    ['banana', 60],
    ['mango', 70],
    ['orange', 30],
    ['pear', 40],
    ['coca-cola', 100],
]

for list_ in menu:
    for word in list_:
        for symbol in word:
            print(symbol)
