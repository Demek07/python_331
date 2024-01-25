"""
Lesson 37
25.01.2024
Паттерны поведения
- Генераторы
- Понятие итератора
- All и Any
- Итеративное чтение больших файлов
- Итеративный поиск по большому файлу
- Паттерн Iterator (итератор)
- Паттерн MVC (Model-View-Controller)
"""


class UserModel:
    def __init__(self, user_data: dict):
        self.user_data = user_data

    def get_user_data(self):
        return self.user_data

    def set_user_data(self, user_data: dict):
        self.user_data = user_data


class UserView:
    def display_user_data(self, user_data: dict):
        print("User Data:")
        for key, value in user_data.items():
            print(f"{key}: {value}")


class UserController:
    def __init__(self, model: UserModel, view: UserView):
        self.model = model
        self.view = view

    def update_view(self):
        user_data = self.model.get_user_data()
        self.view.display_user_data(user_data)

    def set_user_data(self, user_data: dict):
        self.model.set_user_data(user_data)


# Использование
def main():
    user_data = {'name': 'Alice', 'age': 30}
    model = UserModel(user_data)
    view = UserView()
    controller = UserController(model, view)

    controller.update_view()

    # Изменение данных пользователя
    controller.set_user_data({'name': 'Bob', 'age': 35})
    controller.update_view()


if __name__ == "__main__":
    main()


"""
Опишем модель Город (читаем JSON файл с данными о городах):
Опишем модель Представление (Красивый вывод данных):
Опишем модель Контроллер (Обработка данных):
- Проверка прав доступа
"""

import json

class CityModel:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def save_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    # Добавьте здесь методы для CRUD операций

from tabulate import tabulate

class CityView:
    def display_cities(self, students):
        print(tabulate(students, headers="keys"))

    def display_message(self, message):
        print(message)

    # Дополнительные методы для интерактивного взаимодействия с пользователем

class CityController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def display_cities(self):
        students = self.model.load_data()
        self.view.display_cities(students)

    # Методы для обработки пользовательского ввода и вызова соответствующих методов модели

def main():
    model = CityModel('cities.json') # Путь к файлу с данными указать более точный
    view = CityView()
    controller = CityController(model, view)

    controller.display_cities()

    # Здесь будет реализация взаимодействия с пользователем
    # Например, отображение меню и обработка команд

if __name__ == "__main__":
    main()
