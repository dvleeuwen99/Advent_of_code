input = []

with open('input.txt', 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

print(input)
file = True
id = 0
files = []
space = []
for i in input[0]:
    if file:
        files.append((int(i),id))
        file = not file
        id += 1
    else:
        space.append((int(i)))
        file = not file
    

# print(files)
# print(space)
result = []
for s in space:
    if files != []:
        result.append(files[0])
        del files[0]
        while s > 0 and files != []:
            if files[-1][0] <= s:
                s -= files[-1][0]
                result.append(files[-1])
                del files[-1]
            else:
                # print(files[-1], s)
                stay = files[-1][0] - s, files[-1][1]
                go = s, files[-1][1]
                del files[-1]
                files.append(stay)
                result.append(go)
                s = 0

# print(result, files)
checksum = 0
index = 0
for r in result:
    for i in range(r[0]):
        checksum += index * r[1]
        index += 1

print(checksum)


