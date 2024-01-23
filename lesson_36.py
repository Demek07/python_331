"""
Lesson 36
23.01.2024
Паттерны поведения
- Strategy (стратегия)
"""


class Strategy:
    def execute(self, data):
        raise NotImplementedError


class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return sum(data)


class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return max(data)


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        return self._strategy.execute(data)


# Пример использования
data = [1, 2, 3, 4, 5]
context = Context(ConcreteStrategyA())
result = context.execute_strategy(data)
print("Результат ConcreteStrategyA:", result)

context.set_strategy(ConcreteStrategyB())
result = context.execute_strategy(data)
print("Результат ConcreteStrategyB:", result)


class DatabaseStrategy:
    def connect(self):
        raise NotImplementedError


class SqlDatabaseStrategy(DatabaseStrategy):
    def connect(self):
        return "Подключение к SQL базе данных"


class NoSqlDatabaseStrategy(DatabaseStrategy):
    def connect(self):
        return "Подключение к NoSQL базе данных"


class DatabaseContext:
    def __init__(self, strategy: DatabaseStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: DatabaseStrategy):
        self._strategy = strategy

    def connect_to_database(self):
        return self._strategy.connect()


# Пример использования
context = DatabaseContext(SqlDatabaseStrategy())
result = context.connect_to_database()
print(result)

context.set_strategy(NoSqlDatabaseStrategy())
result = context.connect_to_database()
print(result)
