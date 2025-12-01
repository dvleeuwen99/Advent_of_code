input = []

with open('test1.txt', 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

print(input)