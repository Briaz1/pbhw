from sys import argv

name, working_out, rate, prize = argv
print(argv)
print(f"Wage = {working_out} * {rate} + {prize} = {int(working_out) * int(rate) + int(prize)}")
