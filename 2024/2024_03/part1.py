import re
input = []

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

# print(input)

total = 0
mul_regex = re.compile(r'(mul[(]\d{1,3},\d{1,3}[)])')
for i in input:
    # print(i)
    muls = mul_regex.findall(i)
    for m in muls:
        nums = m[4:-1].split(",")
        total += int(nums[0])*int(nums[1])

print(total)