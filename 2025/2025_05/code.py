input = []

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input.txt')

with open(file_path, 'r') as file:
    input = [line.strip() for line in file]

print(input)

# for item in input, if '-' in item, add to ranges, else add to IDs
ranges = []
ids = []
for item in input:
    if '-' in item:
        ranges.append(item)
    elif item == '':
        continue
    else:
        ids.append(item)

print("Ranges:", ranges)
print("IDs:", ids)

#for all ids, check if in any range, if in range add them to a set called fresh
fresh = set()
for id in ids:
    id_num = int(id)
    for range_item in ranges:
        start, end = map(int, range_item.split('-'))
        if start <= id_num <= end:
            fresh.add(id_num)
            break
print("Fresh IDs:", fresh)

res1 = len(fresh)
print("Result 1:", res1)

# for part 2, merge overlapping ranges and sum their lengths
ranges_int = sorted([tuple(map(int, r.split('-'))) for r in ranges])

merged = []
for start, end in ranges_int:
    if merged and start <= merged[-1][1] + 1:
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))

print("Merged Ranges:", merged)
res2 = sum(end - start + 1 for start, end in merged)
print("Result 2:", res2)