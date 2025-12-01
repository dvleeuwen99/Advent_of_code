import re
import itertools

with open('input.txt') as input:
    input = [c.strip('\n') for c in input]

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    if x < line1[0][0] and xdiff[0] < 0:
        return 'past'
    elif x < line2[0][0] and xdiff[1] < 0:
        return 'past'
    elif x > line1[0][0] and xdiff[0] > 0:
        return 'past'
    elif x > line2[0][0] and xdiff[1] > 0:
        return 'past'
    else:
        return x, y

lines = []
for line in input:
    if line != '':
        now, later = line.split(' @ ')
        x1, y1, z1 = map(int, now.split(', '))
        dx, dy, dz = map(int, later.split(', '))
        x2 = x1 + dx
        y2 = y1 + dy
        z2 = z1 + dz
        lines.append(((x1, y1),(x2, y2)))

intersections = []
for ix, line in enumerate(lines):
    for ix2 in range(ix+1, len(lines)):
        intersections.append(line_intersection(line, lines[ix2]))

total1 = 0
minvalue = 200000000000000
maxvalue = 400000000000000
for i in intersections:
    if i != None and i != 'past':
        if i[0] > minvalue and i[0] < maxvalue and i[1] > minvalue and i[1] < maxvalue:
            total1 += 1

print(total1)

    











    
