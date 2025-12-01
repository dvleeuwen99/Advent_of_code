input = []

with open('input.txt', 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

print(input)
total = 0
for i in input:
    parts = i.split(" ")
    decreasing = True
    increasing = True
    safe = True
    for p in range(1,len(parts)):
        if int(parts[p]) == int(parts[p-1]):
            safe = False
            break
        elif int(parts[p]) > int(parts[p-1]):
            decreasing = False
            if int(parts[p]) - int(parts[p-1]) >= 4:
                safe = False
        else:
            if int(parts[p]) - int(parts[p-1]) <= -4:
                safe = False
            increasing = False
    if not increasing and not decreasing:
        safe = False
    if safe == True:
        # print(i)
        total += 1

print(total)


        
        