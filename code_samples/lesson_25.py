"""
Lesson 25
28.11.2023
Знакомство с ООП в Python
"""

"""
Правила нейминга:
- Классы - CamelCase
- Функции и методы - snake_case
- Переменные и поля - snake_case

Классы принято называть существительными, а методы - глаголами.
Классы объявляются с помощью ключевого слова class.
"""


class Car:
    pass


car_1 = Car()
car_2 = Car()
print(car_1)
print(car_2)
print(type(car_1))
print(type(car_2))

# Это точно так же как и со встроенными типами данных
# Например строки. Мы можем создать две строки с одинаковым значением, но это будут разные объекты

# Создаем 2 строки
str_1 = str('Helloa')
str_2 = str('Hello')

print(str_1)
print(str_2)
# У них тип строка
print(type(str_1))
print(type(str_2))
# Есть адреса в памяти
print(id(str_1))
print(id(str_2))


