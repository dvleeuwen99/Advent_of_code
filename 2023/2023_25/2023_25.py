import re
import itertools
from collections import deque
import networkx as nx

with open('input.txt') as input:
    input = [c.strip('\n') for c in input]

G = nx.Graph()

for line in input:
    node1, others = line.split(': ')
    others = others.split(' ')
    G.add_node(node1)
    for o in others:
        G.add_edge(node1, o)
        G.add_node(o)

print(G.nodes())

result = nx.minimum_edge_cut(G)
print(result)
G.remove_edges_from(result)
components = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
print(components)
total1 = components[0]*components[1]
print(total1)




                

                











    
