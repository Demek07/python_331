"""
Lesson 37
25.01.2024
Паттерны поведения
- Генераторы
- Понятие итератора
- Iterator (итератор)
"""
from time import sleep

# Однострочный генератор чисел до 3
gen = (i for i in range(3))
# print(len(gen)) # TypeError: object of type 'generator' has no len()
# next() - возвращает следующий элемент генератора

while True:
    try:
        print(next(gen))
    except StopIteration:
        print("Генератор закончил работу")
        break


# All - возвращает True, если все элементы истинны
# Any - возвращает True, если хотя бы один элемент истинный

list_1 = [1, 1, 1, 0]
list_2 = [1, 1, 1, 1]
list_3 = [0, 0, 0, 0]

print(all(list_1))  # False
print(all(list_2))  # True
print(not all(list_3))  # True (not False = True)
print(any(list_1))  # True
print(any(list_3))  # False

list_letters = ["a", "b", "c", "1"]
# is alpha - проверяет, что строка состоит только из букв
# comprihension - списковое включение
print(all([letter.isalpha() for letter in list_letters]))  # False

# Генератор
print(all(letter.isalpha() for letter in list_letters))  # False

# Any
print(any(letter.isalpha() for letter in list_letters))  # True

# Поищем в списке list_letters "b"
print(any(letter.lower() == "b" for letter in list_letters))  # True

# TODO Практика - реализовать функцию any
"""
Опишите функцию генератор чтения файлов построчно.
Запросите у пользователя поисковое слово.
Через any() проверьте есть ли в файле строка (приведите к нижнему регистру) - "поисковое слово"
Если есть - выведите "поисковое слово", если нет - "поисковое слово"
"""