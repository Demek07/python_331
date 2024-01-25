"""
Lesson 37
25.01.2024
Паттерны поведения
- Генераторы
- Понятие итератора
- Iterator (итератор)
"""
from time import sleep


# Генераторы
# Зачем нужны генераторы?

# Этот код вызовет падение (нехватка ОЗУ)

# Этот код попытается создать очень большой список чисел в памяти.
# Если число n достаточно велико, это может вызвать ошибку из-за нехватки памяти.

# n = 1000000000  # Очень большое число
# large_list = list(range(n))  # Создание большого списка
# print(sum(large_list))  # Суммирование элементов списка
#

# Этот код использует генератор для создания последовательности чисел.
# Генератор производит числа по одному, не сохраняя всю последовательность в памяти.
# Генераторы - это функции, которые возвращают объект-генератор (производят значения по одному за раз).


# def large_range(n):
#     i = 0
#     while i < n:
#         yield i  # Генератор возвращает значение и "замораживает" своё состояние до следующего вызова
#         i += 1


# n = 1000000000  # Очень большое число
# total = sum(large_range(n))  # Суммирование элементов генератора
# print(total)

# Однострочный вариант того и того
# total_list = sum(range(n))
# print(total_list)
#
# total_gen = sum(i for i in range(n))
# print(total_gen)


# Опишем бесконечный генератор, который будет возвращать от 0 до бесконечности
# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1


# Запустим цикл, который будет выводить значения генератора
# for i in infinite_sequence():
#     print(i)
#     sleep(1)

# Генератор для построчного чтения txt файла
# txt_file_path = "../data/generator_text.txt"
#
#
# def read_lines_file(file_path):
#     with open(file_path, "r", encoding='utf-8') as file:
#         for line in file:
#             yield line.strip()
#
#
# generator = read_lines_file(txt_file_path)
#
# for line in generator:
#     print(line)
#
