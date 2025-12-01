input = []

with open('input.txt', 'r') as file:
    for line in file:
        input = [*map(int,line.strip().split(' '))]

print(input)

def split_stones(input):
    new_input = []
    for i in input:
        if i == 0:
            new_input.append(1)
        elif len(str(i)) % 2 == 0:
            i = str(i)
            mid = len(i) // 2
            new_input.append(int(i[:mid]))
            new_input.append(int(i[mid:]))
        else:
            new_input.append(i*2024)
    # print(new_input)
    return new_input

blinks = 0
while blinks < 25:  
    blinks += 1
    print(blinks)
    input = split_stones(input)


print(len(input))

