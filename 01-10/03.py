#%%
with open("./03_input.txt", "r") as file:
    numbers = [number.rstrip() for number in file.readlines()]

total_count = len(numbers)
sample = numbers[0]

#%%
counter = [0 for _ in list(sample)]

for number in numbers:
    for i, bit in enumerate(number):
        counter[i] += int(bit)

gamma_rate_binary = "".join(
    "1" if count > (total_count / 2) else "0" for count in counter
)
gamma_rate_decimal = int(gamma_rate_binary, 2)

epsilon_rate_binary = "".join("1" if bit == "0" else "0" for bit in gamma_rate_binary)
epsilon_rate_decimal = int(epsilon_rate_binary, 2)

answer_part_one = gamma_rate_decimal * epsilon_rate_decimal
answer_part_one

#%%
def rating(original_numbers, bit_criteria_rule):
    candidates = original_numbers[:]

    for position in range(len(sample)):
        ones_in_position = sum(int(b[position]) for b in candidates)
        bit_criteria = bit_criteria_rule(ones_in_position, candidates)
        new_candidates = []

        for candidate in candidates:
            if candidate[position] == bit_criteria:
                new_candidates.append(candidate)

        candidates = new_candidates

        if len(candidates) == 1:
            return candidates[0]


oxygen_generator_rating_binary = rating(
    numbers,
    lambda count_ones, candidates: "1" if count_ones >= len(candidates) / 2 else "0",
)

co2_scrubber_rating_binary = rating(
    numbers,
    lambda count_ones, candidates: "1" if count_ones < len(candidates) / 2 else "0",
)

oxygen_generator_rating_decimal = int(oxygen_generator_rating_binary, 2)
co2_scrubber_rating_decimal = int(co2_scrubber_rating_binary, 2)

answer_part_two = oxygen_generator_rating_decimal * co2_scrubber_rating_decimal
answer_part_two
