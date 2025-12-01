input = []

with open('input.txt', 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

locs = dict()
for ix, i in enumerate(input):
    for j in range(len(i)):
        locs[ix,j] = int(i[j])

print(locs)

def good_neighbours(neighbours, locs):
    new_neighbours = set()
    for n in neighbours:
        row, col = n[0], n[1]
        height = locs[n]
        directions = {(1,0),(-1,0),(0,1),(0,-1)}
        for d in directions:
            neighbour = (row+d[0], col+d[1])
            if neighbour in locs and locs[neighbour] == height + 1:
                new_neighbours.add(neighbour)
    height += 1
    if len(new_neighbours) >= 1:
        return new_neighbours, height
    else:
        return new_neighbours, 100

count = 0
for k in locs.keys():
    if locs[k] == 0:
        height = locs[k]
        neighbours = set([k])
        while height < 9:
            neighbours, height = good_neighbours(neighbours, locs)
            if height == 100:
                break
        if height == 9:
            count += len(neighbours)

print('count', count)







