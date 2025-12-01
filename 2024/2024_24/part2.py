from collections import defaultdict
import copy

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
    

def calculate_z(wires, gates):
    new_gates = list()
    while gates:
        for g in gates:
            if g[0] in wires and g[2] in wires:
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
    return decimal

xs = list()
for w in wires.keys():
    if w.startswith('x'):
        xs.append((w,wires[w]))

xs = sorted(xs, reverse=True)
binary = ''
for x in xs:
    binary += str(x[1])
x = int(binary, 2)
print(binary, x)

ys = list()
for w in wires.keys():
    if w.startswith('y'):
        ys.append((w,wires[w]))

ys = sorted(ys, reverse=True)
binary = ''
for y in ys:
    binary += str(y[1])
y = int(binary, 2)
print(binary, y)

print(x,y)
z = 0
for g1 in gates:
    print('g1', g1)
    test_gates = []
    test_gates.append(g1)
    for g2 in gates:
        if g2 not in test_gates:
            test_gates.append(g2)
            old_g1 = copy.deepcopy(g1)
            old_g2 = copy.deepcopy(g2)
            new_g1 = copy.deepcopy([*g1[0:3], g2[3]])
            new_g2 = copy.deepcopy([*g2[0:3], g1[3]])
            for g3 in gates:
                if g3 not in test_gates:
                    print('g3',g3)
                    test_gates.append(g3)
                    for g4 in gates:
                        if g4 not in test_gates:
                            test_gates.append(g4)
                            old_g3 = copy.deepcopy(g3)
                            old_g4 = copy.deepcopy(g4)
                            new_g3 = copy.deepcopy([*g3[0:3], g4[3]])
                            new_g4 = copy.deepcopy([*g4[0:3], g3[3]])
                            for g5 in gates:
                                if g5 not in test_gates:
                                    print('g5',g5)
                                    test_gates.append(g5)
                                    for g6 in gates:
                                        if g6 not in test_gates:
                                            test_gates.append(g6)
                                            old_g5 = copy.deepcopy(g5)
                                            old_g6 = copy.deepcopy(g6)
                                            new_g5 = copy.deepcopy([*g5[0:3], g6[3]])
                                            new_g6 = copy.deepcopy([*g6[0:3], g5[3]])
                                            for g7 in gates:
                                                if g7 not in test_gates:
                                                    print('g7',g7)
                                                    test_gates.append(g7)
                                                    for g8 in gates:
                                                        if g8 not in test_gates:
                                                            test_gates.append(g8)
                                                            old_g7 = copy.deepcopy(g7)
                                                            old_g8 = copy.deepcopy(g8)
                                                            new_g7 = copy.deepcopy([*g7[0:3], g8[3]])
                                                            new_g8 = copy.deepcopy([*g8[0:3], g7[3]])
                                                            new_gates = copy.deepcopy(gates)
                                                            for t in test_gates:
                                                                new_gates.remove(t)
                                                            new_gates.append(new_g1)
                                                            new_gates.append(new_g2)
                                                            new_gates.append(new_g3)
                                                            new_gates.append(new_g4)
                                                            new_gates.append(new_g5)
                                                            new_gates.append(new_g6)
                                                            new_gates.append(new_g7)
                                                            new_gates.append(new_g8)
                                                            z = calculate_z(wires, new_gates)
                                                            if z == x + y:
                                                                print('found', g1,g2,g3,g4,g5,g6,g7,g8)
                                                                break 
                                                            test_gates.remove(g8)
                                                    test_gates.remove(g7)
                                            test_gates.remove(g6)
                                    test_gates.remove(g5)
                            test_gates.remove(g4)
                    test_gates.remove(g3)
            test_gates.remove(g2)
    test_gates.remove(g1)

