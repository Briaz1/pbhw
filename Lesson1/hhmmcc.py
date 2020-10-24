user_time = int(input("Enter the number of seconds you want to convert to format hh:mm:cc - "))
hours = user_time // 3600
minutes = (user_time - 3600 * hours) // 60
seconds = user_time % 60

if user_time <= 86400:
    print(f"{user_time} seconds = {hours:02}:{minutes:02}:{seconds:02}")
else:
    print("Please enter a number less or equal 86400!")
