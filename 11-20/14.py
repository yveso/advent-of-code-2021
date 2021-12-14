#%%
with open("./14_input.txt", "r") as file:
    start_pattern = file.readline().rstrip()

    file.readline()

    insertion_rules = {
        key: value
        for key, value in [line.rstrip().split(" -> ") for line in file.readlines()]
    }

start_pattern, len(insertion_rules)

#%%
from collections import Counter

count_steps = 10
pattern = start_pattern

for step in range(count_steps):
    next_pattern = []
    for i, _ in enumerate(pattern[:-1]):
        current_pair = pattern[i] + pattern[i + 1]
        to_be_inserted = insertion_rules[current_pair]

        if i == 0:
            next_pattern.append(current_pair[0])
        next_pattern.append(to_be_inserted)
        next_pattern.append(current_pair[1])

    pattern = "".join(next_pattern)

most_common_letters = Counter(pattern).most_common()
answer_part_one = most_common_letters[0][1] - most_common_letters[-1][1]
answer_part_one

#%%
from collections import defaultdict

count_steps = 40
element_counts = defaultdict(int)
pair_counts = defaultdict(int)

for element in start_pattern:
    element_counts[element] += 1

for i, _ in enumerate(start_pattern[:-1]):
    pair_counts[start_pattern[i] + start_pattern[i + 1]] += 1

for step in range(count_steps):
    new_pairs = defaultdict(int)
    for pair in pair_counts.keys():
        occurrence_of_pair = pair_counts[pair]
        to_be_inserted = insertion_rules[pair]

        element_counts[to_be_inserted] += occurrence_of_pair

        new_pairs[pair[0] + to_be_inserted] += occurrence_of_pair
        new_pairs[to_be_inserted + pair[1]] += occurrence_of_pair

    pair_counts = new_pairs

answer_part_two = max(element_counts.values()) - min(element_counts.values())
answer_part_two
