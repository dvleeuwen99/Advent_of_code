input = []

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for line in file:
        # process each line
        input.append((line.strip().split('-')))

import networkx as nx

G = nx.Graph()
for i in input:
    i = tuple(i)
    G.add_edge(*i)

cliques = list(nx.find_cliques(G))
max_length = 0
for l in cliques:
    len_l = len(l)
    max_length = max(max_length, len_l)
    if max_length == len_l:
        good = []
        good.append((l))
good = ','.join(sorted(tuple(*good)))
print(good)