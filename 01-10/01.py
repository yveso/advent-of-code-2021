#%%
with open("./01_input.txt", "r") as file:
    depths = [int(line.rstrip()) for line in file.readlines()]

assert len(depths) == 2000

#%%
answer_part_one = sum(
    [former < later for former, later in zip(depths[:-1], depths[1:])]
)

answer_part_one

#%%
last_index_with_two_followers = -(len(depths) % 3)

sliding_sums = [
    depths[i] + depths[i + 1] + depths[i + 2]
    for i, _ in enumerate(depths[:last_index_with_two_followers])
]

answer_part_two = sum(
    [former < later for former, later in zip(sliding_sums[:-1], sliding_sums[1:])]
)

answer_part_two
