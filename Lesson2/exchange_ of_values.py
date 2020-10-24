user_list = list(input("Please enter a set of symbols to the list: "))
while user_list.count(" ") > 0:  # Удаляем пробелы, если пользователь их ввёл
    user_list.remove(" ")
old_list = user_list.copy()
last_index = len(user_list) if len(user_list) % 2 == 0 else len(
    user_list) - 1  # защищаем последнее число при нечётной длине
for i in range(0, last_index - 1, 2):
    user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
print(f"Old list - {old_list}. New list - {user_list}")
