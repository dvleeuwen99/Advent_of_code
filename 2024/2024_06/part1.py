input = []

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        input.append((list(line.strip())))

print(input)

rows,cols = len(input), len(input[0])

# find start
start = ()
for r in range(rows):
    if start == ():
        for c in range(cols):
            if input[r][c] == '^':
                start = [r,c]
                break
        
directions = [[1,0],[0,-1],[-1,0],[0,1]]

current = start
finish = False
direction = directions[2]
while not finish:
    r = current[0]
    c = current[1]
    input[r][c] = 'X'
    x,y = direction[0], direction[1]
    # print(r,c, direction)
    if r+x < 0 or c+y < 0 or r+x == rows or c+y == cols:
        finish = True
    elif input[r+x][c+y] == '#':
        if [x,y] == directions[0]:
            direction = directions[1]
        elif [x,y] == directions[1]:
            direction = directions[2]
        elif [x,y] == directions[2]:
            direction = directions[3]
        elif [x,y] == directions[3]:
            direction = directions[0]
    elif input[r+x][c+y] == '.':
        input[r+x][c+y] = 'X'
        current = [r+x, c+y]
    elif input[r+x][c+y] == 'X':
        current = [r+x, c+y]

# print(input)
count = 0
for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == 'X':
            count += 1
print(count)