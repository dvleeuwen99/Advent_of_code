input = []

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

# print(input)

def pick_k_digits(item, k):
    n = len(item)
    k = min(k, n)
    start = 0
    digits = []
    for i in range(k):
        rem = k - i
        end_idx = n - rem  # inclusive index where current choice can go up to
        max_digit = -1
        max_pos = start
        for j in range(start, end_idx + 1):
            d = int(item[j])
            if d > max_digit:
                max_digit = d
                max_pos = j
                if max_digit == 9:  # early exit, can't do better than 9
                    break
        digits.append(max_digit)
        start = max_pos + 1
    return digits

# choose how many digits to pick (set to any positive integer)
digits_to_take = 12

res_any = 0
for item in input:
    digits = pick_k_digits(item, digits_to_take)
    number = 0
    for d in digits:
        number = number * 10 + d
    res_any += number

print(f'res_{digits_to_take}', res_any)



        
