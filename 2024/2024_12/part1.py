def parse_input(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid

def calculate_cost(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def dfs(x, y, letter):
        stack = [(x, y)]
        visited[x][y] = True
        area = 0
        perimeter = 0

        while stack:
            cx, cy = stack.pop()
            area += 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if not in_bounds(nx, ny) or grid[nx][ny] != letter:
                    perimeter += 1
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
        return area, perimeter

    total_cost = 0
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                letter = grid[r][c]
                area, perimeter = dfs(r, c, letter)
                total_cost += area * perimeter

    return total_cost

# Example usage
grid = parse_input('input.txt')
print(calculate_cost(grid))

