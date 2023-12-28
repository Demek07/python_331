"""
Lesson 31
Класс сериализации и класс валидации
сериализация - преобразование объекта в строку
де-сериализация - преобразование строки в объект
валидация - проверка данных на корректность
json schema - формат для описания json данных
"""
from dataclasses import dataclass
from pprint import pprint
from typing import List

# todo Практика
"""
1. Датакласс Film
2. Класс FilmValidator
- проверка что есть ключи title, year
- проверка что title - строка, year - число
3. Класс FilmSerializer
- принимает словарь - отдает дата класс
4. Цикл в main функции для проверки
- получите на выходе список дата классов Film
"""


@dataclass
class Film:
    title: str
    year: int
    director: str
    screenwriter: str
    producer: str
    stage: str


class FilmValidator:

    @staticmethod
    def validate(film: dict) -> bool:
        if not isinstance(film, dict):
            raise ValueError("Должен быть словарь")
        if "title" not in film or "year" not in film:
            raise ValueError("Нет ключей title или year")
        if not isinstance(film["title"], str):
            raise ValueError("Ключ title должен быть строкой")
        if not isinstance(film["year"], int):
            raise ValueError("Ключ year должен быть числом")
        return True


class FilmSerializer:

    def __init__(self):
        self.validator = FilmValidator()

    @staticmethod
    def serialize(film: dict) -> Film:
        if FilmValidator.validate(film):
            return Film(**film)


def main():
    from data.marvel import full_dict
    print(f'Всего фильмов: {len(full_dict)}')
    films = []
    for film in full_dict.values():
        try:
            film = FilmSerializer.serialize(film)
            films.append(film)
        except ValueError as exc:
            print(f"Ошибка валидации: {exc}")

    print(f'Всего фильмов после: {len(films)}')


if __name__ == '__main__':
    main()
