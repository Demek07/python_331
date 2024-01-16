"""
Lesson 34
16.01.2024

- Паттерны проектирования (Порождающие паттерны)
- Singleton
- Builder
- Abstract Factory
- Factory Method
"""


# Factory Method - порождающий паттерн проектирования, который позволяет создавать
# объекты без указания конкретных классов

class Product:
    def show_info(self):
        pass


class ConcreteProductA(Product):
    def show_info(self):
        return "Product A"


class ConcreteProductB(Product):
    def show_info(self):
        return "Product B"


class Creator:
    def factory_method(self):
        pass


class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()


# Использование фабричного метода
creator_a = ConcreteCreatorA()
product_a = creator_a.factory_method()
print(product_a.show_info())

creator_b = ConcreteCreatorB()
product_b = creator_b.factory_method()
print(product_b.show_info())


# Пример приближенный к реальности
# Представим, что у нас есть интернет-магазин, который принимает платежи через PayPal и Stripe
# Нам нужно реализовать логику обработки платежей через эти два сервиса

class PaymentGateway:
    def process_payment(self, amount):
        pass


class PayPalPaymentGateway(PaymentGateway):
    def process_payment(self, amount):
        # Здесь бы происходила логика обработки платежа через PayPal API
        return f"Payment of ${amount} processed via PayPal"


class StripePaymentGateway(PaymentGateway):
    def process_payment(self, amount):
        # Здесь бы происходила логика обработки платежа через Stripe API
        return f"Payment of ${amount} processed via Stripe"


class PaymentGatewayFactory:
    def create_payment_gateway(self, gateway_type):
        pass


class ConcretePaymentGatewayFactory(PaymentGatewayFactory):
    def create_payment_gateway(self, gateway_type):
        if gateway_type == "paypal":
            return PayPalPaymentGateway()
        elif gateway_type == "stripe":
            return StripePaymentGateway()
        else:
            raise ValueError("Unsupported payment gateway")


# Использование фабричного метода
payment_gateway_factory = ConcretePaymentGatewayFactory()
paypal_gateway = payment_gateway_factory.create_payment_gateway("paypal")
stripe_gateway = payment_gateway_factory.create_payment_gateway("stripe")

print(paypal_gateway.process_payment(100))
print(stripe_gateway.process_payment(150))
