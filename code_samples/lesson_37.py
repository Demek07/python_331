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
"""


# Итератор который будет создавать и возвращать только четные числа от 0 до n

class EvenIterator:
    """
    Тут нет метода __iter__ который возвращает сам итератор
    Поэтому мы не сможем использовать наш итератор в цикле for
    Однако мы можем использовать это в цикле while через next()
    """
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __next__(self):
        if self.current < self.n:
            self.current += 2
            return self.current
        else:
            raise StopIteration


# Тестируем наш итератор
even_iterator = EvenIterator(10)
print(next(even_iterator))
print(next(even_iterator))
print(next(even_iterator))

even_iterator_2 = EvenIterator(15)


# EvenIterator2 имеющий метод __iter__ который возвращает сам итератор
class EvenIterator2:
    def __init__(self, n):
        """
        На инициализацию принимает число n, до которого будет возвращать четные числа
        :param n:
        """
        self.n = n
        self.current = 0

    def __iter__(self):
        """
        Метод __iter__ возвращает сам итератор
        Без него мы не сможем использовать наш итератор в цикле for
        :return:
        """
        return self

    def __next__(self):
        """
        Метод __next__ возвращает следующее четное число
        Тут мы явно описываем то, что должен делать наш итератор
        Само возвращаемое значение и условие остановки итератора
        :return:
        """
        if self.current < self.n:
            self.current += 2
            return self.current
        else:
            raise StopIteration


# Тестируем наш итератор
even_iterator = EvenIterator2(10)
for i in even_iterator:
    print(i)


txt_file_path = "../data/generator_text.txt"

# Опишем класс итеративного чтения файла

class TxtFileIterator:
    """
    Класс итеративного чтения файла
    """
    def __init__(self, file_path):
        """
        На инициализацию принимает путь к файлу
        :param file_path:
        """
        self.file_path = file_path
        self.file = None

    def __iter__(self):
        """
        Метод __iter__ возвращает сам итератор
        Без него мы не сможем использовать наш итератор в цикле for
        :return:
        """
        return self

    def __next__(self):
        """
        Метод __next__ возвращает следующую строку из файла
        Тут мы явно описываем то, что должен делать наш итератор
        Само возвращаемое значение и условие остановки итератора
        :return:
        """
        if self.file is None:
            self.file = open(self.file_path, "r", encoding="utf8")
        line = self.file.readline()
        if line:
            return line.strip()
        else:
            self.file.close()
            raise StopIteration


# Тестируем наш итератор
txt_file_iterator = TxtFileIterator(txt_file_path)
while True:
    try:
        print(next(txt_file_iterator))
    except StopIteration:
        print("Итератор закончил работу")
        break

