def factorial(n):
    f = 1
    if n == 0:
        yield f"{el}! = {f}."
    else:
        for el in range(1, n + 1):
            f *= el
            yield f"{el}! = {f}."


while True:
    try:
        for i in factorial(int(input("Enter a number to calculate its factorial: "))):
            print(i)
        break
    except ValueError:
        continue
