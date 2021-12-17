#%%
import pathlib

with open(pathlib.Path(__file__).parent / "16_input.txt", "r") as file:
    input_hex = file.readline().rstrip()

input = "".join(format(int(c, base=16), "04b") for c in input_hex)

len(input)

#%%
from math import prod


def parse_packet(packet, pointer):
    packet_value = 0
    version = int(packet[pointer : pointer + 3], base=2)
    versions.append(version)
    pointer += 3

    type_id = int(packet[pointer : pointer + 3], base=2)
    pointer += 3

    if type_id == 4:
        # literal
        literal_bits = ""
        while packet[pointer] == "1":
            literal_bits += packet[pointer + 1 : pointer + 5]
            pointer += 5
        literal_bits += packet[pointer + 1 : pointer + 5]
        pointer += 5
        packet_value = int(literal_bits, base=2)
    else:
        # operator
        operator_values = []
        length_type_id = int(packet[pointer], base=2)
        pointer += 1
        if length_type_id == 0:
            total_length_subpackets = int(packet[pointer : pointer + 15], base=2)
            pointer += 15
            starting_pointer_subpackets = pointer
            while pointer < starting_pointer_subpackets + total_length_subpackets:
                pointer, value = parse_packet(packet, pointer)
                operator_values.append(value)
        else:
            count_subpackets = int(packet[pointer : pointer + 11], base=2)
            pointer += 11
            for _ in range(count_subpackets):
                pointer, value = parse_packet(packet, pointer)
                operator_values.append(value)

        packet_value = {
            0: lambda v: sum(v),
            1: lambda v: prod(v),
            2: lambda v: min(v),
            3: lambda v: max(v),
            5: lambda v: 1 if v[0] > v[1] else 0,
            6: lambda v: 1 if v[0] < v[1] else 0,
            7: lambda v: 1 if v[0] == v[1] else 0,
        }.get(type_id)(operator_values)

    return (pointer, packet_value)


versions = []
_, value = parse_packet(input, 0)
answer_part_one = sum(versions)
answer_part_two = value
answer_part_one, value
