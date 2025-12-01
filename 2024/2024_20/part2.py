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


def backtrace(parent, start, target):
    path = [target]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def bfs(grid, start, target):
    # Define movement directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Initialize the queue for BFS
    parent = {}
    queue = deque([(start, 0)])  # Each element is (position, steps)
    visited = set()
    visited.add(start)
    
    while queue:
        (x, y), steps = queue.popleft()
        
        # If we reach the target, return the number of steps
        if (x, y) == target:
            return backtrace(parent, start, target)
        
        # Explore all possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if the new position is within bounds and not a wall
            if (nx, ny) in grid and grid[(nx, ny)] == '.' and (nx, ny) not in visited:
                parent[nx,ny] = (x,y)
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))
    
    # If the target is not reachable, return -1
    return -1

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))


normal = bfs(grid, start, target)
print("Normal:", len(normal)-1)

cheats = 0
for i in range(len(normal)):
    if i % 1000 == 0:
        print(i)
    for j in range(i, len(normal)):
        distance = manhattan(normal[i], normal[j]) 
        if distance > 20:
            continue
        else:
            diff = j-i
            if diff - distance + 1 >= 100:
                cheats += 1

print('Cheats:', cheats)

