from collections import deque

# Directions: East, South, West, North
directions = ['E', 'S', 'W', 'N']
dx = {'E': 1, 'S': 0, 'W': -1, 'N': 0}
dy = {'E': 0, 'S': 1, 'W': 0, 'N': -1}

maze = []
with open('input.txt', 'r') as file:
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

    queue = deque([(start[0], start[1], 'E', 0)])
    visited = {}
    scores = set()

    while queue:
        x, y, dir, score = queue.popleft()

        if (x, y, dir) in visited and visited[(x,y,dir)] <= score:
            continue
        else:
            visited[(x, y, dir)] = score

            if (x,y) == end:
                scores.add(score)

            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < cols and 0 <= ny < rows and maze[ny][nx] != '#':
                new = (nx,ny, dir, score + 1)
                if new not in queue:
                    queue.append(new)
            
            right_dir = directions[(directions.index(dir) + 1) % 4]
            new = (x,y,right_dir, score + 1000)
            if new not in queue:
                queue.append(new)

            left_dir = directions[(directions.index(dir) - 1) % 4]
            new = (x,y, left_dir, score + 1000)
            if new not in queue:
                queue.append(new)

    return min(scores)

total1 = find_min_score(maze)

print(total1)


