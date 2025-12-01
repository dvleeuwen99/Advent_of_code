ans = 0
st = False
all_ops = set()
values = {}
gates = {}

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        if line.strip() == "":
            st = True
            continue
        if st:
            op1, op, op2, arrow, out_op = line.strip().split()
            gates[out_op] = (op1, op, op2)
            all_ops.add(out_op)
        else:
            op, val = line.strip().split()
            values[op[:-1]] = int(val)
            all_ops.add(op[:-1])

def evaluate(op):
    if op in values:
        return values[op]
    op1 = evaluate(gates[op][0])
    op2 = evaluate(gates[op][2])
    if gates[op][1] == "AND":
        return op1 & op2
    if gates[op][1] == "OR":
        return op1 | op2
    if gates[op][1] == "XOR":
        return op1 ^ op2
        

def inspect(op, depth=0):
    if op in values or depth >= 3:
        return op
    
    op1 = inspect(gates[op][0], depth+1)
    op2 = inspect(gates[op][2], depth+1)
    if gates[op][1] == "AND":
        return f"{op}{{({op1}) & ({op2})}}"
    if gates[op][1] == "OR":
        return f"{op}{{({op1}) | ({op2})}}"
    if gates[op][1] == "XOR":
        return f"{op}{{({op1}) ^ ({op2})}}"

def get_num(beg):
    digs = {}
    for op in all_ops:
        if op.startswith(beg):
            digs[int(op[1:])] = evaluate(op)

    x = max([k for k in digs])
    num = 0
    for i in range(x,-1,-1):
        num = 2*num + digs[i]
    return num

# Code I used to figure out which bits were wrong:
x = get_num("x")
y = get_num("y")
z = get_num("z")
print(bin(x+y),'right')
print(bin(z),'wrong')
#assert x+y ==z

# print(inspect("z06"))
# print(inspect("z07"))
# print(inspect("z08"))
# print(inspect("z09"))

# print(inspect("z14"))
# print(inspect("z15"))
# print(inspect("z16"))
# print(inspect("z17"))



# print(inspect("z31"))
# print(inspect("z32"))
# print(inspect("z33"))
# print(inspect("z34"))

# print(inspect("z37"))
# print(inspect("z38"))
# print(inspect("z39"))

print(",".join(sorted(("z08","cdj","z16","mrb","z32","gfm","dhm","qjd"))))