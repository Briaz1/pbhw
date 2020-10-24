revenue = int(input("Enter your company's revenue: "))
costs = int(input("Enter your company's costs: "))

if revenue > costs:
    profit = revenue - costs
    profitability = profit / revenue
    print(f"Your company's profit {profit} euro!")
    print(f"Your company's profit to revenue ratio {profitability:.2f}")
    numbers_employee = int(input("Enter the number of employees in your company: "))
    employee_profit = profit / numbers_employee
    print(f"Each employee brought your company {employee_profit:.2f} euro.")
elif revenue < costs:
    profit = costs - revenue
    print(f"Your company's losses {profit} euro!")
elif revenue == costs:
    print("Your company's revenue and costs are equal!")
