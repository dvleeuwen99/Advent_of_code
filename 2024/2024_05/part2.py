input = []
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

# print(input)
rules = []
updates = []
for i in input:
    if '|' in i:
        f, s = i[:2],i[-2:]
        rules.append([int(f),int(s)])
    elif ',' in i:
        update = [*map(int,i.split(','))]
        updates.append(update)

# print(rules)
# print(updates)

total = 0
wrongs = []
for update in updates:
    unsafe = False
    for r in rules:
        if r[0] in update and r[1] in update:
            for u in update:
                if u == r[1]:
                    unsafe = True
                    break
                elif u == r[0]:
                    break
    if unsafe == False:
        middle = int((len(update) - 1)/2)
        total += update[middle]
    else:
        wrongs.append(update)

print(total)
# print(wrongs)

total2 = 0
for w in wrongs:
    # print(w)
    accepted_rules = []
    for r in rules:
        if r[0] in w and r[1] in w:
            accepted_rules.append(r)
    # print(accepted_rules)
    for u in w:
        cf = 0
        cs = 0
        for a in accepted_rules:
            if u == a[0]:
                cf += 1
            elif u == a[1]:
                cs += 1
        if cf == cs:
            total2 += u
print(total2)