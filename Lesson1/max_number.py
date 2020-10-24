user_number = int(input("Please enter a positive integer: "))
max_number = user_number % 10
user_number = user_number // 10

while user_number > 0:
    if max_number < user_number % 10:
        max_number = user_number % 10
    user_number = user_number // 10
print(f"The largest digit of the entered number - {max_number}!")
