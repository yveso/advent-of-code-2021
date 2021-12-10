#%%
with open("./10_input.txt", "r") as file:
    lines = [line.rstrip() for line in file.readlines()]

len(lines)

#%%
def get_first_incorrect_closing(line):
    stack = []
    for chunk in line:
        if chunk in "([{<":
            stack.append(chunk)
        else:
            if (
                (chunk == ")" and stack[-1] == "(")
                or (chunk == "]" and stack[-1] == "[")
                or (chunk == "}" and stack[-1] == "{")
                or (chunk == ">" and stack[-1] == "<")
            ):
                stack.pop()
            else:
                return chunk


incorrect_closings = [get_first_incorrect_closing(line) for line in lines]

answer_part_one = sum(
    {")": 3, "]": 57, "}": 1197, ">": 25137}.get(incorrect_closing)
    for incorrect_closing in incorrect_closings
    if incorrect_closing
)
answer_part_one

#%%
from statistics import median


def get_stack_if_line_is_incomplete(line):
    stack = []
    for chunk in line:
        if chunk in "([{<":
            stack.append(chunk)
        else:
            if (
                (chunk == ")" and stack[-1] == "(")
                or (chunk == "]" and stack[-1] == "[")
                or (chunk == "}" and stack[-1] == "{")
                or (chunk == ">" and stack[-1] == "<")
            ):
                stack.pop()
            else:
                return None
    return stack


def determine_line_ending(stack):
    return [
        {"(": ")", "[": "]", "{": "}", "<": ">"}.get(chunk) for chunk in reversed(stack)
    ]


def calculate_line_ending_score(finish):
    score = 0
    for chunk in finish:
        score *= 5
        score += {")": 1, "]": 2, "}": 3, ">": 4}.get(chunk)
    return score


scores = [
    calculate_line_ending_score(determine_line_ending(stack))
    for stack in (get_stack_if_line_is_incomplete(line) for line in lines)
    if stack
]

answer_part_two = median(sorted(scores))
answer_part_two
