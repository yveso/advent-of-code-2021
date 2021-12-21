#%%
from collections import namedtuple

Player = namedtuple("Player", "current_space total_score")

dice = {"next_roll": 1, "times_rolled": 0}
player_one = Player(current_space=8, total_score=0)
player_two = Player(current_space=9, total_score=0)


def roll(dice):
    roll = dice["next_roll"]
    dice["next_roll"] = roll + 1 if roll < 100 else 1
    dice["times_rolled"] += 1
    return roll


def move(player):
    rolled = sum(roll(dice) for _ in range(3))
    new_space = player.current_space + rolled
    new_space = new_space % 10 if new_space % 10 != 0 else 10
    new_score = player.total_score + new_space
    return Player(current_space=new_space, total_score=new_score)


while True:
    player_one = move(player_one)
    if player_one.total_score >= 1000:
        looser = player_two
        break
    player_two = move(player_two)
    if player_two.total_score >= 1000:
        looser = player_one
        break

answer_part_one = dice["times_rolled"] * looser.total_score
answer_part_one
