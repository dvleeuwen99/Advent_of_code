import re
import itertools

with open('input.txt') as input:
    input = [list(k) for k in [c.strip('\n') for c in input]]

# print(input)
length_x = len(input[0]) - 1
length_y = len(input) - 1
print(length_x, length_y)

def visit(visits):
    new_visit = visits[0]
    visited.add(tuple((visits[0][1])))
    # print('new', new_visit)
    while new_visit in repeat:
        visited.add(tuple((visits[0][1])))
        visits.remove(visits[0])

        if len(visits) == 0:
            return visits
        else:
            new_visit = visits[0]
        # print('run', visits)
    if new_visit not in repeat:
        visited.add(tuple((visits[0][1])))
        repeat.append(new_visit)
    # print(new_visit)
    current = new_visit[1]
    # print('curr', current)
    direction = new_visit[0]
    # print('dir', direction)
    # print(input[current[0]][current[1]])
    visits.remove(visits[0])
    if input[current[0]][current[1]] == '.':
        if direction == 'E' and current[1] < length_x:
            visits.append(['E',[current[0], current[1] + 1]])
        if direction == 'W' and current[1] > 0:
            visits.append(['W',[current[0], current[1] - 1]])
        if direction == 'N' and current[0] > 0:
            visits.append(['N',[current[0] - 1, current[1]]])
        if direction == 'S' and current[0] < length_y:
            visits.append(['S',[current[0] + 1, current[1]]])
        # print('vis', visits)
    elif input[current[0]][current[1]] == '\\':
        if direction == 'E' and current[0] < length_y:
            visits.append(['S', [current[0] + 1, current[1]]])
        if direction == 'W' and current[0] > 0:
            visits.append(['N', [current[0] - 1, current[1]]])
        if direction == 'N' and current[1] > 0:
            visits.append(['W',[current[0], current[1] - 1]])
        if direction == 'S' and current[1] < length_x:
            visits.append(['E', [current[0], current[1] + 1]])
    elif input[current[0]][current[1]] == '/':
        if direction == 'E' and current[0] > 0:
            visits.append(['N', [current[0] - 1, current[1]]])
        if direction == 'W' and current[0] < length_y:
            visits.append(['S', [current[0] + 1, current[1]]])
        if direction == 'N' and current[1] < length_x:
            visits.append(['E',[current[0], current[1] + 1]])
        if direction == 'S' and current[1] > 0:
            visits.append(['W', [current[0], current[1] - 1]])
    elif input[current[0]][current[1]] == '|': 
        if direction == 'N' or direction == 'S':
            if direction == 'N' and current[0] > 0:
                visits.append(['N', [current[0] - 1, current[1]]])
            if direction == 'S' and current[0] < length_y:
                visits.append(['S', [current[0] + 1, current[1]]])
        else:
            if current[0] > 0:
                new = ['N', [current[0] - 1, current[1]]]
                visits.append(new)
            if current[0] < length_y:
                new = ['S', [current[0] + 1, current[1]]]
                visits.append(new)
    elif input[current[0]][current[1]] == '-':
        if direction == 'E' or direction == 'W':
            if direction == 'E' and current[1] < length_x:
                visits.append(['E',[current[0], current[1] + 1]])
            if direction == 'W' and current[1] > 0:
                visits.append(['W',[current[0], current[1] - 1]])
        else:
            if current[1] > 0:
                visits.append(['W', [current[0], current[1] - 1]])
            if current[1] < length_x:
                visits.append(['E', [current[0], current[1] + 1]])

    return visits

total2 = []
for i in range(length_x):
    repeat = []
    visited = set()
    visits = [['S', [0,i]]]
    print(visits)
    while len(visits) > 0:
        visits = visit(visits)
    total2.append(len(visited))
    repeat = []
    visited = set()
    visits = [['N', [length_x,i]]]
    print(visits)
    while len(visits) > 0:
        visits = visit(visits)
    total2.append(len(visited))
for j in range(length_y):
    repeat = []
    visited = set()
    visits = [['E', [j,0]]]
    print(visits)
    while len(visits) > 0:
        visits = visit(visits)
    total2.append(len(visited))
    repeat = []
    visited = set()
    visits = [['W', [j, length_y]]]
    print(visits)
    while len(visits) > 0:
        visits = visit(visits)
    total2.append(len(visited))
    


total = max(total2)
print(total)







    
