import re
import itertools
import functools

with open('input.txt') as input:
    input = [c.strip('\n') for c in input]


@functools.lru_cache(maxsize=None)
def change(s, current):
    ascii = ord(s)
    current += ascii
    current *= 17
    current = current % 256
    return current

total1 = 0
for line in input:
    line = line.split(',')
    print(line)
    for item in line:
        current = 0
        for char in item:
           current = change(char, current)
        total1 += current

print(total1)

print('part 2')

total2 = 0
boxes = [[] for _ in range(256)]
for line in input:
    line = line.split(',')
    for item in line:
        if '=' in item:
            item, number = item.split('=')
            current = 0
            for char in item:
                current = change(char, current)
            if len(boxes[current])>0:
                changed = False
                for idx, items in enumerate(boxes[current]):
                    if item in items[0]:
                        changed = True
                        boxes[current][idx] = [item, number]
                        break
                if changed == False:
                    boxes[current].append([item,number])
            else:
                boxes[current].append([item, number])
                
        elif '-' in item:
            item = item[:-1]
            current = 0
            for char in item:
                current = change(char, current)
            for idx, items in enumerate(boxes[current]):
                    if item in items[0]:
                        boxes[current].remove(items)

for idx, box in enumerate(boxes):
    if len(box) != 0:
        for it, item in enumerate(box):
            total2 += (idx + 1) * (it + 1) * int(item[1])
print(total2)


    








    
