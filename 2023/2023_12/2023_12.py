import re
import itertools
import functools

with open('input.txt') as input:
    input = [c.strip('\n') for c in input]

@functools.lru_cache(maxsize=None)
def solve(s, inGroup, rest):
    if not s:
        if inGroup is None and len(rest) == 0:
            return 1
        if len(rest) == 1 and inGroup is not None and inGroup == rest[0]:
            return 1
        return 0
    possibleMore = 0
    for ch in s:
        if ch == '#' or ch == '?':
            possibleMore += 1
    if inGroup is not None and possibleMore + inGroup < sum(rest):
        return 0
    if inGroup is None and possibleMore < sum(rest):
        return 0
    if inGroup is not None and len(rest) == 0:
        return 0

    possible = 0
    if s[0] == '.' and inGroup is not None and inGroup != rest[0]:
        return 0
    if s[0] == '.' and inGroup is not None:
        possible += solve(s[1:], None, rest[1:])
    if (s[0] == '.' or s[0] == '?') and inGroup is None:
        possible += solve(s[1:], None, rest)
    if (s[0] == '#' or s[0] == '?') and inGroup is not None:
        possible += solve(s[1:], inGroup + 1, rest)
    elif (s[0] == '#' or s[0] == '?'):
        possible += solve(s[1:], 1, rest)
    if s[0] == '?' and inGroup is not None and inGroup == rest[0]:
        possible += solve(s[1:], None, rest[1:])
    return possible

total1 = 0
for line in input:
    question, numbers = line.split(' ')
    numbers = tuple([int(x) for x in numbers.split(',')])
    count = solve(question, None, numbers)
    print(count)
    total1 += count
print('total1', total1)

total2 = 0
for line in input:
    question, numbers = line.split(' ')
    numbers = tuple([int(x) for x in numbers.split(',')])*5
    new_question = question
    for i in range(4):
        new_question += '?'
        new_question += question
    print(new_question)
    count = solve(new_question, None, numbers)
    print(count)
    total2 += count
print('total2', total2)

    







    
