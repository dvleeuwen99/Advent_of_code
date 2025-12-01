input = []
from math import trunc

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

program = []
for i in input:
    if 'A' in i:
        A = int(i.split(': ')[1])
    elif 'B' in i:
        B = int(i.split(': ')[1])
    elif 'C' in i:
        C = int(i.split(': ')[1])
    elif 'Program' in i:
        program = [*map(int,i.split(': ')[1].split(','))]
        ans_program = i.split(': ')[1]


def get_register(a, b, c, opcode):
    if opcode <= 3:  # assume the opcode is in bounds
        return opcode
    elif opcode == 4:
        return a
    elif opcode == 5:
        return b
    else:
        return c


def test(a, program, end, out_index):
    b = c = 0
    pc = 0
    while pc < end:
        instruction, opcode = program[pc:pc+2]
        if instruction == 0:
            a = a >> get_register(a, b, c, opcode)

        elif instruction == 1:
            b ^= opcode

        elif instruction == 2:
            b = get_register(a, b, c, opcode) % 8

        elif instruction == 3:
            if a != 0:
                pc = opcode
                continue

        elif instruction == 4:
            b ^= c

        elif instruction == 5:
            output = get_register(a, b, c, opcode) % 8
            if output != program[out_index]:
                return False
            out_index += 1

        elif instruction == 6:
            b = a >> get_register(a, b, c, opcode)

        else:
            c = a >> get_register(a, b, c, opcode)

        pc += 2
    return out_index == end


def main(program):
    end = len(program)

    # 0 gets the initial 0 and no more
    in_progress = [(0, len(program) - 1)]
    while len(in_progress) > 0:
        a, distance = in_progress.pop(0)
        for chunk in range(8):
            next_a = (a << 3) + chunk
            if not test(next_a, program, end, distance):
                continue

            if distance == 0:
                return next_a

            in_progress.append((next_a, distance - 1))

    return None

print(main(program))