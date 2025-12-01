from itertools import repeat

with open('input.txt') as input:
    input = [c.strip('\n') for c in input]

print(input)

def check(lst):
    repeated = list(repeat(lst[0], len(lst)))
    return repeated == lst

def differences(line):
    level = []
    for idx, n in enumerate(line[:-1]):
        level.append(line[idx+1]-n)
    return level

new = []
for line in input:
    finish = False
    history = [int(x) for x in line.split(' ')] #part 1
    # history = [int(x) for x in line.split(' ')][::-1] #reversed for part 2
    level = differences(history)
    levels = [history]
    while finish == False:
        if not check(level):
            levels.append(level)
            level = differences(level)
        else:
            finish = True
            for i in levels[::-1]:
                i.append(i[-1] + level[-1])
                level = i
    new.append(levels[0][-1])

total = sum(new)

print(total)
