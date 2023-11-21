# Lesson 2
"""
- Bool
- Зарезервированные слова
- Input
- Изменение типов
- Математические операторы
- Округление round()
- Строки и математические операторы
- Print (Аргументы через запятую)
- Операторы сравнения
- Логические операторы
- Приоритет выполнения логических операторов
- Ошибки синтаксические и логические
- F-строки
"""

"""
Служебные слова (зарезервированные слова)
'False', 'None', 'True', 'and', 'as', 'assert',
'break', 'class', 'continue', 'def', 'del', 'elif',
'else', 'except', 'finally', 'for', 'from', 'global',
'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
'not', 'or', 'pass', 'raise', 'return', 'try',
'while', 'with', 'yield'
"""

# print = 1
# print(print)

# int - целые числа
# float - числа с плавающей точкой
# str - строки

# bool - булевы значения (True, False)
# input('Нажми Enter') # Чтобы программа не закрылась

# name = input('Введите ваше имя: ')
# print(name)
# type_name = type(name)
# print(type(name))

# int() - преобразование в целое число
# str() - преобразование в строку
# float() - преобразование в число с плавающей точкой

# integer = input('Введите целое число: ')
# integer = int(integer)
# print(type(integer))

# print()

# Математические операторы
# + - сложение
# - - вычитание
# * - умножение
# / - деление
# // - целочисленное деление
# % - остаток от деления
# ** - возведение в степень

num_1 = 10
num_2 = 3

# print(num_1 + num_2)
# print(num_1 - num_2)
# print(num_1 * num_2)
# print(num_1 / num_2)
# print(num_1 ** num_2)
# Целочисленное деление - возвращает только целую часть от деления
# print(num_1 // num_2)
# Остаток от деления - возвращает только остаток от деления
# print(num_1 % num_2)

# Округление round()
result = num_1 / num_2
# print(result)
round_res = round(result, 2)  # Округление до 2 знаков после запятой
# print(round_res)

# round - округление
# Первый аргумент - число, которое нужно округлить
# Второй аргумент - количество знаков после запятой

iphone_price = 100600
# print(round(iphone_price, -3))  # Округление до сотен

# TODO Практическое задание
# 1. Напишите кредитный калькулятор
# - Пользователь вводит сумму кредита
# - Пользователь вводит годовую процентную ставку
# - Пользователь вводит срок кредита в годах

# Программа должна вывести:
# - Общая сумма выплат

# Не обязательно - ежемесячную сумму выплат
# сумма переплаты

# money = int(input('Введите сумму кредита: '))
# rate = int(input('Введите годовую процентную ставку: '))
# years = int(input('Введите срок кредита в годах: '))

# overpayment_amount = money * rate / 100 * years
# full_amount = money + overpayment_amount

# Запись в одну строку
# full_debt = money + (money * rate / 100 * years)
# full_debt2 = money + money * rate / 100 * years

# print(full_debt)
# print(full_debt2)
# Приоритет выполнения операций
# 1. Скобки
# 2. Возведение в степень
# 3. Умножение, деление, целочисленное деление, остаток от деления
# 4. Сложение и вычитание

# print('Полный долг')
# print(full_debt)

# print('Полный долг', full_debt)
# print('Полный долг', '12313')

# full_debt = 'Полный долг' + ' ' + 222 # TypeError: can only concatenate str (not "int") to str
# full_debt = 'Полный долг' + ' ' + str(222)

# print('+' / 50) # TypeError: unsupported operand type(s) for /: 'str' and 'int'
# print('+' * 50)

# Boolean - булевы значения
# True - истина
# False - ложь
# 0 - ложь
# -n...(кроме 0) +n...  - истина
# '' - ложь
# ' ' - истина

# Сравнение чисел
# > - больше
# < - меньше
# >= - больше или равно (> = )
# <= - меньше или равно (< = )
# == - равно ( = = )
# != - не равно (! = )

# print(2<1)
# print(2>1)
# print(2>=1)
# print(2<=1)
# print(2==1)
# print(2!=1)

# Сравнение строк
# Сравнение строк происходит посимвольно

# print('a' > 'b')
# print('a' < 'b')
# print('a' == 'b')
# print('a' != 'b')

# print('John' > 'Johny') # Сравнение посимвольно. Как в словаре

# Логические операторы
# and - и
# or - или
# not - не

# True and True - True
# True and False - False
# False and True - False
# False and False - False

# True or True - True
# True or False - True
# False or True - True
# False or False - False

# not True - False
# not False - True

# age = int(input('Введите ваш возраст: '))
# Можно всё
# is_alcohol = age >= 21


# Можно войти но нельзя пить
# is_coming = 18 <= age < 21
# С использованием логических операторов
# is_coming = 18 <= age and age < 21

# not_coming = age > 18

# print('Можно ли войти:', not_coming)
# print('Можно войти но нельзя пить:', is_coming)
# print('Можно ли всё:', is_alcohol)


# Приоритет выполнения логических операторов
# 1. not
# 2. and
# 3. or

# Примеры важности приоритета
# True or False and False - True
# True or (False and False) - True
# (True or False) and False - False

# True and False or False - False
# (True and False) or False - False
# True and (False or False) - False

# Синтаксические ошибки
# SyntaxError: invalid syntax - неверный синтаксис

# print('Hello, world!')  # Синтаксически верно
# print('Hello, world!)  # Синтаксически неверно
# print(2/0)  # ZeroDivisionError: division by zero - деление на ноль

# F-строки (f-strings) formatted string literals

name = 'Сёма'
last_name = 'Иванов'
age = 12
nick = 'Сёмушка'

print('Hello, ' + name + ' ' + last_name + '! You are ' + str(age) + ' years old!')

formatted_string = (f'Hello, {name} {last_name}! You are {age} years old!'
                    f'Your nick is "{nick}"')

print(formatted_string)

# f-строки - форматированные строки
# r-строки - сырые строки (raw strings)

file_path = 'c:\\new_folder\\text.txt'
file_path = r'c:\new_folder\text.txt'

doc = 'text.txt'
file_path = fr'c:\new_folder\{doc}'

a = 5
b = 5
# F-строки поддерживают выражения
a_b = f'a + b = {a + b}'
print(a_b)
a_b = f'a + b = {type(a + b)}'
print(a_b)

# Отладочная строка
print(f'{a+b=}')
print(f'Я вызвал type к a+b{type(a+b)=}')

# Округление с помощью f-строк
pi = 3.1415926535
print(f'Число Пи равно {pi:.2f}') # 2f - 2 знака после запятой

pi = 3,1415926535
print(pi)
print(type(pi))
