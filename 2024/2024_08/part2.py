grid = set()
locations = set()
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test1.txt')

with open(file_path, 'r') as file:
    for r, line in enumerate(file):
        # process each line
        line = line.strip()
        for l,x in enumerate(line):
            grid.add((r,l,x))
            locations.add((r,l))
 
# print(locations)

antinodes = set()
antennas = set()
for g in grid:
    if g[2].isdigit() or g[2].isalpha():
        antennas.add(g)

# print(antennas)

for a in antennas:
    for b in antennas:
        if a != b and a[2] == b[2]:
            d0 = b[0] - a[0]
            d1 = b[1] - a[1]
    
            aloc = (a[0],a[1])
            i = 0
            while aloc in locations:
                i += 1
                antinodes.add(aloc)
                aloc = (a[0] - i*d0, a[1] - i*d1)

            bloc = (b[0],b[1])
            i = 0
            while bloc in locations:
                i += 1
                antinodes.add(bloc)
                bloc = (b[0] + i*d0, b[1] + i*d1)

# print(antinodes)           
print(len(antinodes)) 