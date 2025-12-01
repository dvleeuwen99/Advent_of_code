designs = []

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        if ',' in line:
            options = line.strip().split(', ')
        elif len(line.strip()) == 0:
            continue
        else:
            designs.append(line.strip())

print(options)
print(designs)

def is_possible(possible, design, combi):
    if not design:  
        return True, combi

    for o in options:
        if design.startswith(o):  
            new_combi = combi + [o]  
            possible, new_combi = is_possible(possible, design[len(o):], new_combi)  
            if possible:
                return True, new_combi

    return False, combi  # No match found for the current design

count = 0
for design in designs:
    combi = []
    result, combi = is_possible(True, design, combi)
    if result:
        count += 1
        print("Combination found:", combi)
    else:
        print("No combination possible for:", design)

print("Total count:", count)