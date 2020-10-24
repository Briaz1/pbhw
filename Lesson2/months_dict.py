months_by_seasons = {   # Создаём словарь, где времена года ключи, а месяцы значения
    "Winter": [12, 1, 2],
    "Spring": [3, 4, 5],
    "Summer": [6, 7, 8],
    "Autumn": [9, 10, 11]
}
user_answer = int(input("Enter the number of the month to find out its season: "))
while user_answer > 12 or user_answer < 1:  # Защита от дурака
    user_answer = int(input("Pls enter a number from 1 to 12! "))

for season in months_by_seasons:
    if user_answer in months_by_seasons[season]:   # Сканируем словарь на соответствие
        print(f"{user_answer} month is {season}!")
        break   # Чтобы цикл перестал работать после первого совпадения
