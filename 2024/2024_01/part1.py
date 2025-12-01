input = []

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

print(input)

total1 = []
total2 = []
for i in input:
    # print(i)
    parts = i.split(" ")
    # print(parts)
    p1 = int(parts[0])
    p2 = int(parts[-1])
    total1.append(p1)
    total2.append(p2)

stotal1 = sorted(total1)
stotal2 = sorted(total2)
# print(stotal1, stotal2)

total = 0
for i in range(len(total1)):
    total += abs(stotal1[i]-stotal2[i])

print(total)