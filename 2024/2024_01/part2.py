input = []

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

print(input)

list1 = []
list2 = {}
for i in input:
    # print(i)
    parts = i.split(" ")
    # print(parts)
    p1 = int(parts[0])
    p2 = int(parts[-1])
    list1.append(p1)
    if p2 in list2:
        list2[p2] += 1
    else:
        list2[p2] = 1
# print(list1)
# print(list2)

sim = 0
for l in list1:
    if l in list2:
        sim += list2[l]*l
print(sim)
