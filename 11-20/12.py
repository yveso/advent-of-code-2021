#%%
def is_route_in_stack(route, stack):
    for r in stack:
        if len(r) == len(route) and all(a == b for a, b in zip(r, route)):
            return True
    return False


with open("./12_input.txt", "r") as file:
    connections = [line.rstrip().split("-") for line in file.readlines()]

connections

#%%
stack = [["start"]]
paths = []

while len(stack) > 0:
    route = stack.pop()
    current_cave = route[-1]
    for connection in connections:
        if current_cave in connection:
            next_cave = (
                connection[1] if connection[0] == current_cave else connection[0]
            )
            if (next_cave.islower() and next_cave not in route) or (
                next_cave.isupper()
            ):
                new_route = route + [next_cave]
                if next_cave == "end":
                    paths.append(new_route)
                elif not is_route_in_stack(new_route, stack):
                    stack.append(new_route)


answer_part_one = len(paths)
answer_part_one

#%%
stack = [["start"]]
paths = []

small_caves = set(
    [
        conn[0]
        for conn in connections
        if conn[0].islower() and conn[0] not in ["start", "end"]
    ]
    + [
        conn[1]
        for conn in connections
        if conn[1].islower() and conn[1] not in ["start", "end"]
    ]
)

# Not really fast... 🥴
while len(stack) > 0:
    route = stack.pop()
    current_cave = route[-1]
    for connection in connections:
        if current_cave in connection:
            next_cave = (
                connection[1] if connection[0] == current_cave else connection[0]
            )
            if next_cave == "start":
                continue

            small_cave_counts_greater_than_one = [
                route.count(c) for c in small_caves if route.count(c) > 1
            ]
            if (
                next_cave.islower()
                and (
                    len(small_cave_counts_greater_than_one) == 0
                    or (
                        len(small_cave_counts_greater_than_one) == 1
                        and max(small_cave_counts_greater_than_one) == 2
                    )
                )
            ) or (next_cave.isupper()):
                new_route = route + [next_cave]
                if next_cave == "end":
                    paths.append(new_route)
                elif not is_route_in_stack(new_route, stack):
                    stack.append(new_route)

answer_part_two = len(paths)
answer_part_two
