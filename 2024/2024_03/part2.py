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
mul_regex = re.compile(r'(mul[(]\d{1,3},\d{1,3}[)])|(do\(\))|(don\'t\(\))')
dont = False
for i in input:
    print(i)
    muls = mul_regex.findall(i)
    for m in muls:
        print(m)
        if dont == False:
            if 'mul' in m[0]:
                nums = m[0][4:-1].split(",")
                total += int(nums[0])*int(nums[1])
            elif 'd' in m[1]:
                continue
            else:
                dont = True
        elif 'd' in m[1]:
            dont = False
        else:
            continue


print(total)