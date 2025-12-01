from collections import deque

with open('input.txt') as input:
    input = [c.strip('\n') for c in input]

spots = dict()
for iy, line in enumerate(input):
    for ix, row in enumerate(line):
        if row != '#':
            spots[(iy, ix)] = (row, set())
            spots[(iy, ix)][1].add(0)


dest = (len(input)-1, len(input[0])-2)

directions = [[0,1],[1,0],[-1,0],[0,-1]]
queue = deque([[0, 1, 0, 0, 0]])
count = 0
while queue:
    count += 1
    current = queue.popleft()
    distance = current[4]
    if (current[0],current[1]) == dest:
        continue
    else:
        if spots[(current[0],current[1])][0] == '.':
            for d in directions:
                new_row = current[0] + d[0]
                new_col = current[1] + d[1]
                if (new_row, new_col) in spots and (new_row, new_col) != (current[2],current[3]):
                    if spots[(new_row, new_col)][0] == 'v':
                        if d[0] == -1:
                            continue
                        else:
                            queue.append([new_row, new_col, current[0], current[1], distance + 1])
                            spots[(new_row, new_col)][1].add(distance + 1)
                    elif spots[(new_row, new_col)][0] == '^':
                        if d[0] == 1:
                            continue
                        else:
                            queue.append([new_row, new_col, current[0], current[1], distance + 1])
                            spots[(new_row, new_col)][1].add(distance + 1)
                    elif spots[(new_row, new_col)][0] == '>':
                        if d[1] == -1:
                            continue
                        else:
                            queue.append([new_row, new_col, current[0], current[1], distance + 1])
                            spots[(new_row, new_col)][1].add(distance + 1)
                    elif spots[(new_row, new_col)][0] == '<':
                        if d[1] == 1:
                            continue
                        else:
                            queue.append([new_row, new_col, current[0], current[1], distance + 1])
                            spots[(new_row, new_col)][1].add(distance + 1)
                    else:
                        queue.append([new_row, new_col, current[0], current[1], distance + 1])
                        spots[(new_row, new_col)][1].add(distance + 1)
        elif spots[(current[0],current[1])][0] == 'v':
            new_row = current[0] + 1
            new_col = current[1]
            queue.append([new_row, new_col, current[0], current[1], distance + 1])
            spots[(new_row, new_col)][1].add(distance + 1)
        elif spots[(current[0],current[1])][0] == '^':
            new_row = current[0] - 1
            new_col = current[1]
            queue.append([new_row, new_col, current[0], current[1], distance + 1])
            spots[(new_row, new_col)][1].add(distance + 1)
        elif spots[(current[0],current[1])][0] == '>':
            new_row = current[0]
            new_col = current[1] + 1
            queue.append([new_row, new_col, current[0], current[1], distance + 1])
            spots[(new_row, new_col)][1].add(distance + 1)
        elif spots[(current[0],current[1])][0] == '<':
            new_row = current[0]
            new_col = current[1] - 1
            queue.append([new_row, new_col, current[0], current[1], distance + 1])
            spots[(new_row, new_col)][1].add(distance + 1)
print(max(spots[dest][1]))












    
