import re
import itertools

with open('input.txt') as input:
    input = [c.strip('\n') for c in input]

rows, columns = [], []
for idx,line in enumerate(input):
    galaxy = False
    length = len(line)
    for char in line:
        if char == '#':
            galaxy = True
    if galaxy == False:
        rows.append(idx)

for idx in range(length):
    galaxy = False
    for idy, line in enumerate(input):
        if input[idy][idx] == '#':
            galaxy = True
    if galaxy == False:
        columns.append(idx)

for idx, row in enumerate(rows):
    input.insert(row + idx + 1, ''.join('.' for c in range(length)))

for idx, line in enumerate(input):
    for idy, column in enumerate(columns):
        line = line[:(column + idy + 1)] + '.' + line[(column + idy + 1):]
        new_line = line
    input[idx] = new_line

# print(input)

galaxies = []
for idx,line in enumerate(input):
    for idy, char in enumerate(line):
        if char == '#':
            galaxies.append([idx, idy])

print(rows, columns)
print(galaxies)
total1 = 0
for idi, i in enumerate(galaxies):
    for idj, j in enumerate(galaxies):
        if i != j and idi > idj:
            distance = abs(i[0] - j[0]) + abs(i[1] - j[1]) 
            for idr, r in enumerate(rows):
                if i[0] < r + idr < j[0] or j[0] < r + idr < i[0]:
                    distance += 1000000 - 2
            for idc, c in enumerate(columns):
                if i[1] < c + idc < j[1] or j[1] < c + idc < i[1]:
                    distance += 1000000 - 2

            total1 += distance

print(total1)








    
