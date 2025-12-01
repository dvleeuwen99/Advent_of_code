import re
import itertools

with open('input.txt') as input:
    input = [c.strip('\n') for c in input]

blocks = dict()
for ix, line in enumerate(input):
    one, two = line.split('~')
    x1, y1, z1 = map(int, one.split(','))
    x2, y2, z2 = map(int, two.split(','))
    input[ix] = [x1, y1, z1, x2, y2, z2]


input.sort(key=lambda x: min(x[5], x[2]))
count = 0
for line in input:
    block = []
    x1, y1, z1, x2, y2, z2 = line
    if x1 == x2 and y1 == y2:
        zmin = min(z1, z2)
        zmax = max(z1, z2)
        for z in range(zmin, zmax + 1):
            block.append((x1,y1,z))
    elif x1 == x2 and z1 == z2:
        ymin = min(y1, y2)
        ymax = max(y1, y2)
        for y in range(ymin, ymax + 1):
            block.append((x1,y,z1))
    elif y1 == y2 and z1 == z2:
        xmin = min(x1, x2)
        xmax = max(x1, x2)
        for x in range(xmin, xmax + 1):
            block.append((x,y1,z1))
    loc = set()
    for b in block:
        new_loc = (b[0],b[1])
        loc.add(new_loc)
        if new_loc not in blocks:
            blocks[new_loc] = []
    if len(loc) == 1:
        l = list(loc)[0]
        spot = 0
        if len(blocks[l]) >= 1:
            spot = blocks[l][-1][1]
        for b in block:
            blocks[(b[0],b[1])].append((count, spot+1))
            spot += 1
    else:
        spot = 0
        for l in loc:
            new_spot = 0
            if len(blocks[l]) >= 1:
                new_spot = blocks[l][-1][1]
            spot = max(new_spot, spot)
        for l in loc:
            blocks[l].append((count, spot+1))
    count += 1

supports = dict()
for block in blocks.values():
    length = len(block)-1
    for ix, b in enumerate(block):
        if ix < length:
            b2 = block[ix+1]
            if b[1] + 1 == b2[1] and b2[0] != b[0]:
                if b[0] in supports:
                    if b2[0] not in supports[b[0]]:
                        supports[b[0]].append(b2[0])
                else:
                    supports[b[0]] = [b2[0]]
supports = dict(sorted(supports.items()))
disint = set()
counts = dict()
supported = dict()
for c in range(count):
    counts[c] = 0
for s in supports:
    for s2 in supports[s]:
        counts[s2] += 1
        if s2 in supported:
            supported[s2].append(s)
        else:
            supported[s2] = [s]
for c in range(count):
    if c in supports:
        fine = True
        for s in supports[c]:
            if counts[s] <= 1:
                fine = False
        if fine == True:
            disint.add(c)
    else:
        disint.add(c)
print('res1', len(disint))

total2 = 0
for s in supports:
    fall = []
    new_fall = []
    for b in supports[s]:
        if counts[b] <= 1:
            new_fall.append(b)
            fall.append(b)
    while len(new_fall) >= 1:
        current_fall = []
        for n in new_fall:
            current_fall.append(n)
        new_fall = []
        for c in current_fall:
            if c in supports:
                for b in supports[c]:
                    support = True
                    for x in supported[b]:
                        if x not in fall:
                            support = False
                    if b not in fall and support:
                        new_fall.append(b)
                        fall.append(b)
    total2 += len(fall)

print('res2', total2)
            


            

    
        
    


