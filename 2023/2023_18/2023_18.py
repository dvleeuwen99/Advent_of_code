import re
import itertools

with open('input.txt') as input:
    input = [c.strip('\n') for c in input]

# print(input)
length_x = 1
length_y = 1
maxx = 0
maxy = 0
minx = 0
miny = 0
for line in input:
    direction, length, color = line.split(' ')
    if direction == 'R':
        length_x += int(length)
    if direction == 'L':
        length_x -= int(length)
    if direction == 'D':
        length_y += int(length)
    if direction == 'U':
        length_y -= int(length)
    maxx = max(length_x, maxx)
    maxy = max(length_y, maxy)
    miny = min(length_y, miny)
    minx = min(length_x, minx)
    past_direction = direction
print(maxy, maxx, miny, minx)
space = []
for y in range((maxy - miny) + 5):
    space.append([])
    for x in range((maxx - minx) + 5):
        space[y].append('.')
space[-miny+2][-minx+2] = 'F'
print(len(space))
print(len(space[0]))
current = [-miny+2,-minx+2]
print(current)
for line in input:
    direction, length, color = line.split(' ')
    if direction == 'R':
        new = [current[0],current[1]+int(length)]
        for n in range(current[1]+1, new[1]+1):
            space[current[0]][n] = '-'
        if past_direction == 'U':
            space[current[0]][current[1]] = 'F'
        if past_direction == 'D':
            space[current[0]][current[1]] = 'L'
        past_direction = 'R'
    if direction == 'L':
        new = [current[0],current[1]-int(length)]
        for n in range(new[1]+1, current[1]):
            space[current[0]][n] = '-'
        if past_direction == 'U':
            space[current[0]][current[1]] = '7'
        if past_direction == 'D':
            space[current[0]][current[1]] = 'J'
        past_direction = 'L'
    if direction == 'D':
        new = [current[0]+int(length),current[1]]
        for n in range(current[0]+1, new[0]+1):
            space[n][current[1]] = '|'
        if past_direction == 'L':
            space[current[0]][current[1]] = 'F'
        if past_direction == 'R':
            space[current[0]][current[1]] = '7'
        past_direction = 'D'
    if direction == 'U':
        new = [current[0]-int(length),current[1]]
        for n in range(new[0]+1, current[0]):
            space[n][current[1]] = '|'
        if past_direction == 'L':
            space[current[0]][current[1]] = 'L'
        if past_direction == 'R':
            space[current[0]][current[1]] = 'J'
        past_direction = 'U'
    current = new

print(space)
count = 0
for line in space:
    print(line)
    for column in line:
        if column != '.':
            count += 1

def count_area(mat):
  ans = 0
  for row in mat:
    interior = 0
    row = re.sub(r"F-*7|L-*J", "", "".join(row))
    row = re.sub(r"F-*J|L-*7", "|", row)
    row = row.strip('.')
    if len(row) > 1:
        print(row)
    for c in row:
      if c == "|":
        interior += 1
      if interior % 2 == 1 and c == ".":
        ans += 1
  return ans
print('res', count + count_area(space))




        


    
    
    








    
