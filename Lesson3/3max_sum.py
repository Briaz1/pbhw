"""Решение через min"""


def sum_func(a, b, c):
    return f"Sum of two maximum numbers = {a + b + c - min(a, b, c)}."


"""Альтернативное решение через min"""


# def sum_func(a, b, c):
#     s = [a, b, c]
#     s.remove(min(a, b, c))
#     return f"Sum of two maximum numbers = {s[0] + s[1]}."


"""Решение через sort"""


# def sum_func(a, b, c):
#     s = [a, b, c]
#     s.sort(key=None, reverse=True)
#     return f"Sum of two maximum numbers = {s[0] + s[1]}."


print(sum_func(int(input("Enter 1 number: ")), int(input("Enter 2 number: ")), int(input("Enter 3 number: "))))
