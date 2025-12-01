import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    input_text = file.read()  # Read the entire file content

blocks = input_text.strip().split("\n\n")  # Split input into groups by blank lines
keys = []
locks = []

for block in blocks:
    lines = block.split("\n")
    if lines[0].startswith("#####"):
        locks.append(lines)
    elif lines[0].startswith("....."):
        keys.append(lines)

# Output keys and locks
val_keys = []
for key in keys:
    values = []
    for k in range(len(key[0])):
        l = 0
        while l < len(key):
            if key[l][k] == '.':
                l += 1
            else:
                values.append((len(key)-l-1))
                break
    val_keys.append(values)


val_locks = []
for lock in locks:
    values = []
    for k in range(len(lock[0])):
        l = 0
        while l < len(lock):
            if lock[l][k] == '#':
                l += 1
            else:
                values.append(l-1)
                break
    val_locks.append(values)


pairs = 0
for k in val_keys:
    for l in val_locks:
        fit = True
        for t in range(len(k)):
            if k[t] + l[t] >= 6:
                fit = False
                break
        if fit:
            pairs += 1

print(pairs)