"""
Lesson 36
23.01.2024
Паттерны поведения
- Strategy (стратегия)
- Observer (наблюдатель)
- Command (команда)
- State (состояние)
- Пример взаимодействия паттернов Command + Strategy
"""


class TrafficLightState:
    """ Абстрактный класс, описывающий состояние светофора """

    def change(self, traffic_light):
        pass

    def status(self):
        pass


class RedLight(TrafficLightState):
    """ Конкретное состояние: Красный свет """

    def change(self, traffic_light):
        traffic_light.state = traffic_light.green

    def status(self):
        return "Красный свет"


class YellowLight(TrafficLightState):
    """ Конкретное состояние: Желтый свет """

    def change(self, traffic_light):
        traffic_light.state = traffic_light.red

    def status(self):
        return "Желтый свет"


class GreenLight(TrafficLightState):
    """ Конкретное состояние: Зеленый свет """

    def change(self, traffic_light):
        traffic_light.state = traffic_light.yellow

    def status(self):
        return "Зеленый свет"


class TrafficLight:
    """ Контекст, управляющий состояниями светофора """

    def __init__(self):
        self.red = RedLight()
        self.yellow = YellowLight()
        self.green = GreenLight()
        self.state = self.red  # Начальное состояние - красный

    def change(self):
        self.state.change(self)

    def status(self):
        return self.state.status()


# Клиентский код
traffic_light = TrafficLight()

print(traffic_light.status())  # Красный свет
traffic_light.change()
print(traffic_light.status())  # Зеленый свет
traffic_light.change()
print(traffic_light.status())  # Желтый свет


class PlayerState:
    """ Абстрактный класс для состояний плеера """

    def click_play(self, player):
        pass

    def click_stop(self, player):
        pass

    def click_pause(self, player):
        pass


class PlayingState(PlayerState):
    """ Состояние 'Играет' """

    def click_play(self, player):
        print("Музыка уже играет")

    def click_stop(self, player):
        print("Остановка музыки")
        player.state = player.stopped

    def click_pause(self, player):
        print("Музыка на паузе")
        player.state = player.paused


class StoppedState(PlayerState):
    """ Состояние 'Остановлен' """

    def click_play(self, player):
        print("Воспроизведение музыки")
        player.state = player.playing

    def click_stop(self, player):
        print("Музыка уже остановлена")


class PausedState(PlayerState):
    """ Состояние 'На паузе' """

    def click_play(self, player):
        print("Воспроизведение музыки")
        player.state = player.playing

    def click_stop(self, player):
        print("Остановка музыки")
        player.state = player.stopped


class MusicPlayer:
    """ Контекст, управляющий состояниями плеера """

    def __init__(self):
        self.playing = PlayingState()
        self.stopped = StoppedState()
        self.paused = PausedState()
        self.state = self.stopped  # Начальное состояние - остановлен

    def click_play(self):
        self.state.click_play(self)

    def click_stop(self):
        self.state.click_stop(self)

    def click_pause(self):
        self.state.click_pause(self)


# Клиентский код
player = MusicPlayer()

player.click_play()  # Воспроизведение музыки
player.click_pause()  # Музыка на паузе
player.click_play()  # Воспроизведение музыки
player.click_stop()  # Остановка музыки
