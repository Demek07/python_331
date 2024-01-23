"""
Lesson 36
23.01.2024
Паттерны поведения
- Strategy (стратегия)
- Observer (наблюдатель)
"""


class EventListener:
    """
    Абстрактный интерфейс слушателя событий
    """

    def notify(self, event):
        raise NotImplementedError


class EmailAlertListener(EventListener):
    """
    Слушатель событий, который отправляет уведомления на электронную почту
    """

    def notify(self, event):
        print(f"Отправка уведомления на электронную почту: {event}")


class LoggingListener(EventListener):
    """
    Слушатель событий, который логирует события
    """

    def notify(self, event):
        print(f"Логирование события: {event}")


class TelegramAlertListener(EventListener):
    """
    Слушатель событий, который отправляет уведомления в телеграм
    """

    def notify(self, event):
        print(f"Отправка уведомления в телеграм: {event}")


class EventManager:
    """
    Менеджер событий
    """

    def __init__(self):
        self.listeners = []

    def subscribe(self, listener):
        """
        Подписывает слушателя на события
        :param listener:
        :return:
        """
        self.listeners.append(listener)

    def unsubscribe(self, listener):
        """
        Отписывает слушателя от событий
        :param listener:
        :return:
        """
        self.listeners.remove(listener)

    def notify(self, event):
        """
        Уведомляет всех подписчиков о событии
        :param event:
        :return:
        """
        [listener.notify(event) for listener in self.listeners]


# Пример использования
event_manager = EventManager()  # создаем экземпляр менеджера событий для управления подписками
email_listener = EmailAlertListener()  # создаем слушателя событий для отправки уведомлений на почту
logging_listener = LoggingListener()  # создаем слушателя событий для логирования событий
telegram_listener = TelegramAlertListener()  # создаем слушателя событий для отправки уведомлений в телеграм

event_manager.subscribe(email_listener)  # подписываем слушателя на события
event_manager.subscribe(logging_listener)  # подписываем слушателя на события
event_manager.subscribe(telegram_listener)  # подписываем слушателя на события

event_manager.notify("Пользователь вошел в систему")  # отправляем событие всем подписчикам

event_manager.unsubscribe(email_listener)  # отписываем слушателя от событий
event_manager.notify("Пользователь вышел из системы")  # отправляем событие всем подписчикам


# Абстрактный пример
class Observer:
    def update(self, message):
        raise NotImplementedError


class ConcreteObserverA(Observer):
    def update(self, message):
        print(f"ConcreteObserverA получил {message}")


class ConcreteObserverB(Observer):
    def update(self, message):
        print(f"ConcreteObserverB получил {message}")


class Subject:
    def __init__(self):
        self._observers = []

    def register(self, observer):
        self._observers.append(observer)

    def unregister(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


# Пример использования
subject = Subject()
observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()

subject.register(observer_a)
subject.register(observer_b)
subject.notify_observers("Событие 1")

subject.unregister(observer_a)
subject.notify_observers("Событие 2")
