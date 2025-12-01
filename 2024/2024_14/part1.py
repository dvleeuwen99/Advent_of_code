input = []

from math import floor, ceil

test = False
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))

# print(input)

if test:
    rows = 11
    cols = 7
    time = 100
else:
    rows = 101 
    cols = 103
    time = 100

q1 = (0, floor(rows / 2)),(0, floor(cols / 2))
q2 = (0, floor(rows / 2)), (ceil(cols / 2), cols)
q3 = (ceil(rows / 2), rows),(0, floor(cols / 2))
q4 = (ceil(rows / 2), rows), (ceil(cols / 2), cols)

Q1, Q2, Q3, Q4 = 0, 0, 0, 0

print(q1, q2, q3, q4)
for i in input:
    #parsing
    p, v = i.split(' ')[0][2:], i.split(' ')[1][2:]
    px,py = map(int,p.split(','))
    vx,vy = map(int,v.split(','))
    print(px,py,vx,vy)

    nx = (px + time * vx) % rows
    ny = (py + time * vy) % cols
    print(nx, ny)
    
    if q1[0][0] <= nx < q1[0][1] and q1[1][0] <= ny < q1[1][1]:
        Q1 += 1
    elif q2[0][0] <= nx < q2[0][1] and q2[1][0] <= ny < q2[1][1]:
        Q2 += 1
    elif q3[0][0] <= nx < q3[0][1] and q3[1][0] <= ny < q3[1][1]:
        Q3 += 1
    elif q4[0][0] <= nx < q4[0][1] and q4[1][0] <= ny < q4[1][1]:
        Q4 += 1
    else:
        continue
print(Q1, Q2, Q3, Q4)
print(Q1*Q2*Q3*Q4)





