#%%
from dataclasses import dataclass
from typing import List


@dataclass
class NoteEntry:
    unique_signal_patterns: List[str]
    four_digit_output_value: List[str]


with open("./08_input.txt", "r") as file:
    entries = [
        NoteEntry(pattern.split(), output.split())
        for pattern, output in (line.rstrip().split(" | ") for line in file.readlines())
    ]

len(entries)

#%%
total = 0

for entry in entries:
    total += len([p for p in entry.four_digit_output_value if len(p) in [2, 4, 3, 7]])

answer_part_one = total
answer_part_one

#%%
def get_config(signal_patterns):
    digit_one_segments = set([s for s in signal_patterns if len(s) == 2][0])
    digit_seven_segments = set([s for s in signal_patterns if len(s) == 3][0])
    digit_four_segments = set([s for s in signal_patterns if len(s) == 4][0])
    digit_eight_segments = set([s for s in signal_patterns if len(s) == 7][0])

    # 7 - 1 is TOP
    TOP = list(digit_seven_segments - digit_one_segments)[0]

    # 4 - 1 leaves middle and upper_left
    upper_left_or_middle = digit_four_segments - digit_one_segments

    # 1 + 7 + 4 euqals "9 w/o BOTTOM"
    # on that base, only 8 and 9 are constructable
    # so 9 will lead to BOTTOM
    length_six_patterns = [s for s in signal_patterns if len(s) == 6]
    # Length 6 are: 0, 6, 9
    for pattern in length_six_patterns:
        # 9 - 7 - 4 (1 is already included in 7)
        tmp = set(pattern) - digit_seven_segments - digit_four_segments
        if len(tmp) == 1:
            nine_pattern = pattern
            BOTTOM = list(tmp)[0]

    # 8 leads to LOWER_LEFT
    LOWER_LEFT = list(
        digit_eight_segments - digit_seven_segments - digit_four_segments - {BOTTOM}
    )[0]

    length_five_patterns = [s for s in signal_patterns if len(s) == 5]
    # Length 5 are: 2, 3, 5
    # only 3 has 1 included
    three_pattern = [
        x for x in length_five_patterns if set(x).issuperset(digit_one_segments)
    ][0]
    # Intersection of 3 and (4-1) is MIDDLE
    MIDDLE = list(set(three_pattern).intersection(upper_left_or_middle))[0]
    # (4 - 1) - MIDDLE is UPPER_LEFT
    UPPER_LEFT = list(upper_left_or_middle - {MIDDLE})[0]

    # 8 - 6 is UPPER_RIGHT
    six_pattern = [
        pattern
        for pattern in length_six_patterns
        if pattern != nine_pattern and MIDDLE in pattern
    ][0]
    UPPER_RIGHT = list(digit_eight_segments - set(list(six_pattern)))[0]

    LOWER_RIGHT = list(digit_one_segments - {UPPER_RIGHT})[0]

    return {
        "TOP": TOP,
        "UPPER_LEFT": UPPER_LEFT,
        "UPPER_RIGHT": UPPER_RIGHT,
        "MIDDLE": MIDDLE,
        "LOWER_LEFT": LOWER_LEFT,
        "LOWER_RIGHT": LOWER_RIGHT,
        "BOTTOM": BOTTOM,
    }


def decode_digit(config, digit):
    digit_len = len(digit)
    if digit_len == 2:
        return 1
    elif digit_len == 3:
        return 7
    elif digit_len == 4:
        return 4
    elif digit_len == 7:
        return 8
    elif digit_len == 5:
        if config["LOWER_LEFT"] in digit:
            return 2
        elif config["UPPER_RIGHT"] in digit:
            return 3
        else:
            return 5
    elif digit_len == 6:
        if config["MIDDLE"] not in digit:
            return 0
        elif config["LOWER_LEFT"] in digit:
            return 6
        else:
            return 9


total = 0
for entry in entries:
    cfg = get_config(entry.unique_signal_patterns)
    total += int(
        "".join([str(decode_digit(cfg, d)) for d in entry.four_digit_output_value])
    )

answer_part_two = total
answer_part_two
