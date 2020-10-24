def degree_func(x, y, n=1):
    if x > 0 > y:
        value = x
        while n < abs(y):
            value = value * x
            n += 1
        return f"{x} in {y} degree = {1 / value:.3}"
    elif x < 0 or y > 0:
        while x < 0:
            x = float(input("Enter the positive exponential number!: "))
        while y > 0:
            y = int(input("Enter a negative integer degree value!: "))
        value = x
        while n < abs(y):
            value = value * x
            n += 1
        return f"{x} in {y} degree = {1 / value:.3}"


while True:
    try:
        print(degree_func(float(input("Enter the positive exponential number: ")),
                          int(input("Enter a negative integer degree value: "))))
        break
    except ValueError:
        continue
