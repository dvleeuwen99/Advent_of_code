import re

def generate_perms(input):
    permutations = []
    if "_" not in input:
        return input
    first, rest = input.split("_",1)
    perms = generate_perms(rest)
    if type(perms) is list:
        for perm in perms:
            permutations.append(first + "+" + perm)
            permutations.append(first + "*" + perm)
    else:
        permutations.append(first + "+" + perms)
        permutations.append(first + "*" + perms)
    return permutations

def spl_eval(nums,ops):
    if len(ops) == 0:
        return int(nums[0])
    val = eval(nums[0]+ops[0]+nums[1])
    del nums[0]
    del nums[0]
    del ops[0]
    nums.insert(0, str(val))
    return spl_eval(nums, ops)

with open('input.txt', 'r') as file:
    map = {}
    for line in file:
        target, input = line.strip().split(': ')
        map[int(target)] = input.replace(" ", "_")

sum = 0

for t, target in enumerate(map):
    print(t)
    perms = generate_perms(map[target])
    for perm in perms:
        nums = re.findall(r"\d+", perm)
        ops = re.findall(r"[+*]", perm)
        if target == spl_eval(nums, ops):
            sum+=target
            break

print(sum)