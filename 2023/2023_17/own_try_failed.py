import re
import itertools

with open('input.txt') as input:
    input = [list(n) for n in [c.strip('\n') for c in input]]


for idy, row in enumerate(input):
    for idx, column in enumerate(row):
        input[idy][idx] = int(column)

length_x = len(input[0]) - 1
length_y = len(input) - 1
print(length_x, length_y)
print(input)
dest = [length_y, length_x]

paths = []
### hard coded the first path
paths.append([0,[0,0]])

count = 0
best = 1500
new_paths = []
count2 = 1
results = []
while len(paths) > 0:
    count += 1
    path = paths[0]
    if count > 10000000000:
        print(path)
        break
    if count % 50000 == 0:
        print(count, path)
    current = path[-1]
    correct = True
    almost0 = False
    almost1 = False
    if len(path) > 5:
        previous = path[-2]
        before = path[-3]
        other = path[-4]
        next = path[-5]
        if current[0] == previous[0] == before[0] == other[0] == next[0] or current[1] == previous[1] == before[1] == other[1] == next[1]:
            correct = False
        path1 = [path[0]]
        path2 = path[-5:]
        paths[0] = path1 + path2
        path = path1 + path2
        distance = length_y - path[-1][0] + length_x - path[-1][1]
        if path[0] >= (best - 3*distance):
            correct = False
    if correct == True and path[0] < best:
        if current == dest:
            new = path[0]
            best = min(new, best)
            print(new, best)
            print(path)
            results.append(path)
            if len(results) > 3:
                maxcost = 0
                for result in results:
                    maxcost = max(result[0], maxcost)
                    if maxcost == result[0]:
                        maxresult = result
                results.remove(maxresult)
            paths.remove(path)
        else:
            paths.remove(path)
        if current[0] > 0:
            new = [current[0]-1,current[1]]
            if new not in path:
                new_path = path + [new]
                new_path[0] += input[new[0]][new[1]]
                new_paths.append(new_path)
        if current[0] < length_y:
            new = [current[0]+1,current[1]]
            if new not in path:
                new_path = path + [new]
                new_path[0] += input[new[0]][new[1]]
                new_paths.append(new_path)
        if current[1] > 0:
            new = [current[0],current[1]-1]
            if new not in path:
                new_path = path + [new]
                new_path[0] += input[new[0]][new[1]]
                new_paths.append(new_path)
        if current[1] < length_x:
            new = [current[0],current[1]+1]
            if new not in path:
                new_path = path + [new]
                new_path[0] += input[new[0]][new[1]]
                new_paths.append(new_path)
    else:
        paths.remove(path)
    if len(paths) == 0:
        count2 += 1
        print(count2)
        result = []
        for item in new_paths:
            if item not in result:
                result.append(item)
        for new_path in result:
            if new_path[0]/count2 < 5 and new_path[0] < best:
                paths.append(new_path)
        new_paths = []

print('res', best)
print(results)


    
    
    
    

    









    
