"""
Lesson 56 - Dataclasses
19.12.2023

- Определение датакласса
- Разница между обычным классом и датаклассом
- Параметры декоратора dataclass
    - order
"""
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


person = Person('Юлия', 24)
person2 = Person('Юлия', 23)

print(person)
print(person2)

print(id(person))
print(id(person2))

print(person == person2)
print(person is person2)