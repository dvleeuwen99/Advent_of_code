import re
import itertools
import numpy as np
import sympy

with open('input2.txt') as input:
    array = np.array([line.replace('@', ',').split(', ') for line in input], np.int64)

print(array)
p, v, t = (sympy.symbols(f'{ch}(:3)') for ch in 'pvt')
equations = [
    array[i, j] + t[i] * array[i, 3 + j] - p[j] - v[j] * t[i]
    for i in range(3) for j in range(3)
]
print(equations)
print(sum(sympy.solve(equations, (*p, *v, *t))[0][:3]))
