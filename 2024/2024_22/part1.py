input = []

with open('input.txt', 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

print(input)

from math import floor

def mix(secret, value):
    secret = value ^ secret
    return secret

def prune(secret):
    secret = secret % 16777216
    return secret

def process(secret, steps):
    if steps == 0:
        return secret
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
        return process(step6, steps-1)

answer = 0
for i in input:
    i = int(i)
    i2 = process(i, 500)
    i3 = process(i2, 500)
    i4 = process(i3, 500)
    result = process(i4, 500)
    answer += result

print(answer)