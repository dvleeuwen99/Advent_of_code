input = []

from collections import deque

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
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
    bytes = 12
    target = (6,6)
else:
    for r in range(71):
        for c in range(71):
            grid[r,c] = '.'
    bytes = 1024
    target = (70,70)

for b in range(bytes):
    grid[input[b]] = '#'

print(grid)

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
            if (nx, ny) in grid and grid[(nx, ny)] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))
    
    # If the target is not reachable, return -1
    return -1

# Example usage
start = (0, 0)
result = bfs(grid, start, target)
print("Shortest path steps:", result)
