input = []

with open('input.txt', 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip().split('-')))



triples = set()
for ix, i in enumerate(input):
    if ix % 100 == 0:
        print(ix)
    for j in input:
        if i[0] in j or i[1] in j and i != j:
            pair = j
            for k in input:
                if j != k and i != k:
                    if (k[0] in i and k[1] in j):
                        new_set = set((i[0],i[1],j[0],j[1],k[0],k[1]))
                        new_set = tuple(sorted(new_set))
                        for n in new_set:
                            if n.startswith('t'):
                                triples.add(new_set)

print(len(triples))



