#%%
from collections import namedtuple
import pathlib

Cube = namedtuple("Cube", "state x y z")

cubes = []
with open(pathlib.Path(__file__).parent / "22_input.txt", "r") as file:
    for line in file.readlines():
        state, coords = line.rstrip().split(" ")
        state = state == "on"
        coords = coords.split(",")
        coords = [c[2:].split("..") for c in coords]
        coords = [(int(a), int(b)) for a, b in coords]
        cubes.append(Cube(state=state, x=coords[0], y=coords[1], z=coords[2]))

len(cubes)

#%%
reactor = set()
region_start, region_end = -50, 50

for cube in cubes:
    for x in range(max(cube.x[0], region_start), min(cube.x[1], region_end) + 1):
        for y in range(max(cube.y[0], region_start), min(cube.y[1], region_end) + 1):
            for z in range(
                max(cube.z[0], region_start),
                min(cube.z[1], region_end) + 1,
            ):
                if cube.state:
                    reactor.add((x, y, z))
                else:
                    if (x, y, z) in reactor:
                        reactor.remove((x, y, z))

answer_part_one = len(reactor)
answer_part_one
