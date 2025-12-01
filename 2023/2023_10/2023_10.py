import re

with open('input.txt') as input:
    input = [[char for char in c.strip('\n')] for c in input]

for idy,line in enumerate(input):
    length = len(line)
    for idx,char in enumerate(line):
        if char == 'S':
            y = idy
            x = idx

print(y, x, input[y][x])

location = [y, x]
steps = 0
path = [[y,x]]
if input[y-1][x] == '|' or input[y-1][x] == 'F':
    steps += 1
    location = [y-1, x]
    past_direction = 'south'
    first_direction = 'north'
elif input[y][x+1] == '-' or input[y][x+1] == 'J' or input[y][x+1] == '7':
    steps += 1
    location = [y, x+1]
    past_direction = 'west'
    first_direction = 'east'
elif input[y][x-1] == '-' or input[y][x-1] == 'F' or input[y][x-1] == 'L':
    steps += 1
    location = [y, x-1]
    past_direction = 'east'
    first_direction = 'west'

while location != [y,x]:
    if past_direction == 'south':
        steps += 1
        if input[location[0]][location[1]] == '|':
            past_direction = 'south'
            new_location = [location[0]-1, location[1]]
            path.append(location)
        elif input[location[0]][location[1]] == 'F':
            past_direction = 'west'
            new_location = [location[0], location[1]+1]
            path.append(location)
        elif input[location[0]][location[1]] == '7':
            past_direction = 'east'
            new_location = [location[0], location[1]-1]
            path.append(location)
        if new_location == [y,x]:
            last_direction = 'south'
    elif past_direction == 'north':
        steps += 1
        if input[location[0]][location[1]] == 'L':
            past_direction = 'west'
            new_location = [location[0], location[1]+1]
            path.append(location)
        elif input[location[0]][location[1]] == 'J':
            past_direction = 'east'
            new_location = [location[0], location[1]-1]
            path.append(location)
        elif input[location[0]][location[1]] == '|':
            past_direction = 'north'
            new_location = [location[0]+1, location[1]]
            path.append(location)
        if new_location == [y,x]:
            last_direction = 'north'
    elif past_direction == 'west':
        steps += 1
        if input[location[0]][location[1]] == 'J':
            past_direction = 'south'
            new_location = [location[0]-1, location[1]]
            path.append(location)
        elif input[location[0]][location[1]] == '-':
            past_direction = 'west'
            new_location = [location[0], location[1]+1]
            path.append(location)
        elif input[location[0]][location[1]] == '7':
            past_direction = 'north'
            new_location = [location[0]+1, location[1]]
            path.append(location)
        if new_location == [y,x]:
            last_direction = 'west'
    elif past_direction == 'east':
        steps += 1
        if input[location[0]][location[1]] == 'L':
            past_direction = 'south'
            new_location = [location[0]-1, location[1]]
            path.append(location)
        elif input[location[0]][location[1]] == '-':
            past_direction = 'east'
            new_location = [location[0], location[1]-1]
            path.append(location)
        elif input[location[0]][location[1]] == 'F':
            past_direction = 'north'
            new_location = [location[0]+1, location[1]]
            path.append(location)
        if new_location == [y,x]:
            last_direction = 'east'
    else:
        print('error with directions')
    location = new_location


total1 = int(steps / 2)
print(total1)

print(first_direction, last_direction)

count = 0
# clean matrix such that all non path chars are . and S gets the correct shape
for idy,line in enumerate(input):
    length = len(line)
    for idx,char in enumerate(line):
        if [idy,idx] not in path:
            input[idy][idx] = '.'
        if char == 'S':
            if (first_direction == 'north' and last_direction == 'south') or (last_direction == 'north' and first_direction == 'south'):
                input[idy][idx] = '|'
            if (first_direction == 'east' and last_direction == 'west') or (last_direction == 'east' and first_direction == 'west'):
                input[idy][idx] = '-'
            if (first_direction == 'north' and last_direction == 'east') or (last_direction == 'north' and first_direction == 'east'):
                input[idy][idx] = 'L'
            if (first_direction == 'north' and last_direction == 'west') or (last_direction == 'north' and first_direction == 'west'):
                input[idy][idx] = 'J'
            if (first_direction == 'west' and last_direction == 'south') or (last_direction == 'west' and first_direction == 'south'):
                input[idy][idx] = '7'
            if (first_direction == 'east' and last_direction == 'south') or (last_direction == 'east' and first_direction == 'south'):
                input[idy][idx] = 'F'


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

total2 = count_area(input)
print(total2)
