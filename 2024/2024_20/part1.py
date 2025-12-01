grid = dict()
input = []

from collections import deque

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

print(input)

for r, i in enumerate(input):
    for c, j in enumerate(i):
        if j == 'S':
            start = (r,c)
            grid[r,c] = '.'
        elif j == 'E':
            target = (r,c)
            grid[r,c] = '.'
        else:
            grid[r,c] = j

print(grid, start, target)


def bfs(grid, start, target):
    # Define movement directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Initialize the queue for BFS
    queue = deque([(start, 0)])  # Each element is (position, steps)
    visited = set()
    visited.add(start)
    
    while queue:
        (x, y), steps = queue.popleft()
        
        # If we reach the target, return the number of steps
        if (x, y) == target:
            return steps
        
        # Explore all possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if the new position is within bounds and not a wall
            if (nx, ny) in grid and (nx, ny) not in visited:
                parent = (x,y)
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))
    
    # If the target is not reachable, return -1
    return -1


normal = bfs(grid, start, target)
print("Normal:", normal)

cheats = 0
steps = 0
for g in grid:
    steps += 1
    if steps % 100 == 0:
        print(steps)
    if grid[g] == '#':
        grid[g] = '.'
        cheat = bfs(grid,start,target)
        grid[g] = '#'
        if normal - cheat >= 100:
            cheats += 1
print('Cheats:', cheats)
