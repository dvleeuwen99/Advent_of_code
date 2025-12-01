from collections import deque

with open('input.txt') as input:
    input = [c.strip('\n') for c in input]

spots = dict()
for iy, line in enumerate(input):
    for ix, row in enumerate(line):
        if row != '#':
            if row != '.':
                spots[(iy, ix)] = ('.', set())
            else:
                spots[(iy, ix)] = (row, set())
            spots[(iy, ix)][1].add(0)

directions = [[0,1],[1,0],[-1,0],[0,-1]]

corners = []
for spot in spots:
    intersection = 4
    for d in directions:
        if (spot[0]+d[0], spot[1]+d[1]) not in spots:
            intersection -= 1
    if intersection >= 3:
        corners.append(list(spot))

print(corners)

dest = (len(input)-1, len(input[0])-2)

queue = deque([[0, [[0, 0], [0, 1]], []]])
count = 0
new = deque([0])
while queue:
    current = queue.popleft()
    count += 1
    distance = current[0]
    corner_in_route = current[2]
    if count % 100000 == 0:
        print(distance)
    if (current[1][-1][0],current[1][-1][1]) == dest:
        continue
    else:
        for d in directions:
            news = []
            new_row = current[1][-1][0] + d[0]
            new_col = current[1][-1][1] + d[1]
            if (new_row, new_col) in spots and [new_row, new_col] not in current[1]:
                new = []
                new_point = [new_row, new_col]
                new.append(distance + 1)
                new.append([current[1][-1], new_point])
                if new_point in corners and new_point not in corner_in_route:
                    new_corner = [c for c in corner_in_route]
                    new_corner.append(new_point)
                    new.append(new_corner)
                    queue.append(new)
                    spots[(new_row, new_col)][1].add(distance + 1)
                elif new_point not in corners:
                    new.append(corner_in_route)
                    queue.append(new)
                    spots[(new_row, new_col)][1].add(distance + 1)

print('res', max(spots[dest][1]))

