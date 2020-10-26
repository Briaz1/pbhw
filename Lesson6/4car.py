class Car:

    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color

    def go(self):
        return f'{self.name} start.'

    def stop(self):
        return f'\n{self.name} has stopped.'

    def turn(self, direction):
        return f'\n{self.name} turned {direction}.'

    def show_speed(self):
        return f'\nYour speed is {self.speed}.'


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police=True):
        super().__init__(name, speed, color)
        self.is_police = is_police


class SportCar(Car):
    def __init__(self, name, speed, color, is_police=False):
        super().__init__(name, speed, color)
        self.is_police = is_police


class TownCar(Car):
    def __init__(self, name, speed, color, is_police=False):
        super().__init__(name, speed, color)
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 60:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}.'
        else:
            return f'Your speed is {self.speed}.'


class WorkCar(Car):
    def __init__(self, name, speed, color, is_police=False):
        super().__init__(name, speed, color)
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 40:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}.'
        else:
            return f'Your speed is {self.speed}.'


town = TownCar('BMW 320', 70, 'yellow')
print(f'1:\nModel - {town.name}, speed - {town.speed}, color - {town.color}, is police - {town.is_police}.')
print(town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('Lexus LC', 170, 'red')
print(f'2:\nModel - {sport.name}, speed - {sport.speed}, color - {sport.color}, is police - {sport.is_police}.')
print(sport.go(), sport.show_speed(), sport.turn('right'), sport.stop())

work = WorkCar('WV Polo', 30, 'black')
print(f'3:\nModel - {work.name}, speed - {work.speed}, color - {work.color}, is police - {work.is_police}.')
print(work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar('Police_Ford', 100, 'blue')
print(f'4:\nModel - {police.name}, speed - {police.speed}, color - {police.color}, is police - {police.is_police}.')
print(police.go(), police.show_speed(), police.turn('left'), police.stop())
