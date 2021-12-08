#%%
with open("./07_input.txt", "r") as file:
    crab_positions = [int(x) for x in file.readline().split(",")]

len(crab_positions)

#%%
from statistics import median

answer_part_one = int(
    sum(abs(crab_position - median(crab_positions)) for crab_position in crab_positions)
)
answer_part_one

#%%
def single_costs(distance):
    """Carl Friedrich to the rescue!"""
    return distance * (distance + 1) / 2


def total_costs(position):
    return sum(
        single_costs(abs(crab_position - position)) for crab_position in crab_positions
    )


minimal_costs = total_costs(0)

for i in range(1, max(crab_positions) + 1):
    current_costs = total_costs(i)
    if current_costs < minimal_costs:
        minimal_costs = current_costs

answer_part_two = int(minimal_costs)
answer_part_two
