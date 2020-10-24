rating_list = [5000, 3500, 2000, 1000, 500, 100, 50, 20, 10, 5, 1]  # Реализация через цикл и ветвления
old_rating_list = rating_list.copy()  # Сохраняем копию для вывода результатов.
user_num = int(input("Enter the number to add to the rating: "))
while user_num < 0:  # Защита от дурака
    user_num = int(input("Enter the number to add to the rating: "))
for number in rating_list:
    if user_num > number:
        rating_list.insert(rating_list.index(number), user_num)
        break
    elif user_num <= rating_list[-1]:  # Поскольку предыдущее условие не сработает только последнем элементе списка
        rating_list.append(user_num)  # меньше вводимого - делаем для него отдельное условие
        break
print(f"Old rating: {old_rating_list}!\nNew rating: {rating_list}!")

# rating_list = [5000, 3500, 2000, 1000, 500, 100, 50, 20, 10, 5, 1,   # Реализация через .sort() и reverse
#                int(input("Enter the number to add to the rating: "))]
# old_rating_list = rating_list.copy()   # Сохраняем копию для вывода результатов.
# old_rating_list.pop(-1)
# while rating_list[-1] < 0:   # Защита от дурака
#     rating_list = [5000, 3500, 2000, 1000, 500, 100, 50, 20, 10, 5, 1,
#                    int(input("Enter the number > 0 to add to the rating: "))]
# rating_list.sort(key=None, reverse=True)   # Сортируем список со значение reverse=True
# print(f"Old rating: {old_rating_list}!\nNew rating: {rating_list}!")
