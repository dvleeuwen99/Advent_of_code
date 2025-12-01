input = []

with open('input.txt', 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

from math import floor
from collections import deque, defaultdict

def mix(secret, value):
    secret = value ^ secret
    return secret

def prune(secret):
    secret = secret % 16777216
    return secret

def process(secret, steps, digit, change, best):
    if steps == 0:
        return secret, best, change, digit
    else:
        step1 = secret * 64
        secret = mix(secret, step1)
        step2 = prune(secret)
        step3 = floor(step2 / 32)
        secret = mix(secret, step3)
        step4 = prune(secret)
        step5 = step4 * 2048
        secret = mix(secret, step5)
        step6 = prune(secret)
        change.append(step6 % 10 - digit)
        if len(change) >= 5:
            change.popleft()
            digit = step6 % 10
            new_change = tuple(change)
            if new_change not in best.keys():
                best[new_change] += digit
        return process(step6, steps-1, digit, change, best)

new_best = defaultdict(int)

for i in input:
    best = defaultdict(int)
    i = int(i)
    secret, best, change, digit = process(i, 500, i % 10, deque(), best)
    secret, best, change, digit = process(secret, 500, digit, change, best)
    secret, best, change, digit = process(secret, 500, digit, change, best)
    secret, best, change, digit = process(secret, 500, digit, change, best)

    for key, value in best.items():
        new_best[key] += value

answer = max(new_best.values())
print(answer)
value = {i for i in new_best if new_best[i]==answer}
print("key by value:",value)
