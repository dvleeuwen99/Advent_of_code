
with open('input.txt') as input:
    input = [c.strip('\n') for c in input]

time = input[0]
distance = input[1]

def get_digits(line):
    results = []
    number = False
    numbers = ''  
    for idx , c in enumerate(line):
        if number == True:
            if c.isdigit():
                numbers += c
                if idx + 1 == len(line):
                    number = False
                    results.append(int(numbers))
            else:
                number = False
                results.append(int(numbers))
                numbers = ''
        elif c.isdigit():
            number = True
            numbers += c
            if idx + 1 == len(time):
                number = False
                results.append(int(numbers))
                numbers = ''
        else:
            number = False
    return results

def get_one_number(line):
    number = False
    numbers = ''  
    for idx , c in enumerate(line):
        if number == True:
            if c.isdigit():
                numbers += c
                if idx + 1 == len(line):
                    number = False
            else:
                number = False
        elif c.isdigit():
            number = True
            numbers += c
            if idx + 1 == len(time):
                number = False
        else:
            number = False
    return int(numbers)

times = get_digits(time)
distances = get_digits(distance)
print('part 1:')
print(times, distances)


counts = []
for i,j in zip(times, distances):
    count = 0
    for t in range(1,i+1):
        result = t * (i-t)
        if result > j:
            count += 1
    counts.append(count)

total1 = 1
for count in counts:
    total1 *= count
print('result', total1)

#part 2

time2 = get_one_number(time)
distance2 = get_one_number(distance)

print('part 2:')
print(time2, distance2)
for t in range(1, time2):
    if t * (time2 - t) > distance2:
        firsttime = t
        break

for t2 in range(time2, 1, -1):
    if t2 * (time2 - t2) > distance2:
        secondtime = t2
        break

total2 = secondtime - firsttime + 1
print('result', total2)
    
    



