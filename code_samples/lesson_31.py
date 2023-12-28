"""
Lesson 31
Класс сериализации и класс валидации
сериализация - преобразование объекта в строку
де-сериализация - преобразование строки в объект
валидация - проверка данных на корректность
json schema - формат для описания json данных
"""
from dataclasses import dataclass
from typing import List

# простая структура данных для примера ручной валидации

students = [
    {
        "name": "Вася",
        "age": 19,
        "city": "Москва",
        "email": "vas-99@mail.ru",
        "phone": "89999999999",
        "courses": ["Python", "Git", "JS", "HTML", "CSS"]
    },
    {
        "name": "Петя",
        "age": 17,
        "city": "Москва",
        "email": "peter2001@yandex.ru",
        "phone": "89999999998",
        "courses": ["Python", "Git", "JS", "HTML", "CSS"]
    },
    {
        "name": "Вася",
        "age": 19,
        "city": "Москва",
        "email": "vas-99@mail.ru",
        "phone": "89999999999",
        "courses": ["Python", "Git", "JS", "HTML", "CSS"]
    },
    {
        "name": "Василиса",
        "age": '17',
        "city": "Москва",
        "email": "vasilisya@yandex.ru",
        "phone": "89999999998",
        "courses": ["Python", 'Assembler', 123]
    },
]


@dataclass
class Student:
    name: str
    age: int
    city: str
    email: str
    phone: str
    courses: list


class StudentValidator:
    """
    Класс для валидации данных о студенте.
    Дандер метод __call__ принимает словарь на проверку и возвращает True, если данные валидны, иначе False
    """

    def __init__(self):
        self.__student_data: dict | None = None
        self.__dict_keys: List[str] = ["name", "age", "city",
                                       "email", "phone", "courses"]

    def __validate_dict_keys(self):
        """
        Метод для проверки наличия всех ключей в словаре
        :return: True, если все ключи присутствуют, иначе False
        """
        return all(key in self.__student_data for key in self.__dict_keys)

    @staticmethod
    def __is_string(value):
        return isinstance(value, str)

    @staticmethod
    def __is_int(value):
        return isinstance(value, int)

    def __validate_email(self):
        """
        Метод для валидации email
        :return: True, если email валидный, иначе False
        """
        return self.__student_data["email"]

    def __validate_phone(self):
        """
        Метод для валидации телефона
        :return: True, если телефон валидный, иначе False
        """
        return self.__student_data["phone"]

    def __validate_age(self):
        """
        Метод для валидации возраста
        :return: True, если возраст валидный, иначе False
        """
        return self.__is_int(self.__student_data["age"])

    def __validate_name(self):
        """
        Метод для валидации имени
        :return: True, если имя валидное, иначе False
        """
        return self.__student_data["name"]

    def __validate_city(self):
        """
        Метод для валидации города
        :return: True, если город валидный, иначе False
        """
        return self.__student_data["city"]

    def __validate_courses(self):
        """
        Метод для валидации курсов
        :return: True, если курсы валидные, иначе False
        """
        return all(self.__is_string(course) for course in self.__student_data["courses"])

    def __validate(self):
        """
        Метод для валидации данных о студенте.
        Использует все методы валидации. Если проверка не проходит, возвращает False
        А так же raise ValueError с описанием ошибки
        :return: True, если данные валидны, иначе False
        """
        if not self.__validate_dict_keys():
            raise ValueError("В словаре не хватает ключей")

        if not self.__validate_name():
            raise ValueError("Имя не является строкой")

        if not self.__validate_age():
            raise ValueError("Возраст не является числом")

        if not self.__validate_city():
            raise ValueError("Город не является строкой")

        if not self.__validate_email():
            raise ValueError("Email не является строкой")

        if not self.__validate_phone():
            raise ValueError("Телефон не является строкой")

        if not self.__validate_courses():
            raise ValueError("Курсы не являются строками")

        return True

    def __call__(self, student_data: dict) -> bool:
        self.__student_data = student_data
        return self.__validate()


class StudentSerializer:
    """
    Класс для десериализации данных о студенте.
    Композиция: создается экземпляр класса валидации при инициализации класса сериализации
    __call__ принимает словарь, прогоняет его через валидатор и возвращает экземпляр дата-класса Student
    """

    def __init__(self):
        self.__validator = StudentValidator()

    def __call__(self, student_data: dict) -> Student:
        self.__validator(student_data)
        return Student(**student_data)


if __name__ == "__main__":
    # Создаем экземпляр сериализатора
    serializer = StudentSerializer()
    students_obj_list = []

    # Проходимся по списку словарей и преобразуем их в экземпляры дата-класса Student
    for student in students:
        try:
            student_obj = serializer(student)
            students_obj_list.append(student_obj)
        except ValueError as e:
            print(f"Ошибка в данных: {e}")

    print(students_obj_list)