input = []

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input.txt')

with open(file_path, 'r') as file:
    input = [line.strip() for line in file]

rolls = [[i, j] for j, row in enumerate(input) for i, char in enumerate(row) if char == '@']
start = len(rolls)

res1 = 0
# show the number of adjacent cells for each roll
for roll in rolls: 
    x, y = roll
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(input) and 0 <= nx < len(input[ny]):
                if input[ny][nx] == '@':
                    count += 1
        #count the number of rolls that have fewer than 4 adjacent rolls and add them up
    # print(f'Roll at ({x}, {y}) has {count} adjacent rolls.')
    if count < 4:
        res1 += 1

print('res1', res1)



#those with fewer than 4 adjacent rolls can be removed, so keep doing this until no more can be removed
#keep track of the number of removed rolls

removed_rolls = 0
changed = True
counting = 0
while changed:
    counting += 1
    if counting % 10 == 0:
        print(counting)
    changed = False
    new_rolls = []
    roll_set = set(tuple(roll) for roll in rolls)  
    for roll in rolls: 
        x, y = roll
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if (nx, ny) in roll_set: 
                    count += 1
        if count >= 4:
            new_rolls.append(roll)  
        else:
            changed = True
    rolls = new_rolls
print('Final number of iterations:', counting)
end = len(rolls)
print('res2', start - end)
