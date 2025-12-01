import re
import itertools

with open('input.txt') as input:
    input = [c.strip('\n') for c in input]

split_at = int()
for ix, line in enumerate(input):
    if line == '':
        split_at = ix

workflows = input[:split_at]
ratings = input[split_at+1:]

works = {}
for work in workflows:
    part, workflow = work.split('{')
    working = workflow.strip('}').split(',')
    new = []
    new.append(part)
    for w in working:
        if ':' in w:
            w = w.split(':')
            new.append(w)
        else:
            new.append([w])
    works[new[0]] = new[1:]

print(works)
total1 = 0

for rate in ratings:
    #prep
    x, m, a, s = rate.strip('{}').split(',')
    x, m, a, s = int(x[2:]), int(m[2:]), int(a[2:]), int(s[2:])
    value = 'in'
    while value != 'A' and value != 'R':
        for work in works[value]:
            if len(work) == 1:
                value = work[0]
            elif len(work) > 1:
                letter, math, res = work[0][0], work[0][1], work[0][2:]
                if math == '>':
                    if letter == 'x':
                        if x > int(res):
                            value = work[1]
                            break
                    if letter == 'm':
                        if m > int(res):
                            value = work[1]
                            break
                    if letter == 'a':
                        if a > int(res):
                            value = work[1]
                            break
                    if letter == 's':
                        if s > int(res):
                            value = work[1]
                            break
                elif math == '<':
                    if letter == 'x':
                        if x < int(res):
                            value = work[1]
                            break
                    if letter == 'm':
                        if m < int(res):
                            value = work[1]
                            break
                    if letter == 'a':
                        if a < int(res):
                            value = work[1]
                            break
                    if letter == 's':
                        if s < int(res):
                            value = work[1]
                            break
    if value == 'A':
        xmas = x + m + a + s
        total1 += xmas
print(total1)

x = [1, 4000]
m = [1, 4000]
a = [1, 4000]
s = [1, 4000]
aa = []
values = [['in', x, m, a, s]]
while len(values) >= 1:
    current = values[0]
    # print(current)
    test = current[0]
    x = current[1]
    m = current[2]
    a = current[3]
    s = current[4]
    if test == 'A':
        aa.append(current)
        values.remove(current)
    elif test == 'R':
        values.remove(current)
    else:
        values.remove(current)
        for work in works[test]:
            # print(work)
            if len(work) == 1:
                if work[0] != 'R':
                    values.append([work[0], x, m, a, s])
            elif len(work) > 1:
                letter, math, res = work[0][0], work[0][1], int(work[0][2:])
                # print(letter, math, res)
                if math == '>':
                    if letter == 'x':
                        if res > x[0] and res < x[1]:
                            new = [test, [x[0], res], m, a, s]
                            new2 = [work[1], [res + 1, x[1]], m, a, s]
                            values.append(new)
                            values.append(new2)
                            break
                    if letter == 'm':
                        if res > m[0] and res < m[1]:
                            new = [test, x, [m[0], res],  a, s]
                            new2 = [work[1], x, [res + 1, m[1]], a, s]
                            values.append(new)
                            values.append(new2)
                            break
                    if letter == 'a':
                        if res > a[0] and res < a[1]:
                            new = [test, x, m, [a[0], res], s]
                            new2 = [work[1], x, m, [res + 1, a[1]], s]
                            values.append(new)
                            values.append(new2)
                            break
                    if letter == 's':
                        if res > s[0] and res < s[1]:
                            new = [test, x, m, a, [s[0], res]]
                            new2 = [work[1], x, m, a, [res + 1, s[1]]]
                            values.append(new)
                            values.append(new2)
                            break
                elif math == '<':
                    if letter == 'x':
                        if res > x[0] and res < x[1]:
                            new = [work[1], [x[0], res - 1],m, a,  s]
                            new2 = [test, [res, x[1]], m, a,s]
                            values.append(new)
                            values.append(new2)
                            break
                    if letter == 'm':
                        if res > m[0] and res < m[1]:
                            new = [work[1], x, [m[0], res - 1], a,  s]
                            new2 = [test, x, [res, m[1]], a,s]
                            values.append(new)
                            values.append(new2)
                            break
                    if letter == 'a':
                        if res > a[0] and res < a[1]:
                            new = [work[1], x, m, [a[0], res - 1],s]
                            new2 = [test, x, m, [res, a[1]], s]
                            values.append(new)
                            values.append(new2)
                            break
                    if letter == 's':
                        if res > s[0] and res < s[1]:
                            new = [work[1], x, m, a, [s[0], res - 1]]
                            new2 = [test, x, m, a, [res, s[1]]]
                            values.append(new)
                            values.append(new2)
                            break


total2 = 0
for aaa in aa:
    x = aaa[1][1] - aaa[1][0] + 1
    m = aaa[2][1] - aaa[2][0] + 1
    a = aaa[3][1] - aaa[3][0] + 1
    s = aaa[4][1] - aaa[4][0] + 1
    res = x * m * a * s
    total2 += res
print(total2)