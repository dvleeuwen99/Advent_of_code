input = []

from math import floor, ceil
import matplotlib.pyplot as plt

test = False
with open('input.txt', 'r') as file:
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


for time in range(20000):
    unique = True
    grid = [['.' for _ in range(0, rows + 1)] for _ in range(0, cols + 1)]
    for i in input:
        #parsing
        p, v = i.split(' ')[0][2:], i.split(' ')[1][2:]
        px,py = map(int,p.split(','))
        vx,vy = map(int,v.split(','))
        # print(px,py,vx,vy)

        nx = (px + time * vx) % rows
        ny = (py + time * vy) % cols
        if grid[ny][nx] == '#':
            unique = False
            break
        else:
            grid[ny][nx] = '#'
    
    if unique:
        print('TIME', time)
        for row in grid:
            print(''.join(row))

    
    