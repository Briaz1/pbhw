quantity_of_goods = int(input(
    "Enter the quantity of the goods you want to add to the database: "))  # Выставляем количество наименований в базе
n = 1
product_list = []
product_dict = {}

while n <= quantity_of_goods:
    product_dict = {'name': input(f"Enter {n} product name: "),   # Заполняем информацию о каждом товаре
                    'price': int(input(f"Enter {n} product price: ")),
                    'quantity': int(input(f"Enter {n} product quantity: ")),
                    'unit': input(f"Enter {n} product unit: ")
                    }
    product_list.append((n, product_dict))   # Добавляем каждый товар со значениями в список
    n += 1

analytics = {}
for product in product_list:   # Создаём список для аналитики
    for key, value in product[1].items():
        if key in analytics:
            analytics[key].append(value)
        else:
            analytics[key] = [value]
menu = input(   # Создаём меню для управления базой данных
    "To view the list of products Enter 'P'! To view analytics enter 'A'! To quit enter 'Q': ").upper()
while True:
    if menu == 'P':
        print("Product_list:")
        print(*product_list, sep="\n")
        menu = input("To view the list of products Enter 'P'! To view analytics enter 'A'! To quit enter 'Q': ").upper()
    elif menu == 'A':
        print("Analytics_list:")
        for key, value in analytics.items():
            print(f"{key} - {value}")
        menu = input("To view the list of products Enter 'P'! To view analytics enter 'A'! To quit enter 'Q': ").upper()
    elif menu == 'Q':
        print("Thanks for use our Database!")
        break
    else:
        menu = input("To view the list of products Enter 'P'! To view analytics enter 'A'! To quit enter 'Q': ").upper()
