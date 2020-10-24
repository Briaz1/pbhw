user_str = input("Enter any words separated by spaces: ").split()   # Превращаем введённые слова в список
for num, word in enumerate(user_str, 1):
    print(num, word[:10])
