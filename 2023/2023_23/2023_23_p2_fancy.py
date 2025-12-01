from collections import deque

PATH = "."
FOREST = "#"
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
SLOPES = "><v^"


def is_valid(matrix, row, col):
    return (
        0 <= row < len(matrix)
        and 0 <= col < len(matrix[0])
        and matrix[row][col] != FOREST
    )


def part_one(matrix, start, end):
    slope_map = {slop: offset for slop, offset in zip(SLOPES, DIRECTIONS)}
    queue = deque([(start, set())])
    dist = 0
    while queue:
        (row, col), visited = queue.popleft()
        if (row, col) == end and len(visited) > dist:
            dist = len(visited)
        elif matrix[row][col] in SLOPES:
            dr, dc = slope_map[matrix[row][col]]
            new_row, new_col = row + dr, col + dc
            if (new_row, new_col) not in visited:
                queue.append(((new_row, new_col), visited | {(new_row, new_col)}))
        else:
            for new_row, new_col in find_neighbours(matrix, row, col):
                if (new_row, new_col) not in visited:
                    queue.append(((new_row, new_col), visited | {(new_row, new_col)}))
    return dist


def find_neighbours(matrix, row, col):
    neighbours = []
    for dr, dc in DIRECTIONS:
        new_row, new_col = row + dr, col + dc
        if is_valid(matrix, new_row, new_col):
            neighbours.append((new_row, new_col))
    return neighbours


def find_intersections(matrix):
    intersections = []
    for i, row in enumerate(matrix):
        for j, tile in enumerate(row):
            if tile != FOREST and len(find_neighbours(matrix, i, j)) > 2:
                intersections.append((i, j))
    return intersections


def bfs(matrix, start, intersections):
    distances = {}
    visited = set()
    queue = deque([(start, 0)])
    while queue:
        (row, col), dist = queue.popleft()
        if (row, col) in intersections and (row, col) != start:
            distances[(row, col)] = dist
            continue
        for new_row, new_col in find_neighbours(matrix, row, col):
            if (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append(((new_row, new_col), dist + 1))
    return {start: distances}


def dfs(graph, start, end):
    stack = deque([(start, 0, {start})])
    max_distance = 0
    while stack:
        node, current_distance, visited = stack.pop()
        if node == end:
            max_distance = max(max_distance, current_distance)
            continue
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                new_distance = current_distance + weight
                new_visited = visited | {neighbor}
                print(neighbor, new_distance, new_visited)
                stack.append((neighbor, new_distance, new_visited))
    return max_distance


with open('input2.txt', "r") as input_file:
    matrix = input_file.read().split("\n")
start = (0, matrix[0].index(PATH))
end = (len(matrix) - 1, matrix[-1].index(PATH))
print(part_one(matrix, start, end))

intersections = find_intersections(matrix)
nodes = [start] + intersections + [end]

graph = {}
for node in nodes:
    graph |= bfs(matrix, node, nodes)
print(graph)

print(dfs(graph, start, end))
