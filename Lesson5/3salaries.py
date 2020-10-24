from statistics import mean

with open('salaries.txt', 'r', encoding='utf-8') as salaries:
    salaries_list = salaries.read().split('\n')
    surnames = []
    salaries = []
    for emp_data in salaries_list:
        if float(emp_data.split()[1]) < 20000:
            surnames.append(emp_data.split()[0])
        salaries.append(float(emp_data.split()[1]))

print(f'{", ".join(surnames)} have a salary of less than 20,000.')
print(f'Average salary in the company - {round(mean(salaries))} rub.')
