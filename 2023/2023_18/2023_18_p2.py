import re
import itertools
import numpy as np

with open('input.txt') as input:
    input = [c.strip('\n') for c in input]

# print(input)
length_x = np.int64(1)
length_y = np.int64(1)
maxx = np.int64(0)
maxy = np.int64(0)
minx = np.int64(0)
miny = np.int64(0)
for line in input:
    direction, length, color = line.split(' ')
    direction = color[-2]
    length = color[2:-2]
    length = int(length, 16)
    length = np.int64(length) 
    print(direction, length, color)
    if direction == '0':
        print('R')
        length_x += length
    if direction == '2':
        print('L')
        length_x -= length
    if direction == '1':
        print('D')
        length_y += length
    if direction == '3':
        print('U')
        length_y -= length
    maxx = max(length_x, maxx)
    maxy = max(length_y, maxy)
    miny = min(length_y, miny)
    minx = min(length_x, minx)

print(maxy, maxx, miny, minx)
space = []
lists = []
current = [-miny+1, -minx+1]
perimeter = 0
for line in input:
    direction, length, color = line.split(' ')
    direction = color[-2]
    length = color[2:-2]
    length = int(length, 16)
    length = np.int64(length) 
    perimeter += length
    if direction == '0':
        new = [current[0],current[1]+length]
        lists.append(new)
    if direction == '2':
        new = [current[0],current[1]-length]
        lists.append(new)
    if direction == '1':
        new = [current[0]+length,current[1]]
        lists.append(new)
    if direction == '3':
        new = [current[0]-length,current[1]]
        lists.append(new)
    current = new
print(lists)

res = 0
first = lists[-1]
for list in lists:
    second = list
    res1 = first[1]*second[0] - second[1]*first[0]
    res += res1
    print(res, res1)
    first = list
print(int(abs(res / 2) + perimeter / 2 + 1))