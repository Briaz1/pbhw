class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки. Инструмент -  {self.title}.'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки. Инструмент -  {self.title}.'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки. Инструмент -  {self.title}.'


pen = Pen('Ручка')
print(pen.draw())
pencil = Pencil('Карандаш')
print(pencil.draw())
handle = Handle('Маркер')
print(handle.draw())
