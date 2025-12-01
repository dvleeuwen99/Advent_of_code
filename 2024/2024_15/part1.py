input = []
from math import sqrt

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    grid = dict()
    moves = []
    col = 0
    for line in file:
        if '#' in line:
            for row,l in enumerate(line):
                if line[row] != '\n':
                    grid[col,row] = line[row]
                if line[row] == '@':
                    robot = (col,row)
            col += 1
        elif len(line)<=1:
            continue
        else:
            for m in line:
                for move in range(len(m)):
                    if m[move] != '\n':
                        moves.append(m[move])

# print(grid)
# print(moves)
# print(robot)
d = dict()
d['>'] = (0,1)
d['<'] = (0,-1)
d['v'] = (1,0)
d['^'] = (-1,0)
for im, m in enumerate(moves):
    print('move:', im, m)
    place = robot
    line = []
    count = 0
    c = place[0]
    r = place[1]
    dc, dr = d[m]
    # print(c,r,dc,dr)
    check = (c+dc, r+dr)
    while check in grid.keys():
        if grid[check] == '#':
            break
        elif grid[check] == 'O':
            # print(check, count, grid[check])
            check = (c+(count+2)*dc, r+(count+2)*dr)
            count += 1
        elif grid[check] == '.':
            # print(check, count, grid[check])
            # print(place[0]+dc, place[1]+dr)
            grid[place[0]+dc, place[1]+dr] = '@'
            robot = place[0]+dc, place[1]+dr
            if count > 0:
                grid[place[0]+(count+1)*dc, place[1]+(count+1)*dr] = 'O'
            grid[place] = '.'
            break
    # print(grid)

# print(len(grid))
final_grid = []
total = 0
length = int(sqrt(len(grid)))
for c in range(length):
    gridline = []
    for r in range(length):
        gridline.append(grid[c,r])
        if grid[c,r] == 'O':
           total += 100 * c + r 
    final_grid.append(gridline)
print(final_grid)
print(total)

