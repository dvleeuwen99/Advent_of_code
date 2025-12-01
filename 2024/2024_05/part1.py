input = []

with open('test1.txt', 'r') as file:
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

total = 0
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
        middle = len(update) // 2
        total += update[middle]
        # print(update)

print(total)
                    
