#%%
from dataclasses import dataclass


@dataclass
class Vent:
    x1: int
    y1: int
    x2: int
    y2: int


with open("./05_input.txt", "r") as file:
    lines = [line.rstrip().split(" -> ") for line in file.readlines()]

vents = []
for line in lines:
    one, two = line
    x1, y1 = one.split(",")
    x2, y2 = two.split(",")
    vents.append(Vent(int(x1), int(y1), int(x2), int(y2)))

len(vents)

#%%
non_diagonal_vents = [
    vent for vent in vents if (vent.x1 == vent.x2 or vent.y1 == vent.y2)
]

map = {}
for vent in non_diagonal_vents:
    # vertical
    if vent.x1 == vent.x2:
        x = vent.x1
        for y in range(min(vent.y1, vent.y2), max(vent.y1, vent.y2) + 1):
            if (x, y) in map:
                map[(x, y)] += 1
            else:
                map[(x, y)] = 1

    # horizontal
    else:
        y = vent.y1
        for x in range(min(vent.x1, vent.x2), max(vent.x1, vent.x2) + 1):
            if (x, y) in map:
                map[(x, y)] += 1
            else:
                map[(x, y)] = 1

answer_part_one = sum(1 for v in map.values() if v > 1)
answer_part_one

#%%
map = {}
for vent in vents:
    # vertical
    if vent.x1 == vent.x2:
        x = vent.x1
        for y in range(min(vent.y1, vent.y2), max(vent.y1, vent.y2) + 1):
            if (x, y) in map:
                map[(x, y)] += 1
            else:
                map[(x, y)] = 1

    # horizontal
    elif vent.y1 == vent.y2:
        y = vent.y1
        for x in range(min(vent.x1, vent.x2), max(vent.x1, vent.x2) + 1):
            if (x, y) in map:
                map[(x, y)] += 1
            else:
                map[(x, y)] = 1

    # diagonal left to right
    elif vent.x1 < vent.x2:
        x, y = vent.x1, vent.y1
        for _ in range(vent.x2 - vent.x1 + 1):

            if (x, y) in map:
                map[(x, y)] += 1
            else:
                map[(x, y)] = 1
            x += 1
            y += 1 if vent.y1 < vent.y2 else -1

    # diagonal right to left
    elif vent.x1 > vent.x2:
        x, y = vent.x1, vent.y1
        for _ in range(vent.x1 - vent.x2 + 1):
            if (x, y) in map:
                map[(x, y)] += 1
            else:
                map[(x, y)] = 1
            x -= 1
            y += 1 if vent.y1 < vent.y2 else -1

answer_part_two = sum(1 for v in map.values() if v > 1)
answer_part_two
