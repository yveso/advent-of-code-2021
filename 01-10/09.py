#%%
with open("./09_input.txt", "r") as file:
    height_map = []
    lines = file.readlines()
    for row in lines:
        height_map.append([int(d) for d in row if d.isdigit()])

f"{len(height_map)=} x {len(height_map[0])=}"

#%%
low_points = []

for y, row in enumerate(height_map):
    for x, height in enumerate(row):
        adjacent_locations = []
        if y == 0 or y == len(height_map) - 1 or x == 0 or x == len(row) - 1:
            if y != 0:
                # has top
                adjacent_locations.append(height_map[y - 1][x])
            if y != len(height_map) - 1:
                # has bottom
                adjacent_locations.append(height_map[y + 1][x])
            if x != 0:
                # has left
                adjacent_locations.append(height_map[y][x - 1])
            if x != len(row) - 1:
                # has right
                adjacent_locations.append(height_map[y][x + 1])

        else:
            adjacent_locations.extend(
                [
                    height_map[y - 1][x],
                    height_map[y + 1][x],
                    height_map[y][x - 1],
                    height_map[y][x + 1],
                ]
            )

        if all(height < adj_loc for adj_loc in adjacent_locations):
            low_points.append(height)

answer_part_one = sum(1 + low_point for low_point in low_points)
answer_part_one

#%%
basin_sizes = []

for y, row in enumerate(height_map):
    for x, height in enumerate(row):
        adjacent_locations = []
        if y == 0 or y == len(height_map) - 1 or x == 0 or x == len(row) - 1:
            if y != 0:
                # has top
                adjacent_locations.append(height_map[y - 1][x])
            if y != len(height_map) - 1:
                # has bottom
                adjacent_locations.append(height_map[y + 1][x])
            if x != 0:
                # has left
                adjacent_locations.append(height_map[y][x - 1])
            if x != len(row) - 1:
                # has right
                adjacent_locations.append(height_map[y][x + 1])

        else:
            adjacent_locations.extend(
                [
                    height_map[y - 1][x],
                    height_map[y + 1][x],
                    height_map[y][x - 1],
                    height_map[y][x + 1],
                ]
            )

        if all(height < adj_loc for adj_loc in adjacent_locations):
            # https://de.wikipedia.org/wiki/Floodfill
            stack = [(y, x)]
            bassin = []
            already_visited = set()
            while len(stack) > 0:
                yy, xx = stack.pop()

                if (yy, xx) not in already_visited:
                    bassin.append(height_map[yy][xx])
                    already_visited.add((yy, xx))

                    if yy > 0 and height_map[yy - 1][xx] != 9:
                        stack.append((yy - 1, xx))

                    if yy < len(height_map) - 1 and height_map[yy + 1][xx] != 9:
                        stack.append((yy + 1, xx))

                    if xx > 0 and height_map[yy][xx - 1] != 9:
                        stack.append((yy, xx - 1))

                    if xx < len(height_map[0]) - 1 and height_map[yy][xx + 1] != 9:
                        stack.append((yy, xx + 1))

            basin_sizes.append(len(bassin))

product = 1
for size in sorted(basin_sizes)[-3:]:
    product *= size

answer_part_two = product
answer_part_two
