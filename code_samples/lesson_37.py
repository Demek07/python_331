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


