data = open("input.txt").read()

patterns, towels = data.split("\n\n")

patterns = patterns.split(", ")

towels = towels.rstrip().split("\n")

from functools import cache

@cache
def count(t):
    cnt = 0
    for p in patterns:
        if t == '':
            return 1
        if t.startswith(p):
            cnt += count(t[len(p):])
    return cnt

total = 0
for t in towels:
    cnt = count(t)
    print(cnt, t)
    total += cnt

print(total)