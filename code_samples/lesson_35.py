"""
Lesson 35
18.01.2024

- Паттерны проектирования (Структурные паттерны)
- Adapter (адаптер)
- Facade (фасад)
"""

"""
Паттерн "Фасад" в программировании представляет собой структурный шаблон проектирования, цель которого - предоставление
 простого интерфейса к сложной системе классов, библиотеке или фреймворку. Основные задачи фасада:

- **Упрощение интерфейса**: Скрыть сложность системы, предоставляя простой интерфейс для взаимодействия с ней.
- **Уменьшение зависимостей**: Снизить зависимость внешнего кода от множества классов в системе, сосредоточив 
взаимодействие через одну точку доступа.

- **Повышение гибкости**: Облегчить изменение и обновление внутренних компонентов системы, не затрагивая клиентский код.
"""

"""
Давайте рассмотрим пример паттерна "Фасад" в контексте системы онлайн-бронирования отелей. 

В этой системе может быть несколько сложных компонентов, таких как поиск доступных отелей,
 бронирование номеров и управление платежами. Фасад будет упрощать взаимодействие 
 с этими подсистемами для клиентского кода.
"""


# Подсистема 1: Поиск отелей
class HotelBookingSystem:
    @staticmethod
    def search_hotels(self, date_from, date_to, destination):
        return f"Найдены отели в {destination} с {date_from} по {date_to}"


# Подсистема 2: Бронирование отелей
class HotelReservationSystem:
    @staticmethod
    def book_hotel(self, hotel_id, date_from, date_to):
        return f"Отель {hotel_id} забронирован с {date_from} по {date_to}"


# Подсистема 3: Управление платежами
class PaymentSystem:
    @staticmethod
    def process_payment(self, payment_details):
        return "Платеж обработан"


# Фасад: Упрощенный интерфейс для системы бронирования отелей
class HotelBookingFacade:
    def __init__(self):
        self.hotel_booking = HotelBookingSystem()
        self.reservation = HotelReservationSystem()
        self.payment = PaymentSystem()

    def book_hotel_for_vacation(self, date_from, date_to, destination, hotel_id, payment_details):
        available_hotels = self.hotel_booking.search_hotels(date_from, date_to, destination)
        print(available_hotels)

        reservation_details = self.reservation.book_hotel(hotel_id, date_from, date_to)
        print(reservation_details)

        payment_confirmation = self.payment.process_payment(payment_details)
        print(payment_confirmation)

        return "Отпуск успешно забронирован!"


# Клиентский код
facade = HotelBookingFacade()
vacation = facade.book_hotel_for_vacation("2021-12-24", "2021-12-31", "Майами", "Hotel123", "Visa 1234")
print(vacation)


