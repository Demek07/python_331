"""
Lesson 40
06.02.2024
- pytest.mark.slow - маркировка тестов
Команда для вызова маркированных тестов:
Вызов тестов с маркировкой slow:
pytest -m slow
Вызов всех тестов кроме тех, что маркированы как slow:
pytest -m "not slow"

"""



# Пишем функцию a + b

def add(a, b):
    return a + b


