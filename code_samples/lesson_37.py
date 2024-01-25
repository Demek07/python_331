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

# Решение практики
# Генератор для построчного чтения txt файла
txt_file_path = "../data/generator_text.txt"


def read_lines_file(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        for line in file:
            yield line.strip()


generator = read_lines_file(txt_file_path)

# Поиск слова в файле
search_word = input("Введите слово для поиска: ")
result = any(search_word.lower() in line.lower() for line in generator)
if result:
    print(f"Слово '{search_word}' найдено в файле")
else:
    print(f"Слово '{search_word}' не найдено в файле")

# А если нам нужно поискать и вывести все строки, в которых есть искомое слово?
# Тогда нам нужно использовать функцию filter()
# Filter - фильтрует элементы по условию
# Возвращает объект-генератор

result = filter(lambda line: search_word.lower() in line.lower(), read_lines_file(txt_file_path))
print(list(result))

# В полном виде