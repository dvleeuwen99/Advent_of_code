input = []
from math import trunc

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

program = []
for i in input:
    if 'A' in i:
        A = int(i.split(': ')[1])
    elif 'B' in i:
        B = int(i.split(': ')[1])
    elif 'C' in i:
        C = int(i.split(': ')[1])
    elif 'Program' in i:
        program = [*map(int,i.split(':')[1].split(','))]
        

output = str()
ix = 0
out = None
while ix < len(program): 
    p = (program[ix],program[ix+1])
    if p[1] <= 3:
        combo = p[1]
    elif p[1] == 4:
        combo = int(A)
    elif p[1] == 5:
        combo = int(B)
    elif p[1] == 6:
        combo = int(C)


    if p[0] == 0:
        A = trunc(A / (2**combo))
    elif p[0] == 1:
        B = B ^ p[1]
    elif p[0] == 2:
        B = combo % 8
    elif p[0]== 4:
        B = B ^ C
    elif p[0] == 5:
        out = combo % 8
    elif p[0] == 6:
        B = trunc(A / (2**combo))
    elif p[0] == 7: 
        C = trunc(A / (2**combo))

    if p[0] == 3 and A != 0:
        ix = p[1]
    else:
        ix += 2
    
    if out or out == 0:
        if len(output) > 0:
            output += ','+str(out)
        else:
            output += str(out)
        out = None

print(output)