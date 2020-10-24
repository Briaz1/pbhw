months_by_seasons = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 1]  # Создаём список принадлежности месяцов к временам года
seasons = ["winter", "spring", "summer", "autumn"]  # Создаём список времён года
user_answer = int(input("Enter the number of the month to find out its season: "))

while user_answer > 12 or user_answer < 1:  # Защита от дурака
    user_answer = int(input("Pls enter a number from 1 to 12! "))
print(
    f"{user_answer} month is {seasons[months_by_seasons[user_answer - 1] - 1]}!")
# Обращаемся к списку времён года  с индексом из списка принадлежности
