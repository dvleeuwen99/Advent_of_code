from collections import defaultdict

input = []
wires = dict()
gates = list()

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip()))
        if ':' in line:
            wire, num = line.strip().split(': ')
            wires[wire] = int(num)
        elif '->' in line:
            gate, goal = line.strip().split(' -> ')
            gate = gate.split(' ')
            gate.append(goal)
            gates.append(gate)

def XOR(x,y):
    if x == 1 and y == 0:
        return 1
    elif x == 0 and y == 1:
        return 1
    else:
        return 0

def AND(x,y):
    if x == 1 and y == 1:
        return 1
    else:
        return 0
    
def OR(x,y):
    if x == 1 or y == 1:
        return 1
    else:
        return 0
    
new_gates = list()
while gates:
    for g in gates:
        if g[0] in wires and g[2] in wires:
            print(g)
            goal = g[3]
            if g[1] == 'OR':
                wires[goal] = OR(wires[g[0]],wires[g[2]])
            elif g[1] == 'AND':
                wires[goal] = AND(wires[g[0]],wires[g[2]])
            else:
                wires[goal] = XOR(wires[g[0]],wires[g[2]])
        else:
            new_gates.append(g)
    gates = new_gates
    new_gates = list()

zets = list()
for w in wires.keys():
    if w.startswith('z'):
        zets.append((w,wires[w]))

zets = sorted(zets, reverse=True)

binary = ''
for z in zets:
    binary += str(z[1])
decimal = int(binary, 2)
print(decimal)