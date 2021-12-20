#%%
import pathlib

with open(pathlib.Path(__file__).parent / "17_input.txt", "r") as file:
    line = file.readline().rstrip()

line = line[len("target area: x=") :]
x_part, y_part = line.split(", y=")
target_start_x, target_end_x = [int(x) for x in x_part.split("..")]
target_end_y, target_start_y = [int(y) for y in y_part.split("..")]

target_start_x, target_end_x, target_start_y, target_end_y

#%%
# 🤯
answer_part_one = target_end_y * (target_end_y + 1) // 2
answer_part_one

#%%
def launch_probe(velocity):
    position_x, position_y = 0, 0
    velocity_x, velocity_y = velocity

    while (
        position_x <= target_end_x
        and not (velocity_x == 0 and position_x < target_start_x)
    ) and position_y >= target_end_y:
        position_x += velocity_x
        position_y += velocity_y
        velocity_x = (
            (velocity_x - 1)
            if velocity_x > 0
            else ((velocity_x + 1) if velocity_x < 0 else 0)
        )
        velocity_y -= 1

        if (target_start_x <= position_x <= target_end_x) and (
            target_start_y >= position_y >= target_end_y
        ):
            return True

    return False


count = 0
for x in range(1, target_end_x + 1):

    for y in range(target_end_y, 200):
        will_land_in_target = launch_probe((x, y))
        if will_land_in_target:
            count += 1

answer_part_two = count
answer_part_two
