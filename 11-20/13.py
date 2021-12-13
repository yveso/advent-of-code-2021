#%%
points = set()
instructions = []
with open("./13_input.txt", "r") as file:
    while line := file.readline().rstrip():
        x, y = line.split(",")
        points.add((int(x), int(y)))
    while line := file.readline().rstrip():
        direction, position = line.split()[-1].split("=")
        instructions.append((direction, int(position)))

paper_width = instructions[0][1] * 2 + 1
paper_height = instructions[1][1] * 2 + 1

paper = []
for y in range(paper_height):
    paper.append([True if (x, y) in points else False for x in range(paper_width)])

f"{len(points)=}, {len(instructions)=}, {paper_width=}, {paper_height=}"


#%%
def fold_x(paper, position):
    new_paper = []
    for row in paper:
        new_paper.append(
            [
                first or second
                for first, second in zip(row[:position], row[position + 1 :][::-1])
            ]
        )
    return new_paper


def fold_y(paper, position):
    new_paper = []
    for y in range(position):
        new_paper.append(
            [first or second for first, second in zip(paper[y], paper[-y - 1])]
        )
    return new_paper


#%%
paper_after_first_fold = fold_x(paper, instructions[0][1])

dots_after_first_fold = 0
for row in paper_after_first_fold:
    dots_after_first_fold += sum(1 if x else 0 for x in row)

answer_part_one = dots_after_first_fold
answer_part_one

#%%
next_paper = paper
for instruction in instructions:
    next_paper = (
        fold_x(next_paper, instruction[1])
        if instruction[0] == "x"
        else fold_y(next_paper, instruction[1])
    )

for row in next_paper:
    print("".join("#" if x else " " for x in row))

answer_part_two = "Check print output 🎅"
answer_part_two
