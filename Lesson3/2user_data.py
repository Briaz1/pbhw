"""Решение через f-строку"""


def user_data_func(name, surname, city, date_of_birth, email, phone):
    return f"name - {name}, surname - {surname}, city - {city}, " \
           f"date_of_birth - {date_of_birth}, email - {email}, phone number - {phone}.".title()


"""Решение через kwargs"""


# def user_data_func(**kwargs):
#     return ' '(kwargs.values())


user_data = user_data_func(name=input("Enter your name: "), surname=input("Enter your surname: "),
                           city=input("Enter your city: "), date_of_birth=input("Enter your date of birth: "),
                           email=input("Enter your email: "), phone=input("Enter your phone number: "))
print(user_data)
