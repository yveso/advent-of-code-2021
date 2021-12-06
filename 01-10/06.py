#%%
with open("./06_input.txt", "r") as file:
    original_fishes = [int(f) for f in file.readline().split(",")]

len(original_fishes)

#%%
days = 80
fishes = original_fishes[:]

for day in range(days):
    next_fishes = []
    count_newborn = 0

    for fish in fishes:
        if fish > 0:
            next_fishes.append(fish - 1)
        else:
            next_fishes.append(6)
            count_newborn += 1

    next_fishes.extend(8 for _ in range(count_newborn))
    fishes = next_fishes

answer_part_one = len(fishes)
answer_part_one

#%%
from collections import Counter

days = 256
counter = Counter(original_fishes)

fishes_by_day = [counter.get(i, 0) for i in range(8, -1, -1)]

for day in range(days):
    zero_day_fishes = fishes_by_day[-1]
    fishes_by_day = [zero_day_fishes] + fishes_by_day[:-1]
    fishes_by_day[2] += zero_day_fishes

answer_part_two = sum(fishes_by_day)
answer_part_two
