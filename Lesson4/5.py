from functools import reduce


def multiplication(prev_el, el):
    return prev_el * el


print(reduce(multiplication, [el for el in range(100, 1001, 2)]))
