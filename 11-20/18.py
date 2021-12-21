#%%
import pathlib

with open(pathlib.Path(__file__).parent / "18_input.txt", "r") as file:
    # 😱😱😱
    snailfish_numbers = [eval(line) for line in file.readlines()]

len(snailfish_numbers)

#%%
from collections import namedtuple
import math

ExplodeResult = namedtuple(
    "ExplodeResult",
    "has_explosion_occoured new_number to_be_added_left to_be_added_right",
)

SplitResult = namedtuple("SplitResult", "has_split_occured new_number")


def add_to_the_left(snailfish_number, ammount):
    if isinstance(snailfish_number, int):
        return snailfish_number + ammount
    else:
        return [snailfish_number[0], add_to_the_left(snailfish_number[1], ammount)]


def add_to_the_right(snailfish_number, ammount):
    if isinstance(snailfish_number, int):
        return snailfish_number + ammount
    else:
        return [add_to_the_right(snailfish_number[0], ammount), snailfish_number[1]]


def check_for_explosion(number, nesting_level):
    if isinstance(number, int):
        return ExplodeResult(
            has_explosion_occoured=False,
            new_number=number,
            to_be_added_left=0,
            to_be_added_right=0,
        )
    if nesting_level == 4:
        return ExplodeResult(
            has_explosion_occoured=True,
            new_number=0,
            to_be_added_left=number[0],
            to_be_added_right=number[1],
        )
    result_left_part = check_for_explosion(number[0], nesting_level=nesting_level + 1)
    if result_left_part.has_explosion_occoured:
        return ExplodeResult(
            has_explosion_occoured=True,
            new_number=[
                result_left_part.new_number,
                add_to_the_right(number[1], result_left_part.to_be_added_right),
            ],
            to_be_added_left=result_left_part.to_be_added_left,
            to_be_added_right=0,
        )

    result_right_part = check_for_explosion(number[1], nesting_level=nesting_level + 1)
    if result_right_part.has_explosion_occoured:
        return ExplodeResult(
            has_explosion_occoured=True,
            new_number=[
                add_to_the_left(number[0], result_right_part.to_be_added_left),
                result_right_part.new_number,
            ],
            to_be_added_left=0,
            to_be_added_right=result_right_part.to_be_added_right,
        )

    return ExplodeResult(
        has_explosion_occoured=False,
        new_number=number,
        to_be_added_left=0,
        to_be_added_right=0,
    )


def check_for_split(number):
    if isinstance(number, int):
        return (
            SplitResult(
                has_split_occured=True,
                new_number=[math.floor(number / 2), math.ceil(number / 2)],
            )
            if number >= 10
            else SplitResult(has_split_occured=False, new_number=number)
        )

    result_left_part = check_for_split(number[0])
    if result_left_part.has_split_occured:
        return SplitResult(
            has_split_occured=True, new_number=[result_left_part.new_number, number[1]]
        )

    result_right_part = check_for_split(number[1])
    if result_right_part.has_split_occured:
        return SplitResult(
            has_split_occured=True, new_number=[number[0], result_right_part.new_number]
        )

    return SplitResult(has_split_occured=False, new_number=number)


def add(a, b):
    result = [a, b]
    while True:
        explosion = check_for_explosion(result, nesting_level=0)
        if explosion.has_explosion_occoured:
            result = explosion.new_number
            continue
        split = check_for_split(result)
        if split.has_split_occured:
            result = split.new_number
        else:
            break

    return result


def calculate_magnitude(number):
    if isinstance(number, int):
        return number
    return 3 * calculate_magnitude(number[0]) + 2 * calculate_magnitude(number[1])


#%%
snailfish_number_sum = snailfish_numbers[0]
for number in snailfish_numbers[1:]:
    snailfish_number_sum = add(snailfish_number_sum, number)

answer_part_one = calculate_magnitude(snailfish_number_sum)
answer_part_one

#%%
import itertools

# 🥴
answer_part_two = max(
    calculate_magnitude(add(a, b))
    for a, b in itertools.permutations(snailfish_numbers, 2)
)
answer_part_two
