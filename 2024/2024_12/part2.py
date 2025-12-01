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
        corners = 0

        while stack:
            cx, cy = stack.pop()
            area += 1
            corner = 0
            turns = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if not in_bounds(nx, ny) or grid[nx][ny] != letter:
                    perimeter += 1
                    corner += 1
                    turns.append((nx,ny))
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
            if corner == 2:
                diff1 = turns[1][0]- turns[0][0]
                diff2 = turns[1][1]- turns[0][1]
                if diff1 == 0 or diff2 == 0:
                    continue
                else:
                    corners += 1
                    if grid[turns[1][0] + diff1][turns[0][1] - diff2] != letter:
                        corners += 1
            elif corner == 3:
                corners += 2
            elif corner == 4:
                corners += 4
            elif corner == 0:
                for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    nx, ny = cx + dx, cy + dy
                    if in_bounds(nx, ny) and grid[nx][ny] != letter:
                        corners += 1
                        print(cx, cy, nx, ny)
            elif corner == 1:
                print(turns)
                for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    nx, ny = cx + dx, cy + dy
                    if in_bounds(nx, ny) and grid[nx][ny] != letter:
                        side1 = grid[cx][ny]
                        side2 = grid[nx][cy]
                        if side1 == side2:
                            corners += 1
                            print(cx, cy, nx, ny)
        return area, perimeter, corners

    total_cost = 0
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                letter = grid[r][c]
                area, perimeter, corners = dfs(r, c, letter)
                print(letter, area, perimeter, corners)
                total_cost += area * corners

    return total_cost

# Example usage
grid = parse_input('input.txt')
print(calculate_cost(grid))

