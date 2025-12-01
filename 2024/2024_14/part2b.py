input = []

from math import floor, ceil
import matplotlib.pyplot as plt

test = False
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

# print(input)

if test:
    rows = 11
    cols = 7

else:
    rows = 101 
    cols = 103

for time in range(15000):
    grid = [['.' for _ in range(0, rows + 1)] for _ in range(0, cols + 1)]
    for i in input:
        #parsing
        p, v = i.split(' ')[0][2:], i.split(' ')[1][2:]
        px,py = map(int,p.split(','))
        vx,vy = map(int,v.split(','))
        # print(px,py,vx,vy)

        nx = (px + time * vx) % rows
        ny = (py + time * vy) % cols
        grid[ny][nx] = '#'

    good_times = set()
    for ir, r in enumerate(grid):
        for ic, c in enumerate(r):
            if ic < cols - 10 and grid[ir][ic] == '#':
                good = True
                for _ in range(6):
                    ic += 1
                    if grid[ir][ic] == '#':
                        continue
                    else:
                        good = False
                if good:
                    if time not in good_times:
                        good_times.add(time)
                        print('TIME', time)
                        for row in grid:
                            print(''.join(row))


                