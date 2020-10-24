def sum_func():
    total_sum = 0
    while True:
        sum_list = input("Input any numbers separated by space to sum it. To exit enter 'Q': ").lower()
        sum_list = sum_list.split()

        for i, item in enumerate(sum_list):
            if item == 'Q'.lower():
                while i < len(sum_list):
                    sum_list.pop(i)
                return f"New sum = {sum(sum_list)}. Total sum = {total_sum + sum(sum_list)}."
            else:
                try:
                    sum_list[i] = int(item)   # Мария, прокомментируйте пожалуйста почему тут warning
                except ValueError:
                    sum_list.remove(item)
                    sum_list.insert(i, 0)  # и тут week warning
        print(f" New sum = {sum(sum_list)}. Total sum = {total_sum + sum(sum_list)}.")
        total_sum = total_sum + sum(sum_list)   # и оказывается через isdigit было проще, но пусть уже так будет :D


print(sum_func())
