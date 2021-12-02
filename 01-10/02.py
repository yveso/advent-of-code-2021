#%%
with open("./02_input.txt", "r") as file:
    course = [
        (direction, int(ammount))
        for direction, ammount in (
            instruction.split() for instruction in file.readlines()
        )
    ]

course

#%%
depth, horizontal_position = 0, 0

for direction, ammount in course:
    if direction == "down":
        depth += ammount
    elif direction == "up":
        depth -= ammount
    elif direction == "forward":
        horizontal_position += ammount

answer_part_one = depth * horizontal_position
answer_part_one

#%%
depth, horizontal_position, aim = 0, 0, 0

for direction, ammount in course:
    if direction == "down":
        aim += ammount
    elif direction == "up":
        aim -= ammount
    elif direction == "forward":
        horizontal_position += ammount
        depth += aim * ammount

answer_part_two = depth * horizontal_position
answer_part_two
