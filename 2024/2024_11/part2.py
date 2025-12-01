from collections import defaultdict

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        input = line


stones = defaultdict(int)
for stone in map(int, input.split(' ')):
    stones[stone] += 1

def run(stones):
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        length = len(str(stone))
        if stone == 0:
            new_stones[1] += count
        elif length%2 == 0:
            new_stones[stone // 10**(length//2)] += count
            new_stones[stone % 10**(length//2)] += count
        else:
            new_stones[stone*2024] += count
    return new_stones

for blink in range(25):
    stones = run(stones)

print(sum(stones.values()))

for blink in range(50):
    stones = run(stones)

print(sum(stones.values()))