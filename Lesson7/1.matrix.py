class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        out = []
        for row in self.matrix:
            out.append(' '.join([str(_) for _ in row]))
        return '\n'.join(out)

    def __add__(self, other):
        for el in range(len(self.matrix)):
            for number in range(len(self.matrix[el])):
                self.matrix[el][number] = (self.matrix[el][number] + other.matrix[el][number])
        return Matrix(self.matrix)


m_1 = Matrix([[11, 22], [33, 44], [55, 66]])
m_2 = Matrix([[77, 88], [99, 101], [111, 122]])
print(m_1 + m_2)
