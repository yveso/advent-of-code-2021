#%%
with open("./15_input.txt", "r") as file:
    cavern = {}
    for y, line in enumerate(file.readlines()):
        for x, risk_level in enumerate(line.rstrip()):
            cavern[(x, y)] = int(risk_level)

start = min(cavern.keys())
end = max(cavern.keys())

start, end

#%%
import heapq


def get_neighbours(location, width, height):
    neighbours = []
    x, y = location
    if x > 0:
        neighbours.append((location[0] - 1, location[1]))
    if x <= width - 1:
        neighbours.append((location[0] + 1, location[1]))
    if y > 0:
        neighbours.append((location[0], location[1] - 1))
    if y <= height - 1:
        neighbours.append((location[0], location[1] + 1))

    return neighbours


def find_smallest_risk(cavern, start, end):
    routes = []
    risk_map = {start: 0}
    heapq.heappush(routes, (0, start))

    while len(routes) > 0:
        current_risk, current_location = heapq.heappop(routes)
        for neighbour in get_neighbours(current_location, end[0], end[1]):
            new_risk = current_risk + cavern[neighbour]
            if neighbour not in risk_map or new_risk < risk_map[neighbour]:
                risk_map[neighbour] = new_risk
                heapq.heappush(routes, (new_risk, neighbour))
    return risk_map


#%%
risks = find_smallest_risk(cavern, start, end)
answer_part_one = risks[end]
answer_part_one

#%%
# 🥴🥴🥴
big_cavern = {}
for x_factor in range(5):
    for y_factor in range(5):
        for location in cavern.keys():
            risk = cavern[location] + x_factor + y_factor
            big_cavern[
                (
                    x_factor * (end[0] + 1) + location[0],
                    y_factor * (end[1] + 1) + location[1],
                )
            ] = (
                risk if risk < 10 else risk - 9
            )

big_cavern_end = max(big_cavern)

risks = find_smallest_risk(big_cavern, start, big_cavern_end)
answer_part_two = risks[big_cavern_end]
answer_part_two
