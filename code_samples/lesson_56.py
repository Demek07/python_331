"""
Lesson 56 - Dataclasses
19.12.2023

- Определение датакласса
- Разница между обычным классом и датаклассом
- Атрибуты по умолчанию
- Параметры декоратора dataclass
    - order=True - генерация дандер методов сравнения (по умолчанию генерируется только __eq__)
"""
from dataclasses import dataclass


@dataclass(order=True)
class Person:
    name: str
    age: int
    address: str = 'Москва'




person = Person('ОлегГ', 23)
person2 = Person('Олег', 23)

print(person)
print(person2)

print(id(person))
print(id(person2))

print(person == person2)
print(person is person2)

print(person > person2)