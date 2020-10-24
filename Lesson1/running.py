start = float(input("How many kilometers are you running today?: "))
goal = float(input("How many kilometers do you want to run?: "))
days = 1
while start < goal:
    start += 0.1 * start
    days += 1
print(f"You will run at least {goal:.1f} kilometers on day {days}!")
