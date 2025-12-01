input = []

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

# print(input)
file = True
id = 0
files = []
for i in input[0]:
    if file:
        files.append([int(i),id])
        file = not file
        id += 1
    else:
        files.append([int(i),'s'])
        file = not file
    

# print(files)

result = [f for f in files]
while files != []:
    f = files[-1]

    if f[1] == 's':
        del files[-1]
        continue
    else:
        tried = False
        res = result.index(f)
        for ig,g in enumerate(result[:res]):
            if g[1] == 's' and f[0] <= g[0]:
                tried = True
                del files[-1]
                if f[0] == g[0]:
                    i = result.index(f)                    
                    result = result[:i]+[[f[0], 's']]+result[i+1:]
                    result = result[:ig] + [f] + result[ig+1:]
                else:
                    new_s = [[g[0]-f[0],'s']]
                    i = result.index(f)                    
                    result = result[:i]+[[f[0], 's']]+result[i+1:]
                    result = result[:ig] + [f] + new_s + result[ig+1:]
                    files = files[:ig] + files[ig+1:]
                break
        # print('result',result)
        if not tried:
            del files[-1]


# print('result', result)

checksum = 0
index = 0
for r in result:
    if r[1] == 's':
        for i in range(r[0]):
            index += 1
    else:
        for i in range(r[0]):
            checksum += index * r[1]
            index += 1

print(checksum)