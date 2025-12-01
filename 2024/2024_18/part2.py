input = []

from collections import deque

with open('input.txt', 'r') as file:
    for line in file:
        # process each line
        x, y = map(int,(line.strip().split(',')))
        input.append((x, y))

test = False
grid = dict()
if test:
    for r in range(7):
        for c in range(7):
            grid[r,c] = '.'
    target = (6,6)
else:
    for r in range(71):
        for c in range(71):
            grid[r,c] = '.'
    target = (70,70)



print(grid)

def bfs(grid, start, target):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([(start, 0)]) 
    visited = set()
    visited.add(start)
    
    while queue:
        (x, y), steps = queue.popleft()
        
        if (x, y) == target:
            return steps
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            

            if (nx, ny) in grid and grid[(nx, ny)] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))
    
    return -1

start = (0, 0)
for b in range(len(input)):
    if b % 500 == 0:
        print(b)
    grid[input[b]] = '#'
    result = bfs(grid, start, target)
    if result == -1:
        print('answer', input[b])
        break


