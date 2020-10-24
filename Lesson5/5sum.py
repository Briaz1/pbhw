with open('sum.txt', 'w+', encoding='utf-8') as sum_file:
    sum_file.write(input("Enter the numbers separated by a space to count their sum: "))
    sum_file.seek(0)
    i = 0
    for el in sum_file.read().split():
        try:
            i += float(el)
        except ValueError:
            continue
    print(f'Sum of your numbers = {i}.')
