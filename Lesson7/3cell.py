class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        return self.cells

    def __add__(self, other):
        return f'Сумма клеток - {self.cells + other.cells}'

    def __sub__(self, other):
        return f'Разность клеток - {self.cells - other.cells}'

    def __floordiv__(self, other):
        return f'Целочисленное деление клеток - {self.cells // other.cells}'

    def __mul__(self, other):
        return f'Умножение клеток - {self.cells * other.cells}'

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.cells // rows)]) + '\n' + '*' * (self.cells % rows)


cell_1 = Cell(18)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 // cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(4))

# P.S. Очень похоже на вариант из разбора, но делал сам)
