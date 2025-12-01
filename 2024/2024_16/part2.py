from collections import deque
from collections import defaultdict
import time

# Directions: East, South, West, North
directions = ['E', 'S', 'W', 'N']
dx = {'E': 1, 'S': 0, 'W': -1, 'N': 0}
dy = {'E': 0, 'S': 1, 'W': 0, 'N': -1}

maze = []
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        maze.append((line.strip()))

print(maze)

def find_min_score(maze):
    rows = len(maze)
    cols = len(maze[0])

    start = end = None
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)

    queue = deque([(start[0], start[1], 'E', 0, set())])
    visited = {}
    scores = defaultdict(list)

    while queue:
        x, y, dir, score, path = queue.popleft()
        new_path = set(path)
        new_path.add((x,y))
        if (x, y, dir) in visited and visited[(x,y,dir)] < score:
            continue
        else:
            visited[(x, y, dir)] = score

            if (x, y) == end:
                for n in new_path:
                    if n in scores[score]:
                        continue
                    else:
                        scores[score].append(n)

            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < cols and 0 <= ny < rows and maze[ny][nx] != '#':
                new = (nx,ny, dir, score + 1, new_path)
                if new not in queue:
                    queue.append(new)
            
            right_dir = directions[(directions.index(dir) + 1) % 4]
            new = (x,y,right_dir, score + 1000, new_path)
            if new not in queue:
                queue.append(new)

            left_dir = directions[(directions.index(dir) - 1) % 4]
            new = (x,y, left_dir, score + 1000, new_path)
            if new not in queue:
                queue.append(new)

    return scores

start_time = time.time()
scores = find_min_score(maze)

min_score = min(scores.keys())

min_path = scores[min_score]

path_length = len(min_path)
end_time = time.time()

print(f"Minimum score: {min_score}")
print(f"Path length: {path_length}")

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")



