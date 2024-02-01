from abc import ABC, abstractmethod


class AbstractPalindromeStrategy(ABC):
    """
    Абстрактный класс для стратегий проверки палиндромов
    """
    @abstractmethod
    def is_palindrome(self, text: str) -> bool:
        """
        Метод для проверки палиндрома
        :param text:
        :return: bool
        """
        pass


class SingleWordPalindrome(AbstractPalindromeStrategy):
    """
    Класс для проверки одиночных слов на палиндром
    """
    def is_palindrome(self, text: str) -> bool:
        """
        Метод для проверки одиночных слов на палиндром
        :param text:
        :return: bool
        """
        return text.lower() == text[::-1].lower()


class MultiWordPalindrome(AbstractPalindromeStrategy):
    """
    Класс для проверки многословных выражений на палиндром
    """
    def is_palindrome(self, text: str) -> bool:
        """
        Метод для проверки многословных выражений на палиндром
        :param text:
        :return: bool
        """
        row_string = text.lower().replace(' ', '')
        return row_string == row_string[::-1]


class PalindromeContext:
    """
    Класс для проверки палиндромов
    """
    def __init__(self):
        """
        Конструктор класса
        :param strategy:
        """
        self.strategy = None

    def set_strategy(self, strategy: AbstractPalindromeStrategy):
        """
        Метод для установки стратегии
        :param strategy:
        :return:
        """
        self.strategy = strategy

    def check(self, text: str) -> bool:
        """
        Метод для проверки палиндрома
        :param text:
        :return: bool
        """
        return self.strategy.is_palindrome(text)


class PalindromeFacade:
    """
    Класс для проверки палиндромов.
    Именно с ним будет взаимодействовать пользователь
    """
    def __init__(self):
        """
        Конструктор класса
        """
        self.context = PalindromeContext()

    def check_palindrome(self, text: str) -> bool:
        """
        Метод для проверки палиндрома
        :param text:
        :return: bool
        """
        if ' ' in text:
            self.context.set_strategy(MultiWordPalindrome())
        else:
            self.context.set_strategy(SingleWordPalindrome())
        return self.context.check(text)


def main():
    """
    Функция для проверки работы программы
    :return:
    """
    facade = PalindromeFacade()
    while True:
        text = input('Введите слово или фразу для проверки: ')
        if not text:
            break
        print(f'"{text}" - палиндром: {facade.check_palindrome(text)}')


if __name__ == '__main__':
    main()
