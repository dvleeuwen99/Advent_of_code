input = []

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

print(input)

total = 0
for i in input:
    parts = i.split(" ")
    # print(parts)
    num = []
    for p in parts:
        n = int(p)
        num.append(n)
    distances = []
    for ix, m in enumerate(num):
        if ix > 0:
            num1 = num[ix - 1]
            num2 = num[ix]
            distances.append(num2 - num1)
    positives = 0
    negatives = 0
    big = 0
    same = 0
    for d in distances:
        if d < 0:
            negatives += 1
            if d < -3:
                big += 1
        elif d > 0:
            positives += 1
            if d > 3:
                big += 1  
        elif d == 0:
            same += 1
    # print(positives, negatives, big, same)
    if negatives == 0 and big == 0 and same <= 1:
        total += 1
    elif positives == 0 and big == 0 and same <= 1:
        total += 1
    elif same >= 2:
        continue
    else:
        # print(num)
        for r in range(len(num)):
            new = num[:r] + num[r+1:]
            # print(new)
            distances = []
            for ix, m in enumerate(new):
                if ix > 0:
                    num1 = new[ix - 1]
                    num2 = new[ix]
                    distances.append(num2 - num1)
            # print(distances)
            positives = 0
            negatives = 0
            big = 0
            same = 0
            for d in distances:
                if d < 0:
                    negatives += 1
                    if d < -3:
                        big += 1
                elif d > 0:
                    positives += 1
                    if d > 3:
                        big += 1  
                elif d == 0:
                    same += 1
            # print(positives, negatives, big, same)
            if negatives == 0 and big == 0 and same == 0:
                total += 1
                break
            elif positives == 0 and big == 0 and same == 0:
                total += 1
                break

print(total)
    
