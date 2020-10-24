def div_func(a, b):
    try:
        f"{a} / {b}"
        return f"{a} / {b} = {a / b:.3}"
    except ZeroDivisionError:
        while b == 0:
            b = int(input("Input divider(not 0): "))
        return f"{a} / {b} = {a / b:.3}."


print(div_func(float(input("Input dividend: ")), float(input("Input divider: "))))
