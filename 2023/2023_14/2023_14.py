import re
import itertools

with open('input.txt') as input:
    input = [list(k) for k in [c.strip('\n') for c in input]]

# print(input)
length = len(input[0])
def north(input):
    for row in range(len(input)-1,0,-1):
        for column in range(length):
            if input[row][column] == 'O':
                for i in range(row,-1,-1):
                    if input[i][column] == '#':
                        break
                    if input[i][column] == '.':
                        input[i][column] = 'O'
                        input[row][column] = '.'
                        break
    return input

def west(input):
    for column in range(length-1, 0, -1):
        for row in range(len(input)):
            if input[row][column] == 'O':
                for i in range(column, -1, -1):
                    if input[row][i] == '#':
                        break
                    if input[row][i] == '.':
                        input[row][i] = 'O'
                        input[row][column] = '.'
                        break
    return input

def south(input):
    for row in range(len(input)):
        for column in range(length):
            if input[row][column] == 'O':
                for i in range(row, len(input)):
                    if input[i][column] == '#':
                        break
                    if input[i][column] == '.':
                        input[i][column] = 'O'
                        input[row][column] = '.'
                        break
    return input

def east(input):
    for column in range(length):
        for row in range(len(input)):
            if input[row][column] == 'O':
                for i in range(column, length):
                    if input[row][i] == '#':
                        break
                    if input[row][i] == '.':
                        input[row][i] = 'O'
                        input[row][column] = '.'
                        break
    return input

def listToString(list):
    str1 = ''
    for list2 in list:
        for s in list2:
            str1 += ''.join(s)
    return str1

# print(input)
total1 = 0
length = len(input)
res1 = north(input)
for idx, row in enumerate(res1):
    for column in row:
        if column == 'O':
            total1 += length - idx
print('res1', total1)

cycle = 0
cycles = dict()
remaining = 0
while cycle < 10000:
    input = east(south(west(north(input))))
    res = listToString(input)
    if res in cycles.keys():
        print('current', cycle)
        print('match', cycles[res])
        match = cycles[res]
        length_cycle = cycle - cycles[res]
        print(length_cycle)
        for n in range(1000000000):
            sum = 1000000000 - cycles[res] - n*length_cycle
            if sum <= 0:
                remaining = length_cycle + sum
                break
        break
    cycles[res] = cycle
    cycle += 1 

print(remaining)

with open('input.txt') as input:
    input = [list(k) for k in [c.strip('\n') for c in input]]

cycle = 0
while cycle < match + remaining:
    input = east(south(west(north(input))))
    cycle += 1

total2 = 0
for idx, row in enumerate(input):
    for column in row:
        if column == 'O':
            total2 += length - idx
print('res2', total2)



    
