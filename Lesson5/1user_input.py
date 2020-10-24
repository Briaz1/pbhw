with open('user_data.txt', 'a', encoding='utf-8') as user_data:
    while True:
        user_input = user_data.write(f"{input(f'Enter string to save in user_data.txt. Just press enter to exit: ')}\n")
        if user_input == 1:
            break
