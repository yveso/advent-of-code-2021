#%%
def get_neighbour_stack(y, x, height, width):
    stack = []

    if y > 0:
        if x > 0:
            stack.append((y - 1, x - 1))
        stack.append((y - 1, x))
        if x < width - 1:
            stack.append((y - 1, x + 1))
    if x > 0:
        stack.append((y, x - 1))
    if x < width - 1:
        stack.append((y, x + 1))
    if y < height - 1:
        if x > 0:
            stack.append((y + 1, x - 1))
        stack.append((y + 1, x))
        if x < width - 1:
            stack.append((y + 1, x + 1))

    return stack


with open("./11_input.txt", "r") as file:
    lines = [line.rstrip() for line in file.readlines()]
    original_octopuses = []
    for line in lines:
        original_octopuses.append([int(level) for level in line if level.isdigit()])

height, width = len(original_octopuses), len(original_octopuses[0])

original_octopuses

#%%
count_steps = 100
octopuses = [row[:] for row in original_octopuses]
count_flashes = 0

for step in range(count_steps):
    for y, row in enumerate(octopuses):
        for x, level in enumerate(row):
            octopuses[y][x] += 1

    flashed_octopuses_in_step = set()
    octo_stack = []
    for y, row in enumerate(octopuses):
        for x, level in enumerate(row):
            if level > 9 and (y, x) not in flashed_octopuses_in_step:

                flashed_octopuses_in_step.add((y, x))
                octo_stack.extend(get_neighbour_stack(y, x, height, width))
                while len(octo_stack) > 0:
                    yy, xx = octo_stack.pop()
                    octopuses[yy][xx] += 1
                    if (
                        octopuses[yy][xx] > 9
                        and (yy, xx) not in flashed_octopuses_in_step
                    ):
                        flashed_octopuses_in_step.add((yy, xx))
                        octo_stack.extend(get_neighbour_stack(yy, xx, height, width))

    for y, x in flashed_octopuses_in_step:
        octopuses[y][x] = 0
    count_flashes += len(flashed_octopuses_in_step)


answer_part_one = count_flashes
answer_part_one

#%%
count_steps = 0
octopuses = [row[:] for row in original_octopuses]

while True:
    count_steps += 1
    for y, row in enumerate(octopuses):
        for x, level in enumerate(row):
            octopuses[y][x] += 1

    flashed_octopuses_in_step = set()
    octo_stack = []
    for y, row in enumerate(octopuses):
        for x, level in enumerate(row):
            if level > 9 and (y, x) not in flashed_octopuses_in_step:

                flashed_octopuses_in_step.add((y, x))
                octo_stack.extend(get_neighbour_stack(y, x, height, width))
                while len(octo_stack) > 0:
                    yy, xx = octo_stack.pop()
                    octopuses[yy][xx] += 1
                    if (
                        octopuses[yy][xx] > 9
                        and (yy, xx) not in flashed_octopuses_in_step
                    ):
                        flashed_octopuses_in_step.add((yy, xx))
                        octo_stack.extend(get_neighbour_stack(yy, xx, height, width))

    for y, x in flashed_octopuses_in_step:
        octopuses[y][x] = 0

    if len(flashed_octopuses_in_step) == (width * height):
        break


answer_part_two = count_steps
answer_part_two
