input = []

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    input = [line.strip().split() for line in file]

print(input)

res1 = 0
for i in range(len(input[0])):
    operation = input[-1][i]
    numbers = [int(input[j][i]) for j in range(len(input) - 1)]
    
    if operation == '*':
        result = 1
        for num in numbers:
            result *= num
    elif operation == '+':
        result = sum(numbers)
    else:
        result = 0
    res1 += result
print(res1)

with open(file_path, 'r') as file:
    input2 = [line for line in file]

print(input2)
block_num = 0
res2 = 0

# i need to process each column of the input separately, first print each column
for i in range(len(input2[0])-1):
    operation = input2[-1][i]
    digit_string = ''.join(char for j in range(len(input2) - 1) for char in input2[j][i] if char.isdigit())
    numbers = int(digit_string) if digit_string else 0
    if numbers == 0:
        block_num += 1
        res2 = set()
    else:
        if 'sets' not in locals():
            sets = []
            res2 = set()
        res2.add((operation, numbers))
        if block_num == len(sets):
            sets.append(res2)
        else:
            sets[block_num] = res2
print(sets)

#for each set, perform the operations
final_res = 0
for s in sets:
    temp_res = 0
    op = None
    nums = []
    for operation, number in s:
        if operation != ' ':  # Only one operation per set
            op = operation
            nums.append(number)
        else:
            nums.append(number)
    if op == '*':
        temp_res = 1
        for n in nums:
            temp_res *= n
    elif op == '+':
        temp_res = sum(nums)
    final_res += temp_res
print(final_res)