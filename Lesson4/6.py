from itertools import count, cycle

count_gen = count(1)
count_list = [next(count_gen) for el in range(10)]
print(f"Generated sequence - {count_list}")

cycle_gen = cycle(count_list)
print(f"Generated sequence - {[next(cycle_gen) for i in range(30)]}")
