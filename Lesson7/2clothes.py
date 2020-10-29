from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def amount(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def amount(self):
        return self.size / 6.5 + 0.5

    def __str__(self):
        return f'Ткани на пальто нужно {self.amount:.2f}'


class Suit(Clothes):
    def __init__(self, growth):
        self.growth = growth

    @property
    def amount(self):
        return self.growth * 2 + 0.3

    def __str__(self):
        return f'Ткани на костюм нужно {self.amount:.2f}'


c = Coat(float(input('Укажите размер для расчёта ткани на пальто: ')))
s = Suit(float(input('Укажите рост для расчёта ткани на костюм: ')))
print(c.amount)
print(s)
print(f'Общее количество ткани - {c.amount + s.amount:.2f}')

# P.S. Какие-то странные формулы для расчёта количества ткани)
