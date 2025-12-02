input = []

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip().split(',')))

print(input)
res1 = 0
res2 = 0
for item in input[0]:
    first, second = item.split('-')
    for i in range(int(first), int(second)+1):
        j = str(i)
        for k in range(2,len(j)+1):
            n = int(len(j)/k)
            if j[0:n] * k == j:
                if k == 2:
                    res1 += i
                res2 += i
                break
print('result part 1', res1)
print('result part 2', res2)