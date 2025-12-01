puzzles = []

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    AX, AY, BX, BY, PX, PY = None, None, None, None, None, None
    for line in file:
        if len(line) <= 3:
            continue
        else:
            puzzle = line.split(' ')
            if 'A:' in line:
                AX = puzzle[2][2:-1]
                AY = puzzle[3][2:-1]
            elif 'B:' in line:
                BX = puzzle[2][2:-1]
                BY = puzzle[3][2:-1]
            else:
                PX = puzzle[1][2:-1]
                if '\n' in line:
                    PY = puzzle[2][2:-1]
                else:
                    PY = puzzle[2][2:]
        if AX and BX and PX:
            puzzles.append([AX, AY, BX, BY, PX, PY]) 
            AX, AY, BX, BY, PX, PY = None, None, None, None, None, None

from math import floor

def solve_claw_machines(puzzle_data):
    def solve_equations(Ax, Ay, Bx, By, Px, Py):
        A = (Px*By - Py*Bx)/(By*Ax - Bx*Ay)
        B = (Px*Ay - Py*Ax)/(Bx*Ay - By*Ax)
        if floor(A) == A and floor(B) == B:
            cost = 3*floor(A) + floor(B)
            return cost
        else:
            return None

    total_prizes = 0
    total_cost = 0

    for puzzle in puzzle_data:
        Ax, Ay, Bx, By, Px, Py = map(int, puzzle)
        if p2:
            Px += 10000000000000
            Py += 10000000000000
        cost = solve_equations(Ax, Ay, Bx, By, Px, Py)
        if cost is not None:
            total_prizes += 1
            total_cost += cost

    return total_prizes, total_cost

p1, p2 = False, False

p1 = False
p2 = not(p1)
prizes, cost = solve_claw_machines(puzzles)
print(f"Total prizes won: {prizes}")
print(f"Minimum cost: {cost}")