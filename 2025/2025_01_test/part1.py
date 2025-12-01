input = []

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

print(input)
old = 50
res1 = 0
res2 = 0
for item in input:
    if item[0] == 'L':
        number = -int(item[1:])
    elif item[0] == 'R':
        number = int(item[1:])
    new = (old + number)
    if new % 100 == 0:
        res1 += 1 
    if number > 0:
        hits = new // 100 - old // 100
    else:
        hits = old // 100 - new // 100
        if old % 100 == 0:
            hits -= 1
        if new % 100 == 0:
            hits += 1
    if hits != 0:
        print(old,new)
        print('hits', hits)
    res2 += abs(hits)
    old = new % 100

print("part1:", res1)
print("part2:", res2)
